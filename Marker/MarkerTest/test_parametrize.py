#Approch-1
import pytest

from pythonUnitTest.Marker.Python_code.test import add1
# Individually call unit test for different sets of data
#Instead of writing each n number of same unit test case we can go for parametrize
'''def test_num():
    assert add1(10,30)==40

def test_str():
    assert add1("muru","gesh")=="murugesh"

def test_list():
    assert add1(["a","b"],["c"])==["a","b","c"]'''

@pytest.mark.parametrize("a,b,c",[(1,1,2),("a","b","ab"),([1,2],[5],[1,2,5]),(10,10,20)],ids=['num','str','list','num'])
def test_addCall(a,b,c):
    assert add1(a,b)==c


@pytest.mark.parametrize("a,b",[("ani","anirudh"),(9)])
class Test_parametrize:
    def test_para1(self,a,b):
        assert a in b
@pytest.mark.parametrize("value",[("9"),("7893"),("vneu")])
def test_para2(value):
    assert value.isalnum()