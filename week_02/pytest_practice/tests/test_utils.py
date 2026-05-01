import pytest

from week_02.pytest_practice.utils import add, divide


def test_add_positive_numbers():
    assert add(4,2) == 6


def test_add_negative_numbers():
    assert add(-3,-5) == -8


def test_add_positive_and_negative_numbers():
    assert add(5, -5) == 0


def test_add_zero_numbers():
    assert add(0, 0) == 0


def test_divide_positive_numbers():
    assert divide(10, 5) == 2.0


def test_divide_positive_and_negative_numbers():
    assert divide(10, -5) == -2.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

