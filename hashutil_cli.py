#!/usr/bin/env python3

"""Command line interface script for interacting with the hashutil module.
Calculates hash digests for strings and files using various algorithms.

Use the 'hashutil_cli -h' command for usage instructions.
"""

import argparse
import sys

from hashutil import core
from pathlib import Path


def main():
    """Executes parsed arguments and prints output."""
    args = prase_args(sys.argv[1:])

    if args.list:
        print(', '.join(core.get_available_algorithms()))
        sys.exit(0)

    if args.file:
        input_type = 'FILE'
    else:
        input_type = 'STRING'

    if not args.quiet:
        print(f'\nCalculating {args.algorithm} for {input_type}: {args.input}')

    if args.file:
        file_path = Path(args.input)

        if not file_path.exists():
            print('Cannot find file \'{0}\''.format(file_path))
            sys.exit(1)

        hash = core.get_file_hash(file_path, args.algorithm)

    else:
        hash = core.get_string_hash(args.input, args.algorithm)

    if args.quiet:
        print(hash)
        return
    else:
        print(f'\n{args.algorithm: <10}: {hash}')

    if (args.compare):
        prefix = 'compare'
        print(f'{prefix: <10}: {args.compare}')

        if hash == args.compare:
            print('\nHashes match!')
        else:
            print('\nHashes DO NOT match!')


def prase_args(argv: list):
    """Builds a Namespace object with parsed arguments.

    Args:
      argv: List: List of arguments to parse.

    Returns:
      A Namespace object with parsed arguments.
    """

    # Note: We use two parsers here in order to support the optional '--list' argument.
    list_parser = argparse.ArgumentParser(add_help=False)
    list_parser.add_argument('--list', action='store_true', help='list help')

    hash_parser = argparse.ArgumentParser(
        prog='hashutil_cli.py',
        description='CLI application that calculates hash sums',
        parents=[list_parser])

    hash_parser.add_argument('algorithm', type=str, help='algorithm help')
    hash_parser.add_argument('input', type=str, help='input help')
    hash_parser.add_argument('--file', '-f', action='store_true', help='file help')

    hash_group = hash_parser.add_mutually_exclusive_group()
    hash_group.add_argument('--compare', '-c', type=str, help='compare help')
    hash_group.add_argument('--quiet', '-q', action="store_true", help='quiet help')

    args, extra_args = list_parser.parse_known_args()

    if len(argv) == 0:
        hash_parser.print_help()
        sys.exit(0)

    if len(extra_args) > 0:
        args = hash_parser.parse_args(extra_args, namespace=args)

    return args


if __name__ == '__main__':
    main()
