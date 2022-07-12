# NF-Core Workflows

The information on how to obtain input data for each individual workflow can be found in the corresponding directories.

## Downloading the igenome data

Many nf-core workflows use igenome data. Sometimes these may want to be downloaded beforehand instead of nextflow downloading them during the workflow execution.
The file `igenome_files.txt` provides a list of all the required igenome files that can usually be found in the `conf/igenomes.conf` file of the respective workflow. Completeness of the list in `igenome_files.txt` is not guaranteed.

The list can be used to manually download all the files, but there is also a python script `createIgenomeDownloadScript.py` provided which lets you create a bash script which then can be copied anywhere e.g. a kubernetes pod to download the data there.

The command

    python3 createIgenomeDownloadScript.py -r eu-central-1 /igenome/dir

creates a bash script that downloads all the igenome data and stores it in `/igenome/dir`.

Before using the bash script you need AWS access as well as `awscli` installed and configured wherever you want to download the igenome data.