import pytest
from api import verificar_primo



def test_primo():
    assert verificar_primo(5) == {'respuesta': True, 'validacion': 'Solicitud Exitosa'}

def test_no_primo():
    assert verificar_primo(6) == {'respuesta': False, 'validacion': 'Solicitud Exitosa'}

def test_fibonacci():
    assert fibonacci(5) == 5