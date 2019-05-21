import hashlib


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
