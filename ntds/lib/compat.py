# This file is part of ntdsxtract.

from binascii import hexlify


def as_bytes(value, encoding="latin-1"):
    if value is None:
        return None
    if isinstance(value, bytes):
        return value
    if isinstance(value, bytearray):
        return bytes(value)
    return str(value).encode(encoding)


def as_text(value, encoding="latin-1"):
    if value is None:
        return None
    if isinstance(value, str):
        return value
    return bytes(value).decode(encoding)


def hexstr(value):
    return hexlify(as_bytes(value)).decode("ascii")


def byte_value(value):
    if isinstance(value, int):
        return value
    return value[0]
