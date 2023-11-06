import pytest
from seasons import check_input

def test_check_input():
    assert check_input("1998-01-23") == ("1998", "01", "23")
    assert check_input("1998-7-3") == None
    assert check_input("july 3, 1998") == None