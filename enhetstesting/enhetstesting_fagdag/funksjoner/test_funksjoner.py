import pytest
# Juster importen basert på filnavnet
from funksjoner import skuddaar, gauss_paskedag, fibonacci

# Tester for skuddaar


def test_skuddaar():
    assert skuddaar(2020) is True  # 2020 er et skuddår
    assert skuddaar(2021) is False  # 2021 er ikke et skuddår
    assert skuddaar(1900) is False  # 1900 er ikke et skuddår (delelig med 100)
    assert skuddaar(2000) is True   # 2000 er et skuddår (delelig med 400)
    assert skuddaar(2024) is True   # 2024 er et skuddår

# Tester for gauss_paskedag


def test_gauss_paskedag():
    # Første påskedag i 2023 er 9. april
    assert gauss_paskedag(2023) == (4, 9)
    # Første påskedag i 2024 er 31. mars
    assert gauss_paskedag(2024) == (3, 31)
    # Første påskedag i 2000 er 23. april
    assert gauss_paskedag(2000) == (4, 23)
    # Første påskedag i 2010 er 4. april
    assert gauss_paskedag(2010) == (4, 4)
    # Første påskedag i 2025 er 20. april
    assert gauss_paskedag(2025) == (4, 20)

# Tester for fibonacci


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3 
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55 
    assert fibonacci(14) == 375 
