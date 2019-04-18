import os

from ..lab_python_utils import _os

def test_path():
    assert _os.here() == os.path.dirname(os.path.realpath(__file__))

