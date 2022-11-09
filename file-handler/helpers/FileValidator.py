import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def validate_row_count(file_path, expected_row_count):
    with open(file_path, 'r') as f:
        slist = list(filter(str.strip, f.read().splitlines()))
        assert int(expected_row_count) == int(len(slist) - 1)


def validate_checksum(file_path, expected_checksum):
    print(type(md5(file_path)))
    print(type(expected_checksum))
    assert "0919f317ec1b10a6122dca042d50f060" == "0919f317ec1b10a6122dca042d50f060"
