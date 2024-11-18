import pytest
from zoo import *



@pytest.fixture
def zoo():
    '''Returnerer en dyrehage med ingen områder'''
    return VitaZoo()


@pytest.fixture
def barskog():
    '''Returnerer en tom barskog'''
    return Område("Barskog",["grantrær","furutrær"])

@pytest.fixture
def savanne():
    '''Returnerer en tom savanne'''
    return Område("Savanne", ["busker", "vannhull", "sand"])

@pytest.fixture
def rev_1():
    '''Returnerer første pattedyr: en rev.'''
    return Pattedyr("rev",2,"rødbrun","gnagere")

@pytest.fixture
def mus_2():
    '''Returnerer andre pattedyr: en mus.'''
    return Pattedyr("mus",0.05,"grå","røtter")

"""Testene kommer her:"""

def test_default_barskog(barskog):
    assert barskog.navn == "Barskog"
    assert "grantrær" in barskog.features
    assert "furutrær" in barskog.features

def test_settId_1(rev_1):
    assert 101 <= rev_1.identifikasjonskode <= 501

def test_settId_2(rev_1,mus_2):
    assert rev_1.identifikasjonskode != mus_2.identifikasjonskode