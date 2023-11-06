from fuel import convert
from fuel import gauge
import pytest


def test_convert():
    assert convert("4/4") == 100
    assert convert("1/4") == 25

def test_DivisonCero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_ValueError():
    with pytest.raises(ValueError):
        convert("cat/d")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
