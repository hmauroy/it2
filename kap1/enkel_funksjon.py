"""
Enkel funksjon i python.
"""

# I python må funksjoner deklareres øverst i koden

# Funksjon som beregner sum av to tall.
def sum(a,b):
    # Return returnerer én ting.
    return a + b

# En funksjon skal helst gjøre kun én ting.
def hello_world():
    print("Hello World")
    return True

sum(1,4)
print(f"1 + 4 = {sum(1,4)}")

hello_world()

print(f"hello_world-funsjonen gir returverdi: {hello_world()}")

# LAg kalkulatorfunksjoner som utfører de fire regneartene
# +, - , * , /
# og 10-er-logaritmen: math.log10()
import math
def logaritme(tall):
    return math.log10(tall)

print(logaritme(111))