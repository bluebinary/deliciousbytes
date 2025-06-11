import pytest
import sys
import os

path = os.path.join(os.path.dirname(__file__), "..", "source")

sys.path.insert(0, path)  # add library path for importing into the tests

import deliciousbytes


def print_bytes_hex(data: bytes, prefix: bool = False):
    hex_string = ("" if prefix else " ").join(
        [(r"\x" if prefix else "") + f"{byte:02x}" for byte in data]
    )
    print(('b"' if prefix else "") + hex_string + ('"' if prefix else ""))
