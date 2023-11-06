from um import count
import pytest

def test_Upper():
    assert count("Um, thanks, um...") == 2

def test_simbols():
    assert count("um?") == 1

def test_count():
    assert count("um") == 1
    assert count("Um, thanks for the album.") == 1