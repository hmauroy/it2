import pytest

# Anta at funksjonene er definert i en fil kalt minibank.py og importeres slik:
from minibank import sjekk_saldo, innskudd, uttak, overføring, vis_transaksjonshistorikk

# Vi definerer kontoer som en fixture


@pytest.fixture
def reset_kontoer():
    """Returnerer en kjent tilstand av kontoene før hver test."""
    return {
        '123456789': {'saldo': 5000, 'transaksjoner': []},
        '987654321': {'saldo': 3000, 'transaksjoner': []},
    }

# Test sjekk_saldo funksjonen


def test_sjekk_saldo(reset_kontoer):
    kontoer = reset_kontoer
    assert sjekk_saldo('123456789', kontoer) == 5000
    assert sjekk_saldo('987654321', kontoer) == 3000
    assert sjekk_saldo('111111111', kontoer) == "Konto ikke funnet"

# Test innskudd funksjonen


def test_innskudd(reset_kontoer):
    kontoer = reset_kontoer
    assert innskudd('123456789', 1000, kontoer) == 6000
    assert innskudd('987654321', 500, kontoer) == 3500
    assert innskudd('111111111', 1000, kontoer) == "Konto ikke funnet"

# Test uttak funksjonen


def test_uttak(reset_kontoer):
    kontoer = reset_kontoer
    assert uttak('123456789', 1000, kontoer) == 4000
    assert uttak('987654321', 3000, kontoer) == 0
    assert uttak('987654321', 500, kontoer) == "Ikke nok saldo"
    assert uttak('111111111', 500, kontoer) == "Konto ikke funnet"

# Test overføring funksjonen


def test_overføring(reset_kontoer):
    kontoer = reset_kontoer
    assert overføring('123456789', '987654321', 2000, kontoer) == (3000, 5000)
    assert overføring('123456789', '987654321', 5000,
                      kontoer) == "Ikke nok saldo på avsenderkonto"
    assert overføring('111111111', '987654321', 1000,
                      kontoer) == "En eller begge kontoer ble ikke funnet"
    assert overføring('123456789', '111111111', 1000,
                      kontoer) == "En eller begge kontoer ble ikke funnet"

# Test vis_transaksjonshistorikk funksjonen


# Test vis_transaksjonshistorikk funksjonen
def test_vis_transaksjonshistorikk(reset_kontoer):
    kontoer = reset_kontoer
    innskudd('123456789', 1000, kontoer)
    uttak('123456789', 500, kontoer)
    overføring('123456789', '987654321', 2000, kontoer)
    assert vis_transaksjonshistorikk('123456789', kontoer) == [
        "Innskudd: +1000 kr",
        "Uttak: -500 kr",
        "Overføring til 987654321: -2000 kr"
    ]
    assert vis_transaksjonshistorikk('987654321', kontoer) == [
        "Overføring fra 123456789: +2000 kr"
    ]
    assert vis_transaksjonshistorikk(
        '111111111', kontoer) == "Konto ikke funnet"
