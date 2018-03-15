import argparse
import os
import psycopg2
import psycopg2.extras
import pwd
import sys

from .errors import GitlabArtifactsError, NoProjectError
from .projects import find_project, list_projects, list_artifacts
from .archive import list_archive_artifacts, archive_artifacts
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
                    print("No project was found with the path {}".format(project_path))
                    return 1
            setattr(args,self.dest, projects)
    return ResolveProject

def get_args(db):
    parser = argparse.ArgumentParser(description='GitLab Artifact Archiver')
    commands = parser.add_subparsers(dest='command', metavar='COMMAND')

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

    return 0

def show_artifacts(db, project_paths, artifacts, reason):
    projects = ", ".join(sorted(project_paths))
    if not len(artifacts):
        raise GitlabArtifactsError("No artifacts were found for "+projects)

    print("Listing", reason, "for", projects, "\n")
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
        dict(key=lambda r:(r[0], r[1])),
        dict(key=lambda r:(r[2]), reverse=True)
        ])

    return 0

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

    args = get_args(gitlab)
    if args.command == 'list':
        if (args.projects):
            artifacts = list_artifacts(gitlab, args.projects.keys())
            show_artifacts(gitlab, args.projects.values(), artifacts, "all artifacts")
        else:
            show_projects(gitlab)
    else:
        if args.dry_run:
            artifacts = list_archive_artifacts(gitlab, args.projects.keys())
            show_artifacts(gitlab, args.projects.values(), artifacts, "old artifacts")
        else:
            archive_artifacts(gitlab, args.projects.keys())
            gitlab.commit()

    return 0

if __name__=='__main__':
    try:
        main()
    except:
        print(sys.exc_info()[1])
        sys.exit(1)
    
    sys.exit(0)
