"""
Klasse som definerer en skoleklasse på Vgs.
"""
from Elev import Elev

class Klasse:
    def __init__(self, navn) -> None:
        self.navn = navn
        self.elever = []
    
    def legg_til(self,elevobjekt):
        self.elever.append(elevobjekt)

kl3C = Klasse("3C")
elev = Elev("henrik",1983)
kl3C.legg_til(elev)
print(kl3C.elever) # Printer ut alle elementene i listen.