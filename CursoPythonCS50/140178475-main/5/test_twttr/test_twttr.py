from twttr import shorten
import sys

def test_twttr():
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("Twitter") == "Twttr"
    assert shorten("12") == "12"
    assert shorten("") == ""
    assert shorten("AbdUzcan tariot") == "bdzcn trt"
    assert shorten("CS50") == "CS50"
