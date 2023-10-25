import pytest

from pythonUnitTest.Marker.Python_code.test import add1

@pytest.mark.xfail
def test_call():
    num=100
    assert num>100

@pytest.mark.xfail(1<2,reason="Output is Xfailed")
def test_call1():
    raise ValueError

@pytest.mark.xfail(reason='Output is Xpassed')
def test_call2():
    assert 10==10

#Class with mark and without mark functions
class TestCall:
    @pytest.mark.xfail
    def test_call1(self):
        assert 10==10

    def test_call2(self):
        assert 20==20

#mark function for whole class
@pytest.mark.xfail
class TestCall1:
    def test_call1(self):
        assert 40==40
    def test_call2(self):
        assert 30==30
    def test_call3(self):
        assert 10==15
