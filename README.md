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
usage: glartifacts list [-h] [-s]
                        [--strategy {LASTGOOD_JOB,LASTGOOD_PIPELINE}]
                        [PROJECT [PROJECT ...]]

positional arguments:
  PROJECT               project path whose artifacts will be listed

optional arguments:
  -h, --help            show this help message and exit
  -s, --short           use a short list format that only prints project names
  --strategy {LASTGOOD_JOB,LASTGOOD_PIPELINE}
                        select the expiration strategy used to identify old
                        artifacts (default: LASTGOOD_PIPELINE)
```

When one or more optional project paths are provided, this command prints
detailed information about each artifact, including: project id, pipeline id,
job name, scheduled date, the ref that was built, build status, artifact state,
and size.

#### Example

List artifacts for all projects:
```
# glartifacts list $(glartifacts list -s)

Project Pipeline Job           Ref                 Scheduled At        Status  Artifacts Size     
------- -------- -------- ---- ------------------- ------------------- ------- --------- -------- 
#1      #70      test-all #147 master              2018-12-08 13:48:54 success lastgood  519.00 B 
#1      #70      build    #141 master              2018-12-08 13:48:54 success lastgood  537.00 B 
#1      #69      build    #137 fix-the-build       2018-12-08 12:56:59 success new       537.00 B 
#1      #69      test-all #138 fix-the-build       2018-12-08 12:56:59 failed  new       519.00 B 
#1      #68      build    #135 15-add-more-awesome 2018-12-08 12:56:37 success new       537.00 B 
#1      #68      test-all #136 15-add-more-awesome 2018-12-08 12:56:37 failed  new       519.00 B 
#1      #67      build    #133 master              2018-12-08 12:56:14 success old       537.00 B 
#1      #67      test-all #134 master              2018-12-08 12:56:14 failed  old       519.00 B 
#1      #66      test-all #132 master              2018-12-08 02:06:29 success old       519.00 B 
#1      #66      build    #129 master              2018-12-08 02:06:29 success old       537.00 B 
#1      #59      test-all #116 test-failing-jobs   2018-12-08 01:19:12 failed  orphaned  519.00 B 
#1      #56      test-all #110 test-failing-jobs   2018-12-07 12:00:43 failed  orphaned  519.00 B 
#1      #53      test-all #104 test-failing-jobs   2018-12-06 09:53:03 failed  orphaned  519.00 B 
#1      #52      test-all #102 test-failing-jobs   2018-12-06 09:51:10 failed  orphaned  519.00 B 
#1      #19      build    #39  1.0                 2018-12-01 11:51:25 success tagged    537.00 B 
#1      #19      test     #40  1.0                 2018-12-01 11:51:25 success tagged    519.00 B 
```

### remove
Marks GitLab CI artifacts as expired using expiration strategies rather than
time. Expired artifacts will be removed when the next `Sidekiq` task is
executed.

```
usage: glartifacts remove [-h] [--dry-run]
                          [--strategy {LASTGOOD_JOB,LASTGOOD_PIPELINE}]
                          PROJECT [PROJECT ...]

positional arguments:
  PROJECT               paths to the projects whose artifacts should be
                        removed

optional arguments:
  -h, --help            show this help message and exit
  --dry-run             identify artifacts to be removed, but do not make any
                        changes
  --strategy {LASTGOOD_JOB,LASTGOOD_PIPELINE}
                        select the expiration strategy used to identify old
                        artifacts (default: LASTGOOD_PIPELINE)
```

#### Example

List old or orphaned artifacts for all projects:
```
# glartifacts remove --dry-run $(glartifacts list -s)
Listing old or orphaned artifacts for awesome-people/awesome-prod #1 using LASTGOOD_PIPELINE strategy

