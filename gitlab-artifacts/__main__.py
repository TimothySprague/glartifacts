import argparse
import os
import psycopg2
import psycopg2.extras
import pwd
import sys

from .errors import NoProjectError
from .projects import find_project, list_projects, list_artifacts
from .artifacts import list_archive_artifacts 
from .utils import tabulate, humanize_size

def switch_user():
    gluser = pwd.getpwnam('gitlab-psql')
    os.setuid(gluser.pw_uid)
    os.setuid(gluser.pw_gid)

def get_args():
    parser = argparse.ArgumentParser(description='GitLab Artifact Archiver')
    commands = parser.add_subparsers(dest='command', metavar='COMMAND')

    listcmd = commands.add_parser("list")
    listcmd.add_argument("project", nargs='?', help='Project path whose artifacts will be listed')

    archivecmd = commands.add_parser("archive")
    archivecmd.add_argument('projects', nargs='+',
                                help='Paths to the projects to archive')
    archivecmd.add_argument('--dry-run', action="store_true", help='Only print the artifacts that would be archived')
    return parser.parse_args()

def show_projects(db):
    rows = [['Project', 'Jobs with Artifacts']]
    for p in list_projects(db):
        rows.append([
            '/'.join([p['namespace'], p['project']]),
            p['artifact_count']
            ]
        )
    tabulate(rows, sortby=dict(key=lambda r:r[0]))

def show_artifacts(db, project_path):
    print("Listing artifacts for", project_path)
    rows = [['Job', 'Scheduled At', 'Built At', 'Status', 'Tag?', 'Expiring?', 'Size']]
    for r in list_artifacts(db, project_path):
        rows.append([
            r['name'],
            r['scheduled_at'],
            r['built_at'],
            r['status'],
            'yes' if r['tag'] else 'no',
            'yes' if r['expire_at'] else 'no',
            humanize_size(r['size'])
            ])
    tabulate(rows, sortby=[
        dict(key=lambda r:(r[0], r[1])),
        dict(key=lambda r:(r[2]), reverse=True)
        ])

def show_archive_artifacts(db, project_id):
    rows = [['Job', 'Scheduled At', 'Built At', 'Status', 'Tag?', 'Expiring?', 'Size']]
    for r in list_archive_artifacts(db, project_id):
        rows.append([
            r['name'],
            r['scheduled_at'],
            r['built_at'],
            r['status'],
            'yes' if r['tag'] else 'no',
            'yes' if r['expire_at'] else 'no',
            humanize_size(r['size'])
            ])
    tabulate(rows, sortby=[
        dict(key=lambda r:(r[0], r[1])),
        dict(key=lambda r:(r[2]), reverse=True)
        ])


def main():
    try:
        switch_user()
    except:
        print("Unable to switch to gitlab-psql user")
        return 1

    gitlab = psycopg2.connect(
                 database="gitlabhq_production",
                 user="gitlab-psql",
                 host="/var/opt/gitlab/postgresql",
                 port="5432")

    args = get_args()
    if args.command == 'list':
        if (args.project):
            show_artifacts(gitlab, args.project)
        else:
            show_projects(gitlab)
    else:
        for project_path in args.projects:
            try:
                project_id = find_project(gitlab, project_path)
            except NoProjectError:
                print("No project was found with the path {}".format(project_path))
                return 1
            if args.dry_run:
                show_archive_artifacts(gitlab, project_id)
            else:
                archive_artifacts(project_id)

    return 0

if __name__=='__main__':
    sys.exit(main())
