import pytest
from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci_n_equals_0():
    expected = 0
    actual = fibonacci(0)
    assert expected == actual

def test_fibonacci_n_equals_1():
    expected = 1
    actual = fibonacci(1)
    assert expected == actual

def test_fibonacci_n_equals_2():
    expected = 1
    actual = fibonacci(2)
    assert expected == actual

def test_fibonacci_n_equals_4():
    expected = 3
    actual = fibonacci(4)
    assert expected == actual

def test_fibonacci_n_equals_7():
    expected = 13
    actual = fibonacci(7)
    assert expected == actual

def test_fibonacci_n_is_negative():
    expected = 0
    actual = fibonacci(-10)
    assert expected == actual