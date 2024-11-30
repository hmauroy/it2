from funksjoner import *
import pytest

#print(legg_sammen(1,4))

def test_legg_sammen():
    assert legg_sammen(1,4) == 5
    assert legg_sammen(9,11) == 20
    assert legg_sammen(9,0) == "b er null!"
