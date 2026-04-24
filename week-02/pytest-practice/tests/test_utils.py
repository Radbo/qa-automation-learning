from utils import add
from utils import divide


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


def test_divide_positive_and_zero_numbers():
    assert divide(10, 0) == 0
