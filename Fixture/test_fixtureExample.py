import pytest


#Example-1
@pytest.fixture(scope='function',ids='g2s2')
def one():
    print("Print statement before method")
    yield 1
    print("Print statement after method")

def test_run(one):
    print("Test runing")
    assert one==1

#Example-2
@pytest.fixture
def resource():
    return "muru"

def test_Resource(resource):
    print(resource)    #printing


class TestResource(TestCase):
    def test_demo(self,resource):
        print(resource)