import hashlib
import argparse
import sys

from argparse import Namespace
from pathlib import Path


class Command:
    def execute(self, options: Namespace):
        pass


class MD5(Command):
    '''Output a file or string's md5 checksum.'''
    def execute(self, options):
        file_path = Path(options.file)

        if not options.string and not file_path.is_file():
            print('Cannot find file \'{0}\''.format(file_path))
            return

        if options.string:
            print('\nCalculating MD5 for \'{0}\''.format(options.file))
            checksum = get_string_md5(options.file)

        else:
            print('\nCalculating MD5 for \'{0}\''.format(file_path))
            checksum = get_file_md5(file_path)

        print('md5    : {0}'.format(checksum))

        if options.compare:
            print('compare: {0}'.format(options.compare))

            if checksum == options.compare:
                print('\nMatches!')
            else:
                print('\nDoes NOT match!')

    @staticmethod
    def configure(subparser):
        subparser.add_argument('file', type=str, help='The file\'s path')
        subparser.add_argument('-s', '--string', action='store_true', help='Treat the file argument as a string when calculating the MD5 hash')
        subparser.add_argument('-c', '--compare', type=str, help='Compare the calculated MD5 hash with a string')


class SHA256(Command):
    '''Output a file or string's SHA256 checksum.'''
    def execute(self, options):
        file_path = Path(options.file)

        if not options.string and not file_path.is_file():
            print('Cannot find file \'{0}\''.format(file_path))
            return

        if options.string:
            print('\nCalculating SHA256 for \'{0}\''.format(options.file))
            checksum = get_string_sha256(options.file)

        else:
            print('\nCalculating SHA256 for \'{0}\'\n'.format(file_path))
            checksum = get_file_sha256(file_path)

        print('sha256 : {0}'.format(checksum))

        if options.compare:
            print('compare: {0}'.format(options.compare))

            if checksum == options.compare:
                print('\nMatches!')
            else:
                print('\nDoes NOT match!')

    @staticmethod
    def configure(subparser):
        subparser.add_argument('file', type=str, help='The file\'s path')
        subparser.add_argument('-s', '--string', action='store_true', help='Treat the file argument as a string when calculating the hash')
        subparser.add_argument('-c', '--compare', type=str, help='Compare the calculated hash with a string')


def get_file_md5(file_path):
    '''Returns:
        The MD5 hash of the file as a string.
    '''
    md5Hash = hashlib.md5()
    with open(file_path, "rb") as f:
        # Note: Allow handling of extremely large files by passing in chunks at
        # a time. This ensures we do not run out of memory.
        for chunk in iter(lambda: f.read(4096), b""):
            md5Hash.update(chunk)
    return md5Hash.hexdigest()


def get_string_md5(string: str):
    '''Returns:
        The MD5 hash of the string as a string.
    '''
    md5Hash = hashlib.md5()
    md5Hash.update(string.encode('utf-8'))
    return md5Hash.hexdigest()


def get_file_sha256(file_path):
    '''Returns:
        The SHA256 hash of the file as a string.
    '''
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Note: Allow handling of extremely large files by passing in chunks at
        # a time. This ensures we do not run out of memory.
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


def get_string_sha256(string: str):
    '''Returns:
        The SHA256 hash of the string as a string.
    '''
    sha256_hash = hashlib.sha256()
    sha256_hash.update(string.encode('utf-8'))
    return sha256_hash.hexdigest()


def main():
    options = get_options(sys.argv[1:])
    command = options.command()
    command.execute(options)


def get_options(argv):
    parser = argparse.ArgumentParser(
        prog='checksum',
        description='CLI utility for reporting file checksums')
    subparsers = parser.add_subparsers(title='Commands')

    md5_parser = subparsers.add_parser('md5', help='Reports file md5 checksum')
    MD5.configure(md5_parser)
    md5_parser.set_defaults(command=MD5)

    sha256_parser = subparsers.add_parser('sha256', help='Reports file sha256 checksum')
    SHA256.configure(sha256_parser)
    sha256_parser.set_defaults(command=SHA256)

    options = parser.parse_args(argv)
    if 'command' not in options:
        parser.print_help()
        sys.exit(2)

    return options


if __name__ == '__main__':
    main()