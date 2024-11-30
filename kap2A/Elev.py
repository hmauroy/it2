"""
Klassen elev
"""

class Elev:
    def __init__(self,fornavn, faar) -> None:
        self.fornavn = fornavn
        self.faar = faar
    
    def __str__(self):
        return f"{self.fornavn}, født {self.faar}"

elev1 = Elev("Henrik", 1983)
print(elev1)
print(elev1.fornavn)
print(elev1.faar)

# Liste til å fylle opp med elev-objekter
klasse3C = []
klasse3C.append(elev1)
# Lager mange elev-objekter med for-løkke
for i in range(30):
    elev = Elev(f"elev{i}",i+2000)
    klasse3C.append(elev)
for elev in klasse3C:
    print(elev)
