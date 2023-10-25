import pytest

from pythonUnitTest.Marker.Python_code.test import add1

@pytest.mark.skipif(10<1,reason='Conditions not satisfied')
def test_addition():
    print(add1(20,20))