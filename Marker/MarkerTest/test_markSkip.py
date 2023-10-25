import pytest

from pythonUnitTest.Marker.Python_code.test import add1

@pytest.mark.skip
def test_add():
    print(add1(10,60))