import argparse
import logging
import sys

from fds.logger import Logger

# Argument parser stuff
from fds.run import Run
from fds.utils import str2bool

arg_parser = argparse.ArgumentParser(description="One command for all your git and dvc needs",
                                     prog="fds")
# Command choice
command_subparser = arg_parser.add_subparsers(dest="command", help="command (refer commands section in documentation)")

# init
parser_init = command_subparser.add_parser('init', help='initialize a git and dvc repository')

# status
parser_status = command_subparser.add_parser('status', help='get status of your git and dvc repository')

# add
parser_add = command_subparser.add_parser('add', help='add files/folders to git and dvc repository')
parser_add.add_argument('add_command', help="choose what to add using . will add everything")

# COMMIT
parser_commit = command_subparser.add_parser('commit', help='commits added changes to git and dvc repository')
parser_commit.add_argument('-y', "--yes",
                           help="Don't ask for confirmation for committing file changes",
                           action="store_true", default=False)
parser_commit.add_argument('message', help="commit message")

# push
parser_push = command_subparser.add_parser(
    'push',
    help='push commits to remote git and dvc repository'
)
parser_push.add_argument('-r', '--remote', help="fds remote name", default="origin")

# save
parser_save = command_subparser.add_parser(
    'save',
    help='saves all project files to a new version and pushes them to your remote'
)
parser_save.add_argument('message', help="save message")
parser_save.add_argument('-r', '--remote', help="fds remote name", default="origin")

# argument for log level
arg_parser.add_argument("-v", "--verbose", help="set log level to DEBUG",
                        type=str2bool, nargs='?', const=True, default=False)


def parse_args(args):
    arguments = vars(arg_parser.parse_args(args=args or ["--help"]))
    return arguments


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed_args = parse_args(args=args)
    if bool(parsed_args["verbose"]):
        Logger.set_logging_level(logging.DEBUG)
    result = Run(arguments=parsed_args).execute()
    sys.exit(result)


if __name__ == "__main__":
    main()
