import pytest
from source import my_func as func


def add_test():
    result =  func.add(1,5)
    assert result == 6