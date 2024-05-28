import pytest
from calculette import Calculatrice

def test_addition():
    calc = Calculatrice()
    assert calc.addition(1, 2) == 3
    assert calc.addition(-1, 1) == 0
    assert calc.addition(-1, -1) == -2
    assert calc.addition(0, 0) == 0
    assert calc.addition(123456, 654321) == 777777

def test_soustract():
    calc = Calculatrice()
    assert calc.soustract(2, 1) == 1
    assert calc.soustract(2, 3) == -1
    assert calc.soustract(-1, -1) == 0
    assert calc.soustract(0, 0) == 0
    assert calc.soustract(1000000, 1) == 999999

def test_multiplication():
    calc = Calculatrice()
    assert calc.multiplication(2, 3) == 6
    assert calc.multiplication(-1, 1) == -1
    assert calc.multiplication(-1, -1) == 1
    assert calc.multiplication(0, 1) == 0
    assert calc.multiplication(1000, 1000) == 1000000

def test_division():
    calc = Calculatrice()
    assert calc.division(6, 3) == 2
    assert calc.division(-1, 1) == -1
    assert calc.division(-1, -1) == 1
    assert calc.division(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        calc.division(1, 0)
    with pytest.raises(ZeroDivisionError):
        calc.division(0, 0)

def test_edge_cases():
    calc = Calculatrice()
    assert calc.addition(1e12, 1e12) == 2e12
    assert calc.soustract(1e12, 1e12) == 0
    assert calc.multiplication(1e6, 1e6) == 1e12
    assert calc.division(1e12, 1e6) == 1e6

    assert calc.addition(1e-12, 1e-12) == 2e-12
    assert calc.soustract(1e-12, 1e-12) == 0
    assert calc.multiplication(1e-6, 1e-6) == 1e-12
    assert calc.division(1e-12, 1e-6) == 1e-6

    assert calc.addition(-1e6, 1e6) == 0
    assert calc.soustract(-1e6, 1e6) == -2e6
    assert calc.multiplication(-1e6, 1e6) == -1e12
    assert calc.division(-1e6, 1e6) == -1

    assert calc.division(1, 1e-12) == 1e12
