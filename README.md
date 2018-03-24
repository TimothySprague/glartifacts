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

**Example**
```
# glartifacts list $(glartifacts list -s)
Listing artifacts for awesomesoft/awesome-core 

Pipeline Job       Scheduled At        Built At            Status  Tag? Expiring? Size     
-------- --------- ------------------- ------------------- ------- ---- --------- -------- 
#13      awesomify 2018-03-18 11:58:26 2018-03-19 10:27:47 success no   no        2.73 KiB 
#13      awesomify 2018-03-18 11:58:26 2018-03-18 11:58:26 success no   no        2.73 KiB 
#11      awesomify 2018-03-17 09:55:40 2018-03-19 10:28:02 success no   no        2.73 KiB 
#9       awesomify 2018-03-15 10:40:58 2018-03-19 10:28:25 success no   no        2.73 KiB 
#8       awesomify 2018-03-14 10:14:48 2018-03-19 10:29:45 success no   no        2.73 KiB 
#6       awesomify 2018-02-23 04:02:01 2018-03-19 10:28:15 success no   no        2.75 KiB 
```

### archive
Marks GitLab CI artifacts as expired using expiration strategies rather than
time. Expired artifacts will be removed when the next Sidekiq task is
executed.

```
usage: glartifacts [-h] [-d] [--verbose] [-v]  ...

GitLab Artifact Archiver

optional arguments:
  -h, --help     show this help message and exit
  -d, --debug    show detailed debug information
  --verbose      show additional information
  -v, --version  show program's version number and exit

Commands:

    list         List build artifacts
    archive      Archive build artifacts for a project
```
The `--strategy` option selects the heuristic used to identify expired
artifacts. An archive strategy determines a point in time where artifacts are
known to be good. Artifacts before that point-in-time are removed. Tagged
artifacts are never removed.

The strategies available are listed below.

|Name              |Description    |
|------------------|---------------|
|LASTGOOD_PIPELINE |Keep artifacts from all jobs in the last successful pipeline. The entire pipeline must succeed to advance the expiration point-in-time.|
|LASTGOOD_BUILD    |Keep artifacts from the last successful job. The point-in-time is advanced any time the job succeeds, even if its pipeline fails.|

The `--dry-run` option lists the artifacts that would be removed by the
selected strategy.
