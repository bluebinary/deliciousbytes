import pytest
import sys
import os

path = os.path.join(os.path.dirname(__file__), "..", "source")

sys.path.insert(0, path)  # add library path for importing into the tests

import deliciousbytes
