"""Calculates hash digests for strings and files using various algorithms."""

import hashlib
from pathlib import Path


_SUPPORTED_ALGORITHMS = {
    'blake2b',
    'blake2s',
    'md5',
    'sha1',
    'sha224',
    'sha256',
    'sha384',
    'sha3_224',
    'sha3_256',
    'sha3_384',
    'sha3_512',
    'sha512'
}


class HashutilError(Exception):
    """Base error for core HashUtility module exceptions."""
    pass


class InvalidAlgorithmError(HashutilError):
    """An error occured because an invalid algorithm was requested."""
    pass


def get_available_algorithms():
    """Fetches a sorted set of supported algorithms.

    Returns:
      A set of supported algorithms.
    """
    return sorted(_SUPPORTED_ALGORITHMS.copy())
    # return set(sorted(hashlib.algorithms_available))
    # return set(sorted(hashlib.algorithms_guaranteed))


def get_string_hash(string: str, algorithm_name: str):
    """Calculates the hash digest of a string.

    Args:
      string: str: The string to digest.
      algorithm_name: str: The name of the algorithm to hash the string with.

    Returns:
      A hash digest in string form.
    """

    hash_algorithm = _get_algorithm(algorithm_name)
    hash_algorithm.update(string.encode('utf-8'))

    return hash_algorithm.hexdigest()


def get_file_hash(file_path: Path, algorithm_name: str):
    """Calculates the hash digest of a file.

    Args:
      file_path: Path: The file to digest.
      algorithm_name: str: The name of the algorithm to hash the file with.

    Returns:
      A hash digest in string form.
    """

    hash_algorithm = _get_algorithm(algorithm_name)

    with open(file_path, 'rb') as f:
        # Note: Allow handling of extremely large files by passing in chunks at
        # a time. This ensures we do not run out of memory.
        for chunk in iter(lambda: f.read(4096), b""):
            hash_algorithm.update(chunk)

    return hash_algorithm.hexdigest()


def _get_algorithm(algorithm: str):
    """Fetches a constructed hash object from hashlib.

    Args:
      algorithm: str: The name of the hash object to construct.

    Returns:
      A constructed hash object.
    """
    if algorithm not in get_available_algorithms():
        raise InvalidAlgorithmError(f'{algorithm} is not a valid algorithm')

    target_constructor = getattr(hashlib, algorithm)
    return target_constructor()
