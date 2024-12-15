import pytest

from src.operaciones import suma, resta, multiplicacion, division, square

def test_suma():
    assert suma(1, 1) == 2

def test_resta():
    assert resta(1, 1) == 0

def test_multiplicacion():
    assert multiplicacion(1, 1) == 1

def test_division():
    assert division(1, 1) == 1

def test_division_raises():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert square(input) == expected