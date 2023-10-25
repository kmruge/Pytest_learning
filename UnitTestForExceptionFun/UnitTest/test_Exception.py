import pytest
from UnitTestForExceptionFun.PythonCode.exception import raiseException

#Exception alone
'''def test_sample():
    with pytest.raises(ValueError):
        raiseException(10)'''

#Exception with message validation
'''def test_sample():
    with pytest.raises(ValueError) as out:
        raiseException(-10)
        #value method get the message mentioned that expection
    assert str(out.value)=="This error raised by myself"'''

#Exception with message validation in same line
def test_sample():
    with pytest.raises(ValueError, match="This error raised by myself"):
        raiseException(-1)