Project Pipeline Job           Ref               Scheduled At        Status  Artifacts Size     
------- -------- -------- ---- ----------------- ------------------- ------- --------- -------- 
#1      #67      build    #133 master            2018-12-08 12:56:14 success old       537.00 B 
#1      #67      test-all #134 master            2018-12-08 12:56:14 failed  old       519.00 B 
#1      #66      test-all #132 master            2018-12-08 02:06:29 success old       519.00 B 
#1      #66      build    #129 master            2018-12-08 02:06:29 success old       537.00 B 
#1      #59      test-all #116 test-failing-jobs 2018-12-08 01:19:12 failed  orphaned  519.00 B 
#1      #56      test-all #110 test-failing-jobs 2018-12-07 12:00:43 failed  orphaned  519.00 B 
#1      #53      test-all #104 test-failing-jobs 2018-12-06 09:53:03 failed  orphaned  519.00 B 
#1      #52      test-all #102 test-failing-jobs 2018-12-06 09:51:10 failed  orphaned  519.00 B 
```

Mark old or orphaned artifacts as expired:
```
# glartifacts remove awesomesoft/awesome-core
```

List the current state of the project's artifacts. Expiring artifacts are removed
from this list by `Sidekiq`.
```
# glartifacts list awesome-people/awesome-prod
Listing artifacts for awesome-people/awesome-prod #1

Project Pipeline Job           Ref                 Scheduled At        Status  Artifacts Size     
------- -------- -------- ---- ------------------- ------------------- ------- --------- -------- 
#1      #70      test-all #147 master              2018-12-08 13:48:54 success lastgood  519.00 B 
#1      #70      build    #141 master              2018-12-08 13:48:54 success lastgood  537.00 B 
#1      #69      build    #137 fix-the-build       2018-12-08 12:56:59 success new       537.00 B 
#1      #69      test-all #138 fix-the-build       2018-12-08 12:56:59 failed  new       519.00 B 
#1      #68      build    #135 15-add-more-awesome 2018-12-08 12:56:37 success new       537.00 B 
#1      #68      test-all #136 15-add-more-awesome 2018-12-08 12:56:37 failed  new       519.00 B 
#1      #67      build    #133 master              2018-12-08 12:56:14 success expiring  537.00 B 
#1      #67      test-all #134 master              2018-12-08 12:56:14 failed  expiring  519.00 B 
#1      #66      test-all #132 master              2018-12-08 02:06:29 success expiring  519.00 B 
#1      #66      build    #129 master              2018-12-08 02:06:29 success expiring  537.00 B 
#1      #59      test-all #116 test-failing-jobs   2018-12-08 01:19:12 failed  expiring  519.00 B 
#1      #56      test-all #110 test-failing-jobs   2018-12-07 12:00:43 failed  expiring  519.00 B 
#1      #53      test-all #104 test-failing-jobs   2018-12-06 09:53:03 failed  expiring  519.00 B 
#1      #52      test-all #102 test-failing-jobs   2018-12-06 09:51:10 failed  expiring  519.00 B 
#1      #19      build    #39  1.0                 2018-12-01 11:51:25 success tagged    537.00 B 
#1      #19      test     #40  1.0                 2018-12-01 11:51:25 success tagged    519.00 B 
```

## Artifact States
Artifacts for a job can be in one of the following states.

|State |Description|
|------|-----------|
|`tagged`|The artifacts are from a tagged build. Tagged artifacts are never removed.|
|`expiring`|The artifacts have an expiration date set, and will be removed by Sidekiq.|
|`orphaned`|The job (by name) or branch associated with these artifacts has been removed. These artifacts are considered old.|
|`lastgood`|Artifacts from the job or pipeline identified as the lastgood point-in-time for the given ref.|
|`old`|Artifacts that are older than the lastgood point-in-time.|
|`new`|Artifacts that are newer than the lastgood point-in-time.|

The `remove` command removes artifacts in the `old` or `orphaned` state. 

## Archive Expiration Strategies
The `--strategy` option of the `list` and `remove` commands selects the heuristic
used to identify old artifacts. An expiration strategy determines a 
point in time where artifacts are known to be good. Artifacts before that 
point-in-time are old and will be removed.

Tagged artifacts are **never** removed.

The strategies available are listed below.

|Name              |Description    |
|------------------|---------------|
|LASTGOOD_PIPELINE |Keep artifacts from all jobs in the last successful pipeline. The entire pipeline must succeed to advance the expiration point-in-time.|
|LASTGOOD_JOB    |Keep artifacts from the last successful job. The point-in-time is advanced any time the job succeeds, even if its pipeline fails.|


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
