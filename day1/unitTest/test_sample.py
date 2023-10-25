import pytest

from pythonUnitTest.day1.addition.calculator import calculator

s1=calculator()
#We can run it with assert and without assert
#Assert is just for verify the result
def test_add():
    assert s1.add(10,10)==20
def test_sub():
    assert s1.sub(10,5)==4


def test_add1():
    assert s1.add(20,30)==50

class TestSample:
    def test_add1(self):
        assert s1.add(20,10)==30

    def test_sub1(self):
        assert s1.sub(3,2)==1

    def test_str(self):
        assert s1.textTest()=="call"