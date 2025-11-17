from lib.instance_methods import Calculator

def test_add():
    calc = Calculator(5)
    assert calc.add(3) == 8

def test_multiply():
    calc = Calculator(4)
    assert calc.multiply(3) == 12

def test_square():
    calc = Calculator(6)
    assert calc.square() == 36
