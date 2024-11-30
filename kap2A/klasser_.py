"""
To klasser som beskriver elever og skoleklasser.
"""
from datetime import datetime

class Elev:
    def __init__(self, fornavn, faar, klasse) -> None:
        self.fornavn = fornavn
        self.faar = faar
        self.klasse = klasse
        self.emoticon = "^__^"  # default emoticon
    
    def get_alder(self):
        return 2024 - self.faar
    
    def bytt_klasse(self,ny_klasse):
        self.klasse = ny_klasse
    
    def set_emoticon(self,ny_emoticon):
        self.emoticon = ny_emoticon
    
    def __str__(self):
        return f"{self.emoticon} : {self.fornavn} går i klasse {self.klasse} og er {self.get_alder()} år gammel."


class Klasse:
    def __init__(self, kode, kontaktlærer) -> None:
        self.navn = kode
        self.kontaktlærer = kontaktlærer
        self.elever = []
    
    def bytt_kontaktlærer(self, objekt):
        self.kontaktlærer = objekt

    def legg_til_elev(self, objekt):
        self.elever.append(objekt)
    
    def __str__(self):
        tekst = f"Klasse {self.navn}: \n"
        tekst += f"Kontaklærer: {self.kontaktlærer} \n"
        for elev in self.elever:
            tekst += f"{elev.fornavn} \n"
        return tekst

# Oppretter et Elev-objekt
henrik = Elev("Henrik",1983,"3C")

print(henrik)

henrik.set_emoticon(":/")

print(henrik)












exit()
henrik2 = Elev("Henrik2", 1989, "3STC")
henrik3 = Elev("Henrik3", 1984, "3STC")
henrik4 = Elev("Henrik4", 1985, "3STC")
print(henrik)

# Oppretter en klasse
klasse3STC = Klasse("3STC","Kristoffer")

# Legger til elev
klasse3STC.legg_til_elev(henrik)
klasse3STC.legg_til_elev(henrik2)
klasse3STC.legg_til_elev(henrik3)
klasse3STC.legg_til_elev(henrik4)

print(klasse3STC)