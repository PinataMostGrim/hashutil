import hashlib
import argparse
import sys

from argparse import Namespace
from pathlib import Path


class Command:
    def execute(self, options: Namespace):
        pass


class MD5(Command):
    '''
    Output a file or string's md5 checksum.
    '''
    def execute(self, options):
        file_path = Path(options.file)

        if not file_path.is_file():
            print('Cannot find file \'{0}\''.format(file_path))
            return

        print('Calculating MD5 for \'{0}\''.format(file_path))
        checksum = get_file_md5(file_path)
        print('md5: {0}\n'.format(checksum))

    @staticmethod
    def configure(subparser):
        subparser.add_argument('file', type=str, help='The file\'s path')
        # a flag that treats the file as a string
        # a flag that passes in a string with a hash to compare


def get_file_md5(file_path):
    '''Returns:
        The MD5 hash of the file as a string
    '''
    md5Hash = hashlib.md5()
    with open(file_path, "rb") as f:
        # Note: Allow handling of extremely large files
        # by passing in chunks at a time. This ensures we
        # do not run out of memory.
        for chunk in iter(lambda: f.read(4096), b""):
            md5Hash.update(chunk)
    return md5Hash.hexdigest()


def main():
    options = get_options(sys.argv[1:])
    command = options.command()
    command.execute(options)


def get_options(argv):
    parser = argparse.ArgumentParser(
        prog='checksum',
        description='CLI utility for reporting file checksums')
    subparsers = parser.add_subparsers(title='Commands')

    md5Parser = subparsers.add_parser('md5', help='Reports file md5 checksum')
    MD5.configure(md5Parser)
    md5Parser.set_defaults(command=MD5)

    options = parser.parse_args(argv)
    if 'command' not in options:
        parser.print_help()
        sys.exit(2)

    return options


if __name__ == '__main__':
    main()
