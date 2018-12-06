import argparse
import logging
import os
import pwd
import sys
import traceback

import psycopg2

from . import log
from .config import load_config
from .errors import GitlabArtifactsError, NoProjectError, InvalidCIConfigError
from .gitaly import GitalyClient
from .projects import find_project, list_projects, list_artifacts
from .archive import list_archive_artifacts, archive_artifacts, ArchiveStrategy
from .utils import tabulate, humanize_datetime, humanize_size, memoize
from .version import __version__

def switch_user():
    gluser = pwd.getpwnam('git')
    os.setgid(gluser.pw_gid)
    os.setuid(gluser.pw_uid)

@memoize(
    key=lambda args: (args[1].project.id, args[1].commit,) # memoize over project_id and commit
    )
def get_ci_config(gitaly, branch):
    oid, size, data = gitaly.get_tree_entry(
        branch,
        '.gitlab-ci.yml',
        )

    # Gitaly returns an empty response if not found
    if not oid:
        return None

    return data

def resolve_projects(db, gitaly, project_paths):
    projects = {}
    ci_config = {}
    for project_path in project_paths:
        try:
            project = find_project(db, project_path)

            # Load branches
            branches = gitaly.get_branches(project)
            for name, commit in branches:
                branch = project.add_branch(name, commit)

                # Load branch jobs via .gitlab-ci.yml
                config_data = get_ci_config(gitaly, branch)
                if not config_data:
                    # No config for this branch means CI has been turned off
                    log.warn('No .gitlab-ci.yml for {}'.format(
                            branch.tree_path()
                            )
                        )
                else:
                    branch.load_ci_config(config_data)

                    if not branch.job_names:
                        log.warn('No jobs found in .gitlab-ci.yml for {}'.format(
                                branch.tree_path()
                                )
                            )
        except (NoProjectError, InvalidCIConfigError) as e:
            # Continue loading projects even if a single project fails
            log.warn('Skipping {}. Reason: {}'.format(project_path, str(e)))
            log.debug(traceback.format_exc())
            continue

        projects[project.id] = project

    return projects

def get_args():
    parser = argparse.ArgumentParser(
        prog='glartifacts',
        description='GitLab Artifact Archiver')
    parser.add_argument(
        '-d', '--debug',
        action="store_true",
        help="show detailed debug information")
    parser.add_argument(
        '--verbose',
        action="store_true",
        help="show additional information")
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s v'+__version__)

    commands = parser.add_subparsers(dest='command', title='Commands', metavar='')
    listcmd = commands.add_parser("list", help='List build artifacts')
    listcmd.add_argument(
        "projects",
        metavar='PROJECT',
        nargs='*',
        help='project path whose artifacts will be listed')
    listcmd.add_argument(
        '-s', '--short',
        action='store_true',
        help='use a short list format that only prints project names')

    archivecmd = commands.add_parser("archive", help='Archive build artifacts for a project')
    archivecmd.add_argument(
        'projects',
        metavar='PROJECT',
        nargs='+',
        help='paths to the projects to archive')
    archivecmd.add_argument(
        '--dry-run',
        action="store_true",
        help='identify artifacts to be archived, but do not make any changes')
    archivecmd.add_argument(
        '-s', '--strategy',
        type=ArchiveStrategy.parse,
        choices=list(ArchiveStrategy),
        default=ArchiveStrategy.LASTGOOD_PIPELINE,
        help='select the archive strategy used to identify old artifacts (default: LASTGOOD_PIPELINE)',
        )
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return None

    if args.debug:
        log.setLevel(logging.DEBUG)
    elif args.verbose:
        log.setLevel(logging.INFO)

    return args

def show_projects(db, short_format=False):
    projects = list_projects(db)
    if not len(projects):
        raise GitlabArtifactsError("No projects were found with artifacts")

    if short_format:
        names = set(['/'.join((p['namespace'], p['project'])) for p in projects])
        print("\n".join(names))
        return

    rows = [['Project', 'Id','Jobs with Artifacts']]
    for p in projects:
        rows.append([
            '/'.join((p['namespace'], p['project'])),
            p['project_id'],
            p['artifact_count']
            ])
    tabulate(rows, sortby=dict(key=lambda r: r[0]))

def show_artifacts(projects, artifacts, scope, short_format=False, strategy=None):
    project_names = ['{} #{}'.format(p.full_path, id) for id, p in projects.items()]
    projects = ", ".join(sorted(project_names))
    if not len(artifacts):
        raise GitlabArtifactsError("No "+scope+" were found for "+projects)

    if short_format:
        print("\n".join(set([r['name'] for r in artifacts])))
        return

    print("Listing", scope, "for", projects, end="")
    if strategy:
        print(" using", strategy, "strategy", end="")
    print("\n")

    rows = [['Pipeline', 'Job', '', 'Scheduled At', 'Status', 'Ref', 'Tag?', 'Expiring?', 'Size']]
    for r in artifacts:
        rows.append([
            '#'+str(r['pipeline_id']),
            r['name'],
            '#'+str(r['job_id']),
            humanize_datetime(r['scheduled_at']),
            r['status'],
            r['ref'],
            'yes' if r['tag'] else 'no',
            'yes' if r['expire_at'] else 'no',
            humanize_size(r['size'])
            ])
    tabulate(rows, sortby=[
        dict(key=lambda r: (r[3]), reverse=True),
        dict(key=lambda r: (int(r[0][1:])), reverse=True),
        ])

def run_command(db, gitaly, args):
    projects = []
    if args.projects:
        projects = resolve_projects(db, gitaly, args.projects)
        if not projects:
            raise GitlabArtifactsError('No valid projects specified')

    if args.command == 'list':
        if projects:
            artifacts = list_artifacts(db, projects.keys())
            show_artifacts(projects, artifacts, "artifacts", args.short)
        else:
            show_projects(db, args.short)
    elif args.command == 'archive':
        if args.dry_run:
            artifacts = list_archive_artifacts(
                db,
                projects,
                args.strategy
                )
            show_artifacts(projects, artifacts, "expired artifacts", strategy=args.strategy)
        else:
            with db:
                archive_artifacts(db, projects, args.strategy)
    else:
        raise Exception("Command {} not implemented".format(args.command))

def glartifacts():
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.WARN,
        format='%(levelname)s: %(message)s')

    args = get_args()
    if not args:
        sys.exit(1)

    config = load_config()

    try:
        switch_user()
    except PermissionError:
        log.error("Permission Denied. Unable to switch to GitLab's git user.")
        return 1

    db = None
    try:
        db = psycopg2.connect(
            database=config['postgres']['dbname'],
            user=config['postgres']['user'],
            host=config['postgres']['host'],
            port=config['postgres']['port'],
            )

        with GitalyClient(config['gitaly']['address']) as gitaly:
            run_command(db, gitaly, args)

    finally:
        if db:
            db.close()

    return 0

def main():
    try:
        sys.exit(glartifacts())
    except Exception:  # pylint: disable=broad-except
        log.error(sys.exc_info()[1])
        if log.level == logging.DEBUG:
            traceback.print_exc()

        sys.exit(1)

if __name__ == '__main__':
    main()
