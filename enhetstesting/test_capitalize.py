import pytest

def capital_case(x):
    return x.capitalize()

def lower_case(text):
    return text.lower()

def test_capital_case():
    assert capital_case("semaphore") == "Semaphore"
    assert True == False

def test_lower_case():
    assert False==False
    assert lower_case("HEI") == "hei"

def test_True_False():
    assert False == True




