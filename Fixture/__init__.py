
dict={"a":1,"b":2,"c":3}
list=list(dict.values())
print(list)

def setup_method():
    print("setup Method")

def teardown_method():
    print("tearDown ")

def test_call():
    print("call")