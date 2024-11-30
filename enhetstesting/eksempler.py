# Funksjon som vi skal teste
def legg_sammen(a, b):
    return a + b


# Testfunksjon for å sjekke om legg_sammen virker
def test_legg_sammen():
    assert legg_sammen(2, 3) == 5  # Sjekker om 2 + 3 blir 5
    assert legg_sammen(0, 0) == 0  # Sjekker om 0 + 0 blir 0
    assert legg_sammen(-1, 1) == 0  # Sjekker om -1 + 1 blir 0



# Funksjon som vi skal teste
def største_tall(a, b):
    if a > b:
        return a
    else:
        return b


# Testfunksjon for å sjekke om største_tall virker
def test_største_tall():
    assert største_tall(5, 3) == 5  # Sjekker om 5 er større enn 3
    assert største_tall(0, -1) == 0  # Sjekker om 0 er større enn -1
    assert største_tall(7, 7) == 7  # Sjekker om 7 og 7 er like


