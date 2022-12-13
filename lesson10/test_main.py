import library
import pytest


def test_asserts():
    assert library.exponentiation(2, 2, expo_num=2) == 16, 'not expected result'
    assert library.exponentiation(-2, 3, expo_num=2) == 36, 'unexpected behaviour'


def test_type_error():
    with pytest.raises(TypeError):
        library.exponentiation([], {}, a=())


def test_type_error_2():
    with pytest.raises(TypeError):
        library.exponentiation('a', 'a', expo_num='a')


#
def test_value_error():
    with pytest.raises(ZeroDivisionError):
        library.exponentiation(0, 0, expo_num=-3)
