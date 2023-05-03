import pytest

def test_primo():
    assert es_primo(5) == True

def test_no_primo():
    assert es_primo(6) == False