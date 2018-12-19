# v2.1.2
* Fixed a bug in namespace lookup when a namespace name was reused at multiple paths

# v2.1.1
* Add documentation hosted by readthedocs.io
* First version available in PyPI

# v2.1.0
* Add `--all` option to `list` and `remove` that runs the command on all projects
* Add `--exclude` option to `list` and `remove` that excludes projects by path
* Add artifact state column to improve the `list` and `remove --dry-run` output.
* Fixed bugs caused by typos, missing imports, etc.

# v2.0.0
* Rename the archive command to remove. It's a more accurate verb.
* Make LASTGOOD_PIPELINE the default strategy
* Parse the GitLab CI configuration file to ensure artifacts are removed when
a job is renamed or removed.
* Update psycopg2 package version for Python 3.7 support

# v1.2.2
* Fix `glartifacts list` when running on old GitLab installations

# v1.2.1
* Rename `LASTGOOD_BUILD` to `LASTGOOD_JOB`. This is consistent with GitLab's modern
vocabulary (jobs, not builds)
* Simplify the `project_id` filter in the artifact archive queries
* Resolve project paths correctly when there are nested parent groups
* Account job artifacts where `job_artifact.size` is null

# v1.2
Use Gitaly to extend project metdata

* Connect to Gitaly to resolve additional project information
* Archive artifacts from deleted branches
* Enable configuration via conf files and environment variables for database and Gitaly connection settings 

# v1.1
Deployment Testing Cleanup

* Use project path, not name for looking up projects (paths are terminal safe, names are not)
* Include more IDs when listing jobs (project id, pipeline id, job id)
* Display the strategy in-use during `archive --dry-run`. Show the default values in the command help.
* Ensure artifacts are kept per-branch. Previously a push to a feature branch might archive the latest `master` artifacts.


# v1.0
Initial version of GitLab Artifacts Tools

* Added list command that prints projects with artifacts
* Added archive command that marks expired artifacts as expired
* Implemented two archive strategies `LASTGOOD_PIPELINE` and `LASTGOOD_BUILD`
