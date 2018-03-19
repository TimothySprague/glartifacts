import argparse
import logging
import os
import pwd
import sys

import psycopg2
import psycopg2.extras

from . import log
from .errors import GitlabArtifactsError
from .projects import find_project, list_projects, list_artifacts
from .archive import list_archive_artifacts, archive_artifacts, ArchiveStrategy
from .utils import tabulate, humanize_size, humanize_datetime
from .version import __version__

def switch_user():
    gluser = pwd.getpwnam('gitlab-psql')
    os.setuid(gluser.pw_uid)
    os.setuid(gluser.pw_gid)

def resolve_projects(db, project_paths):
    projects = {}
    for project_path in project_paths:
        pid = find_project(db, project_path)
        projects[pid] = project_path

    return projects

def get_args():
    parser = argparse.ArgumentParser(prog='glartifacts', description='GitLab Artifact Archiver')
    parser.add_argument(
        '-d', '--debug',
        action="store_true",
        help="Show detailed debug information")
    parser.add_argument(
        '--verbose',
        action="store_true",
        help="Show additional information")
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
        help='Project path whose artifacts will be listed')
    listcmd.add_argument(
        '-s', '--short',
        action='store_true',
        help='Use a short list format that only prints project names')

    archivecmd = commands.add_parser("archive", help='Archive build artifacts for a project')
    archivecmd.add_argument(
        'projects',
        metavar='PROJECT',
        nargs='+',
        help='Paths to the projects to archive')
    archivecmd.add_argument(
        '--dry-run',
        action="store_true",
        help='Identify artifacts to be archived, but do not make any changes')
    archivecmd.add_argument(
        '-s', '--strategy',
        type=ArchiveStrategy.parse,
        choices=list(ArchiveStrategy),
        default=ArchiveStrategy.LASTGOOD_BUILD,
        help='Select the archive strategy used to identify old artifacts',
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
        print("\n".join(['/'.join([p['namespace'], p['project']]) for p in projects]))
        return

    rows = [['Project', 'Jobs with Artifacts']]
    for p in projects:
        rows.append([
            '/'.join(set(p['namespace'], p['project'])),
            p['artifact_count']
            ])
    tabulate(rows, sortby=dict(key=lambda r: r[0]))

def show_artifacts(project_paths, artifacts, scope, short_format=False):
    projects = ", ".join(sorted(project_paths))
    if not len(artifacts):
        raise GitlabArtifactsError("No "+scope+" were found for "+projects)

    if short_format:
        print("\n".join(set(r['name'] for r in artifacts)))
        return

    print("Listing", scope, "for", projects, "\n")
    rows = [['Job', 'Scheduled At', 'Built At', 'Status', 'Tag?', 'Expiring?', 'Size']]
    for r in artifacts:
        rows.append([
            r['name'],
            humanize_datetime(r['scheduled_at']),
            humanize_datetime(r['built_at']),
            r['status'],
            'yes' if r['tag'] else 'no',
            'yes' if r['expire_at'] else 'no',
            humanize_size(r['size'])
            ])
    tabulate(rows, sortby=[
        dict(key=lambda r: (r[0], r[1])),
        dict(key=lambda r: (r[2]), reverse=True)
        ])

def run_command(db, args):
    if args.command == 'list':
        if args.projects:
            projects = resolve_projects(db, args.projects)
            artifacts = list_artifacts(db, projects.keys())
            show_artifacts(projects.values(), artifacts, "artifacts", args.short)
        else:
            show_projects(db, args.short)
    elif args.command == 'archive':
        projects = resolve_projects(db, args.projects)
        if args.dry_run:
            artifacts = list_archive_artifacts(
                db,
                projects.keys(),
                args.strategy
                )
            show_artifacts(projects.values(), artifacts, "expired artifacts")
        else:
            with db:
                archive_artifacts(db, projects.keys(), args.strategy)
    else:
        raise Exception("Command {} not implemented".format(args.command))

def main():
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.WARN,
        format='%(levelname)s: %(message)s')

    args = get_args()
    if not args:
        return 1

    try:
        switch_user()
    except PermissionError:
        log.error("Unable to switch to gitlab-psql user")
        return 1

    db = None
    try:
        db = psycopg2.connect(
            database="gitlabhq_production",
            user="gitlab-psql",
            host="/var/opt/gitlab/postgresql",
            port="5432")

        run_command(db, args)

    finally:
        if db:
            db.close()

    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:  # pylint: disable=broad-except
        log.error(sys.exc_info()[1])
        sys.exit(1)
