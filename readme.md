## Description
**hashutil** is a command line application that calculates hash digests for strings and files using various algorithms. It supports most of the hash algorithms included by the `hashlib` package and requires Python 3.6+.

## Usage
```
usage: hashutil_cli.py [-h] [--list] [--file] [--compare COMPARE | --quiet]
                       algorithm input

Calculates hash digests for strings and files using different algorithms.

positional arguments:
  algorithm             Algorithm to use when calculating the input argument's
                        hash
  input                 String or file to hash (default: string)

optional arguments:
  -h, --help            show this help message and exit
  --list                Display a list of all supported hash algorithms
  --file, -f            Hash the file specified by the input argument
  --compare COMPARE, -c COMPARE
                        Run a comparison between this string and the input
                        argument's hash
  --quiet, -q           Output ONLY the calculated hash.
```
