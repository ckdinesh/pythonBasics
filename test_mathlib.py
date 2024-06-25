import mathlib

def test_calc_total():
    total = mathlib.calc_total(3, 5)
    assert total == 8

def test_calc_multiply():
    result = mathlib.calc_multiply(20, 2)
    assert result == 40