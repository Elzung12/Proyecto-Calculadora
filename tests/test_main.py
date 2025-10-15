import pytest
from src.main import (
    sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada,
    modulo, porcentaje, promedio, maximo, minimo, factorial
)

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 5) == -5

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-2, 3) == -6

def test_dividir():
    assert dividir(6, 3) == 2
    with pytest.raises(ValueError):
        dividir(5, 0)

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1

def test_raiz_cuadrada():
    assert raiz_cuadrada(9) == 3
    with pytest.raises(ValueError):
        raiz_cuadrada(-4)

def test_modulo():
    assert modulo(10, 3) == 1
    with pytest.raises(ValueError):
        modulo(10, 0)

def test_porcentaje():
    assert porcentaje(25, 100) == 25
    with pytest.raises(ValueError):
        porcentaje(10, 0)

def test_promedio():
    assert promedio([2, 4, 6]) == 4
    with pytest.raises(ValueError):
        promedio([])

def test_maximo():
    assert maximo([1, 9, 3, 7]) == 9
    with pytest.raises(ValueError):
        maximo([])

def test_minimo():
    assert minimo([1, 9, 3, 7]) == 1
    with pytest.raises(ValueError):
        minimo([])

def test_factorial():
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-3)
