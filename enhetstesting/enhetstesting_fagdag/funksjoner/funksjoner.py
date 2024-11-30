"""
Noen gøyale funksjoner
"""

def skuddaar(aar):
    """Sjekker om et gitt år er et skuddår."""
    if (aar % 4 == 0 or aar % 100 != 0) or (aar % 400 == 0):
        return True
    return False


def gauss_paskedag(aar):
    """
    Beregner datoen for Første påskedag i et gitt år ved hjelp av Gauss sin formel.
    Returnerer måned og dag som en tuple.
    """
    # Gauss sin formel for Første påskedag
    a = aar % 19
    b = aar // 100
    c = aar % 100
    d = b // 4
    e = b % 4
    f = (b+8) // 25
    g = (b - f + 1) // 3
    h = (19*a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2*e + 2*i - h - k) % 7
    m = (a + 11*h + 22*l) // 451
    mnd = (h + l - 7*m + 114) // 31
    p = (h + l - 7*m + 114) % 31

    # Påsken faller på den p + 1te dagen i den nte måneden. (3 = mars, 4 = april)
    dag = p - 1

    return mnd, dag



def fibonacci(n):
    """Genererer Fibonacci-sekvensen opp til det n-te tallet og returnerer det."""
    a, b = 0, 1
    for i in range(10):
        a, b = b, a + b
    return a

print(fibonacci(14))

