# GitLab Artifact Tools
Set of python utilities for managing GitLab artifacts.

```
# glartifacts -h
usage: glartifacts [-h] [-d] [--verbose] [-v]  ...

GitLab Artifact Archiver

optional arguments:
  -h, --help     show this help message and exit
  -d, --debug    show detailed debug information
  --verbose      show additional information
  -v, --version  show program's version number and exit

Commands:
  
    list         list build artifacts
    archive      archive build artifacts for a project
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
When one or more optional
project paths are provided, this command prints detailed information about
each artifact, including: schedule date, build date, tagged build, and size.

### archive
Marks GitLab CI artifacts as expired using expiration strategies rather than
time. Expired artifacts will be removed when the next Sidekiq task is
executed.

```
usage: glartifacts archive [-h] [--dry-run]
                           [-s {LASTGOOD_BUILD,LASTGOOD_PIPELINE}]
                           PROJECT [PROJECT ...]

  PROJECT               paths to the projects to archive

optional arguments:
  -h, --help            show this help message and exit
  --dry-run             identify artifacts to be archived, but do not make any
                        changes
  -s , --strategy 	select the archive strategy used to identify old
                        artifacts
```
The `--strategy` option selects the heuristic used to identify expired
artifacts. An archive strategy determines a point in time where artifacts are
known to be good. Artifacts before that point-in-time are removed. Tagged
artifacts are never removed.

The strategies available are listed below.

|Name			|Description	|
|-----------------------|---------------|
|LASTGOOD_PIPELINE   	|Keep artifacts from all jobs in the last successful|
|			|pipeline. The entire pipeline must succeed to advance|
|			|the expiration point-in-time.|
|LASTGOOD_BUILD		|Keep artifacts from the last successful job. The|
|			|point-in-time is advanced any time the job succeeds, |
|			|even if its pipeline fails. |

The `--dry-run` option lists the artifacts that would be removed by the
selected strategy.
