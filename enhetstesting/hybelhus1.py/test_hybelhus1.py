import pytest
from hybelhus1 import flytt_inn, flytt_ut, sjekk_status, vis_studentinfo

# Global ordbok for å lagre studentinformasjon
leiligheter = {}

# Fixture for å reset leiligheter før hver test


@pytest.fixture
def reset_leiligheter():
    """Returnerer en kjent tilstand av leiligheter før hver test."""
    global leiligheter
    leiligheter = {}  # Reset leiligheter til tom ordbok
    flytt_inn("123", "Ola Nordmann", "ola@example.com", "12345678")
    flytt_inn("456", "Kari Nordmann", "kari@example.com", "87654321")

# Test for flytt_inn


def test_flytt_inn(reset_leiligheter):
    assert flytt_inn("789", "Per Hansen", "per@example.com",
                     "11223344") == "Per Hansen har flyttet inn."
    assert "789" in leiligheter
    assert leiligheter["789"]["navn"] == "Per Hansen"


def test_flytt_inn_eksisterende_student(reset_leiligheter):
    assert flytt_inn("123", "Ola Nordmann", "ola@example.com",
                     "12345678") == "Studenten er allerede registrert."

# Test for flytt_ut


def test_flytt_ut(reset_leiligheter):
    assert flytt_ut("123") == "Ola Nordmann har flyttet ut."
    assert leiligheter["123"]["status"] == "out"


def test_flytt_ut_allerede_ut(reset_leiligheter):
    flytt_ut("123")  # Flytt ut en gang til
    assert flytt_ut("123") == "Studenten har allerede flyttet ut."


def test_flytt_ut_student_ikke_finnes(reset_leiligheter):
    assert flytt_ut("999") == "Studenten finnes ikke."

# Test for sjekk_status


def test_sjekk_status(reset_leiligheter):
    assert sjekk_status("123") == "Ola Nordmann er inn."
    flytt_ut("123")
    assert sjekk_status("123") == "Ola Nordmann er ut."


def test_sjekk_status_student_ikke_finnes(reset_leiligheter):
    assert sjekk_status("999") == "Studenten finnes ikke."

# Test for vis_studentinfo


def test_vis_studentinfo(reset_leiligheter):
    expected_output = "Navn: Ola Nordmann, E-post: ola@example.com, Telefon: 12345678, Status: in"
    assert vis_studentinfo("123") == expected_output


def test_vis_studentinfo_student_ikke_finnes(reset_leiligheter):
    assert vis_studentinfo("999") == "Studenten finnes ikke."
