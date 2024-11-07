"""
Funksjoner i python.
"""
import math

def funksjon():
    print("Hello World!")
    return "hei"

def areal(radius):
    areal = math.pi * radius**2
    return areal

tekst = funksjon()
print(tekst)
areal(6)

ar = areal(7)
print(ar)