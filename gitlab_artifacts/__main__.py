import argparse
import logging
import os
import pwd
import sys

import psycopg2
import psycopg2.extras

from . import log
from .errors import GitlabArtifactsError, NoProjectError
from .projects import find_project, list_projects, list_artifacts
from .archive import list_archive_artifacts, archive_artifacts, ArchiveStrategy
from .utils import tabulate, humanize_size, humanize_datetime

def switch_user():
    gluser = pwd.getpwnam('gitlab-psql')
    os.setuid(gluser.pw_uid)
    os.setuid(gluser.pw_gid)

def resolve_project(db):
    class ResolveProject(argparse.Action):
        def __call__(self, parser, args, values, option_string=None):
            projects = {}
            for project_path in values:
                try:
                    pid = find_project(db, project_path)
                    projects[pid] = project_path
                except NoProjectError:
                    log.error("No project was found with the path %s", project_path)
                    return 1
            setattr(args, self.dest, projects)
    return ResolveProject

def get_args(db):
    parser = argparse.ArgumentParser(description='GitLab Artifact Archiver')
    parser.add_argument(
        '-d', '--debug',
        action="store_true",
        help="Show detailed debug information")
    parser.add_argument(
        '-v', '--verbose',
        action="store_true",
        help="Show additional information")

    commands = parser.add_subparsers(dest='command', metavar='COMMAND')
    commands.required = True
    listcmd = commands.add_parser("list")
    listcmd.add_argument(
        "projects",
        nargs='*',
        action=resolve_project(db),
        help='Project path whose artifacts will be listed')

    archivecmd = commands.add_parser("archive")
    archivecmd.add_argument(
        'projects',
        nargs='+',
        action=resolve_project(db),
        help='Paths to the projects to archive')
    archivecmd.add_argument(
        '--dry-run',
        action="store_true",
        help='Only print the artifacts that would be archived')
    archivecmd.add_argument(
        '-s', '--strategy',
        type=ArchiveStrategy.parse,
        choices=list(ArchiveStrategy),
        default=ArchiveStrategy.LASTGOOD_BUILD,
        help='Select the archive strategy used to identify old artifacts',
        )
    args = parser.parse_args()

    if args.debug:
        log.setLevel(logging.DEBUG)
    elif args.verbose:
        log.setLevel(logging.INFO)

    return args

def show_projects(db):
    rows = [['Project', 'Jobs with Artifacts']]
    for p in list_projects(db):
        rows.append([
            '/'.join([p['namespace'], p['project']]),
            p['artifact_count']
            ])
    tabulate(rows, sortby=dict(key=lambda r: r[0]))

    return 0

def show_artifacts(project_paths, artifacts, scope):
    projects = ", ".join(sorted(project_paths))
    if not len(artifacts):
        raise GitlabArtifactsError("No "+scope+" were found for "+projects)

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

    return 0

def main():
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.WARN,
        format='%(levelname)s: %(message)s')
    try:
        switch_user()
    except PermissionError:
        log.error("Unable to switch to gitlab-psql user")
        return 1

    gitlab = psycopg2.connect(
        database="gitlabhq_production",
        user="gitlab-psql",
        host="/var/opt/gitlab/postgresql",
        port="5432")

    args = get_args(gitlab)
    if not args:
        return 1

    if args.command == 'list':
        if args.projects:
            artifacts = list_artifacts(gitlab, args.projects.keys())
            show_artifacts(args.projects.values(), artifacts, "artifacts")
        else:
            show_projects(gitlab)
    elif args.command == 'archive':
        if args.dry_run:
            artifacts = list_archive_artifacts(
                gitlab,
                args.projects.keys(),
                args.strategy
                )
            show_artifacts(args.projects.values(), artifacts, "expired artifacts")
        else:
            archive_artifacts(gitlab, args.projects.keys(), args.strategy)
            gitlab.commit()

    return 0

if __name__ == '__main__':
    try:
        main()
    except Exception:  # pylint: disable=broad-except
        log.error(sys.exc_info()[1])
        sys.exit(1)

    sys.exit(0)
