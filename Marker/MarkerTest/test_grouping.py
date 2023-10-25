import pytest

from pythonUnitTest.Marker.Python_code.test import add1

@pytest.mark.number
def test_add_num1():
    assert add1(10,10)==20

@pytest.mark.number
def test_add_num2():
    assert add1(100,200)==300
@pytest.mark.string
def test_add_str1():ß
    assert add1("muru","son")=="muruson"

@pytest.mark.string
def test_add_str2():
    assert add1("wel","come")=="welcome"