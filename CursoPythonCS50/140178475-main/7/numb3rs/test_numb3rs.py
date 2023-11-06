from numb3rs import validate
import pytest

def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1&2@3€4") == False
    assert validate(r"....") == False
    assert validate(r"cat.dog.dog.cat") == False


def test_range():
    assert validate(r"127.0.0.1") == True
    assert validate(r"1.3.6.281111") == False
    assert validate(r"255.255.256.255") == False
    assert validate(r"1.98111.1.3") ==  False
    assert validate(r"256.1.1.1") == False
    assert validate(r"1.1.1.1") == True
