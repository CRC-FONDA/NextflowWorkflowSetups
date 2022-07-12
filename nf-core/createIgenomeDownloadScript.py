#!/usr/bin/env python3.9.7

import getopt
import sys

REGION_DEFAULT: str = None
BASH_FILENAME_DEFAULT: str = "download_igenomes_aws.sh"

USAGE: str = f"Usage: python {sys.argv[0]} [--help] | [-r <aws-region>] | [-b <bash-filename>] stage_dir\nby default:\n\taws_region:\t{REGION_DEFAULT}\n\tbash-filename:\t{BASH_FILENAME_DEFAULT}"
VERSION = f"{sys.argv[0]} version 1.0.0"

def parse(args: list[str]) -> tuple[str, list[int]]:
    options, arguments = getopt.getopt(
        args,
        'vhr:b:',
        ["version", "help", "aws-region", "bash-filename"]
    )
    aws_region = REGION_DEFAULT
    bash_filename = BASH_FILENAME_DEFAULT
    for o, a in options:
        if o in ("-h", "--help"):
            print(USAGE)
            sys.exit()
        if o in ("-v", "--version"):
            print(VERSION)
            sys.exit()
        if o in ("-r", "--region"):
            aws_region = a
    if not arguments or len(arguments) > 1:
        raise SystemExit(USAGE)
    stage_dir: str = arguments[0]
    if stage_dir[-1] != '/':
        stage_dir += '/'
    return aws_region, bash_filename, stage_dir

def createBashScript(aws_region: str, bash_filename: str, stage_dir: str) -> None:
    with open(f"igenome_files.txt", 'r') as f:
        lines: list[str] = f.readlines()
    aws_download_commands: list[str] = []
    command_start = "aws s3 --no-sign-request"
    if aws_region:
        command_start += f" --region {aws_region}"
    for s3_file in lines:
        if s3_file[-1] == '\n':
            s3_file = s3_file[:-1]
        cmd: str = "sync" if s3_file[-1] == '/' else "cp"
        save_file: str = s3_file.replace("s3://ngi-igenomes/igenomes", stage_dir)
        aws_download_commands.append(
            f"{command_start} {cmd} {s3_file} {save_file}"
        )
    with open(bash_filename, 'w') as f:
        for command in aws_download_commands:
            f.write(command + "\n")

def main() -> None:
    args = sys.argv[1:]
    if not args:
        raise SystemExit(USAGE)
    aws_region, bash_filename, stage_dir = parse(args)
    try:
        createBashScript(aws_region, bash_filename, stage_dir)
    except:
        raise SystemExit(USAGE)

if __name__ == "__main__":
    main()