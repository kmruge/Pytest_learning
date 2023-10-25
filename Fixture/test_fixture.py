import pytest

from pythonUnitTest.Fixture.Loading_File import Student

#Here we have initialize the file and two as we want to open the file twice
#Instead we can go for tear
'''def test_method1():
    s1=Student()
    s1.loadFile("JsonFile.json")
    dict=s1.get_data("Scott")
    assert dict['id']==1
    assert dict['result']=='pass'

def test_method2():
    s1 = Student()
    s1.loadFile("JsonFile.json")
    dict=s1.get_data('Mark')
    dict['id']==2
    print(dict['name']+"\n")
    dict['result']=='fail'
'''
#Setup and tearDown method use to perform set-up action
''''
s1=None
def setup_module(module):
    global s1
    s1=Student()
    s1.loadFile("JsonFile.json")

def teardown_module(module):
    pass

def test_method1():
    dict1=s1.get_data('Mark')
    assert dict1['result'] == 'fail'
    assert dict1['id'] == 2
    '''
#fixture is bit dynamic concepts than setup and teardown method

@pytest.fixture()
def fixture_setup():
    s1=Student()
    s1.loadFile('JsonFile.json')
    yield s1
    print("After test done")



def test_run1(fixture_setup):
    dict1=fixture_setup.get_data('Scott',"students-sci")
    assert dict1['id']==1
    assert dict1['result']=='pass'
    assert dict1['location']=='Manapakkam'

def test_run2(fixture_setup):
    dict1=fixture_setup.get_data('Muru',"students-account")
    assert dict1['id']==3
    assert dict1['result']=='pass'
    assert dict1['location']=='Pazhavanthangal'