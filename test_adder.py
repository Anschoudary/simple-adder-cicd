import pytest
from adder import add


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -4) == -5


def test_add_mixed_numbers():
    assert add(5, -2) == 3


def test_add_zero():
    assert add(0, 7) == 7
