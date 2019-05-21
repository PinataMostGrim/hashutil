import hashlib
from pathlib import Path


SUPPORTED_ALGORITHMS = [
    'md5',
    'sha256',
    'sha512'
]


class HashutilError(Exception):
    """ """
    pass


class InvalidAlgorithmError(HashutilError):
    """ """
    pass


def print_available_algorithms():
    available = _get_available_algorithms()
    print(', '.join(available))


def get_string_hash(string: str, algorithm_name: str):
    hash_algorithm = _get_algorithm(algorithm_name)
    hash_algorithm.update(string.encode('utf-8'))

    return hash_algorithm.hexdigest()


def get_file_hash(file_path: Path, algorithm_name: str):
    hash_algorithm = _get_algorithm(algorithm_name)

    with open(file_path, 'rb') as f:
        # Note: Allow handling of extremely large files by passing in chunks at
        # a time. This ensures we do not run out of memory.
        for chunk in iter(lambda: f.read(4096), b""):
            hash_algorithm.update(chunk)

    return hash_algorithm.hexdigest()


def _get_algorithm(algorithm: str):
    available = _get_available_algorithms()

    if algorithm not in available:
        raise InvalidAlgorithmError(f'{algorithm} is not a valid algorithm')

    target_constructor = getattr(hashlib, algorithm)
    return target_constructor()


def _get_available_algorithms():
    return SUPPORTED_ALGORITHMS.copy()
    # return hashlib.algorithms_available
    # return hashlib.algorithms_guaranteed
