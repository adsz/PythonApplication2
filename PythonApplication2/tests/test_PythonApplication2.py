import pytest
from PythonApplication2 import dasti

def test_dasti():
    assert dasti('Adam') == 'Ajo Adam'
    assert dasti('Adam') != None