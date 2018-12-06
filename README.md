# GitLab Artifact Tools
Set of python utilities for managing GitLab artifacts.

```
# glartifacts -h
usage: glartifacts [-h] [-d] [--verbose] [-v]  ...

GitLab Artifact Tools

optional arguments:
  -h, --help     show this help message and exit
  -d, --debug    show detailed debug information
  --verbose      show additional information
  -v, --version  show program's version number and exit

Commands:
  
    list         List build artifacts
    remove       Remove old build artifacts for a project
```

### list
Shows projects that contain build artifacts.
```
usage: glartifacts list [-h] [-s] [PROJECT [PROJECT ...]]

  PROJECT      project path whose artifacts will be listed

optional arguments:
  -h, --help   show this help message and exit
  -s, --short  use a short list format that only prints project names
```
When one or more optional project paths are provided, this command prints
detailed information about each artifact, including: pipeline id, job name, 
schedule date, build status, the ref used to build, and size.

#### Example
```
# glartifacts list $(glartifacts list -s)
Listing artifacts for awesome-people/awesome-prod #1

Pipeline Job           Scheduled At        Status  Ref               Tag? Expiring? Size     
-------- -------- ---- ------------------- ------- ----------------- ---- --------- -------- 
#54      build    #105 2018-12-06 09:54:01 success master            no   no        537.00 B 
#54      test-all #106 2018-12-06 09:54:01 success master            no   no        519.00 B 
#53      build    #103 2018-12-06 09:53:03 success test-failing-jobs no   no        537.00 B 
#53      test-all #104 2018-12-06 09:53:03 failed  test-failing-jobs no   no        519.00 B 
#52      build    #101 2018-12-06 09:51:10 success test-failing-jobs no   no        537.00 B 
#52      test-all #102 2018-12-06 09:51:10 failed  test-failing-jobs no   no        519.00 B 
#19      build    #39  2018-12-01 11:51:25 success 1.0               yes  no        537.00 B 
#19      test     #40  2018-12-01 11:51:25 success 1.0               yes  no        519.00 B 
```

### remove
Marks GitLab CI artifacts as expired using expiration strategies rather than
time. Expired artifacts will be removed when the next `Sidekiq` task is
executed.

```
usage: glartifacts remove [-h] [--dry-run]
                          [-s {LASTGOOD_JOB,LASTGOOD_PIPELINE}]
                          PROJECT [PROJECT ...]

positional arguments:
  PROJECT               paths to the projects whose artifacts should be
                        removed

optional arguments:
  -h, --help            show this help message and exit
  --dry-run             identify artifacts to be removed, but do not make any
                        changes
  -s {LASTGOOD_JOB,LASTGOOD_PIPELINE}, --strategy {LASTGOOD_JOB,LASTGOOD_PIPELINE}
                        select the expiration strategy used to identify old
                        artifacts (default: LASTGOOD_PIPELINE)
```

The `--strategy` option selects the heuristic used to identify expired
artifacts. An expiration strategy determines a point in time where artifacts are
known to be good. Artifacts before that point-in-time are removed. Tagged
artifacts are **never** removed.

The strategies available are listed below.

|Name              |Description    |
|------------------|---------------|
|LASTGOOD_PIPELINE |Keep artifacts from all jobs in the last successful pipeline. The entire pipeline must succeed to advance the expiration point-in-time.|
|LASTGOOD_JOB    |Keep artifacts from the last successful job. The point-in-time is advanced any time the job succeeds, even if its pipeline fails.|

The `--dry-run` option lists the artifacts that would be removed by the
selected strategy.

#### Example

List old artifacts for all projects
```
# glartifacts remove --dry-run $(glartifacts list -s)
Listing expired artifacts for awesome-people/awesome-prod #1

Pipeline Job          Scheduled At        Status  Ref    Tag? Expiring? Size     
-------- -------- --- ------------------- ------- ------ ---- --------- -------- 
#49      build    #95 2018-12-06 09:43:38 success master no   no        537.00 B 
#49      test-all #96 2018-12-06 09:43:38 success master no   no        519.00 B
```

Mark old artifacts as expired
```
# glartifacts remove awesomesoft/awesome-core
```

List the current state of the project's artifacts. Artifacts are removed
from this list by `Sidekiq`.
```
# glartifacts list awesome-people/awesome-prod
Listing artifacts for awesome-people/awesome-prod #1

Pipeline Job           Scheduled At        Status  Ref               Tag? Expiring? Size     
-------- -------- ---- ------------------- ------- ----------------- ---- --------- -------- 
#54      build    #105 2018-12-06 09:54:01 success master            no   no        537.00 B 
#54      test-all #106 2018-12-06 09:54:01 success master            no   no        519.00 B 
#49      test-all #96  2018-12-06 09:43:38 success master            no   yes       519.00 B 
#49      build    #95  2018-12-06 09:43:38 success master            no   yes       537.00 B 
#19      build    #39  2018-12-01 11:51:25 success 1.0               yes  no        537.00 B 
#19      test     #40  2018-12-01 11:51:25 success 1.0               yes  no        519.00 B 
```

## Configuration using glartifacts.conf
Glartifacts requires access to the GitLab database and Gitaly server. The 
default connection settings are based on an omnibus install, but can be
modified for custom deployments via settings in glartifacts.conf. You can
also override any of the configured settings using environment variables.

The table below lists the available configuration options:

|Section   |Option   |ENV var   |Default |
|----------|---------|----------|--------|
|postgres |dbname |`GLARTIFACTS_DBNAME` |`gitlabhq_production` |
|postgres |user |`GLARTIFACTS_DBUSER` |`gitlab` |
|postgres |host |`GLARTIFACTS_DBHOST` |`/var/opt/gitlab/postgresql` |
|postgres |port |`GLARTIFACTS_DBPORT` |`5432` |
|gitaly |address |`GLARTIFACTS_GITALYADDR` |`unix:/var/opt/gitlab/gitaly/gitaly.socket` |

The following paths are searched for the glartifacts.conf. Settings are merged
for each conf file found: `Defaults` > `System Settings` > `User Settings`.
```
$HOME/.config/glartifacts/glartifacts.conf
/etc/glartifacts/glartifacts.conf
```
