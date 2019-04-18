import os

from ..lab_python_utils import _os


def test_here():
    assert _os.here() == os.path.dirname(os.path.realpath(__file__))


def test_heref():
    assert _os.heref() == os.path.realpath(__file__)

