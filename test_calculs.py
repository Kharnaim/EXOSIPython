import pytest
from calculette import Calculatrice

def test_addition():
    calc = Calculatrice()
    assert calc.addition(1, 2) == 3
    assert calc.addition(-1, 1) == 0
    assert calc.addition(-1, -1) == -2

def test_soustract():
    calc = Calculatrice()
    assert calc.soustract(2, 1) == 1
    assert calc.soustract(2, 3) == -1
    assert calc.soustract(-1, -1) == 0

def test_multiplication():
    calc = Calculatrice()
    assert calc.multiplication(2, 3) == 6
    assert calc.multiplication(-1, 1) == -1
    assert calc.multiplication(-1, -1) == 1

def test_division():
    calc = Calculatrice()
    assert calc.division(6, 3) == 2
    assert calc.division(-1, 1) == -1
    assert calc.division(-1, -1) == 1
    assert calc.division(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        calc.division(1, 0)
