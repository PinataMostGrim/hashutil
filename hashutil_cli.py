#!/usr/bin/env python3
""" """

import argparse
import sys

from hashutil import core
from pathlib import Path


def main():
    args = prase_args(sys.argv[1:])

    if args.list:
        core.print_available_algorithms()
        sys.exit(0)

    if args.file:
        input_type = 'file'
    else:
        input_type = 'string'

    print(f'\nCalculating {args.algorithm} for {input_type}: {args.input}')

    if args.file:
        file_path = Path(args.input)

        if not file_path.exists():
            print('Cannot find file \'{0}\''.format(file_path))
            sys.exit(1)

        hash = core.get_file_hash(file_path, args.algorithm)

    else:
        hash = core.get_string_hash(args.input, args.algorithm)

    print(f'\n{args.algorithm: <10}: {hash}')

    if (args.compare):
        prefix = 'compare'
        print(f'{prefix: <10}: {args.compare}')

        if hash == args.compare:
            print('\nMatches!')
        else:
            print('\nDoes NOT match!')

    sys.exit(0)


def prase_args(argv):

    # Note: We use two parsers here in order to support the optional '--list' flag
    list_parser = argparse.ArgumentParser(add_help=False)
    list_parser.add_argument('--list', action='store_true', help='list help')

    hash_parser = argparse.ArgumentParser(
        prog='hashutil_cli.py',
        description='CLI application that calculates hash sums',
        parents=[list_parser])

    hash_parser.add_argument('algorithm', type=str, help='algorithm help')
    hash_parser.add_argument('input', type=str, help='input help')
    hash_parser.add_argument('--file', '-f', action='store_true', help='file help')
    hash_parser.add_argument('--compare', '-c', type=str, help='compare help')

    args, extra_args = list_parser.parse_known_args()

    if len(argv) == 0:
        hash_parser.print_help()
        sys.exit(0)

    if len(extra_args) > 0:
        args = hash_parser.parse_args(extra_args, namespace=args)

    return args


if __name__ == '__main__':
    main()
