import pytest
from source import my_func as func


def test_add():
    result =  func.add(1,5)
    assert result == 6


def test_subtract():
    result = func.subtract(1,5)
    assert result == -4


def test_divide():
    result = func.divide(6,3)
    assert result == 2

def test_div0():
    with pytest.raises(ZeroDivisionError):
        func.divide(2,0)
        