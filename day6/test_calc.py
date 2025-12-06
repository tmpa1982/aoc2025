from calc import calculate

import pytest


def test_calculate_addition():
    result = calculate([3, 5], "+")
    assert result == 8

def test_calculate_multiplication():
    result = calculate([3, 5], "*")
    assert result == 15

def test_calculate_addition_long():
    result = calculate([3, 5, 6, 7], "+")
    assert result == 21

def test_calculate_multiplication_long():
    result = calculate([3, 5, 1, 2], "*")
    assert result == 30

def test_calculate_invalid_operation():
    with pytest.raises(ValueError):
        calculate([1, 2], "x")
