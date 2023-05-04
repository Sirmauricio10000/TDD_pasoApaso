import pytest
from api import fibonacci, helloFastApi, verificar_primo



def test_primo():
    assert verificar_primo(5) == {'respuesta': True, 'validacion': 'Solicitud Exitosa'}

def test_no_primo():
    assert verificar_primo(6) == {'respuesta': False, 'validacion': 'Solicitud Exitosa'}

def test_fibonacci():
    assert fibonacci(5) == {"validacion": "Solicitud Exitosa", "respuesta": 5}

def test_helloFastApi():
    assert helloFastApi() == {"mensaje": "Hello FastAPI"}