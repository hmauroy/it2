"""
Test-suite for filen matematiske_operasjoner.py
"""

import pytest
from matematiske_operasjoner_løsning import (add_and_subtract,
                                     multiply_and_divide,
                                     power_and_square_root,
                                     floor_and_ceil,
                                     mod_and_integer_division,
                                     average_and_sum)

# Tester for add_and_subtract


def test_add_and_subtract():
    assert add_and_subtract(10, 5) == (15, 5)
    assert add_and_subtract(-3, -2) == (-5, -1)
    assert add_and_subtract(0, 0) == (0, 0)

# Tester for multiply_and_divide


def test_multiply_and_divide():
    assert multiply_and_divide(10, 2) == (20, 5)
    assert multiply_and_divide(-3, 3) == (-9, -1)
    assert multiply_and_divide(-3, 0) == "Kan ikke dele på null!"

# Tester for power_and_square_root


def test_power_and_square_root():
    assert power_and_square_root(4, 2) == (16, 2.0)
    assert power_and_square_root(9, 0.5) == (3.0, 3.0)

# Tester for floor_and_ceil


def test_floor_and_ceil():
    assert floor_and_ceil(3.7, 2.3) == (3, 3)
    assert floor_and_ceil(-3.1, -2.5) == (-4, -2)

# Tester for mod_and_integer_division


def test_mod_and_integer_division():
    assert mod_and_integer_division(10, 3) == (1, 3)
    assert mod_and_integer_division(10, 0) == "Kan ikke dele på null!"

# Tester for average_and_sum


def test_average_and_sum():
    assert average_and_sum(10, 20) == (15.0, 30)
    assert average_and_sum(-5, 5) == (0.0, 0)
