import pytest
from api import verificar_primo

def test_primo():
    assert verificar_primo(5) == True