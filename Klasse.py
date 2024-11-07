"""
Klasse
navn: str
antall: int
rom: str
fag: list
lærer: str
elever: list
__________________
__str__() - printer ut alle elevene i klassen
legg_til()
bytt_rom()
fjern_elev()
bytt_lærer()

"""

#from Elev import Elev

class Elev:
    def __init__(self,fornavn) -> None:
        self.fornavn = fornavn

class Klasse:
    def __init__(self, navn, lærer, rom) -> None:
        self.navn = navn
        self.antall = 0
        self.rom = rom
        self.fag = []
        self.lærer = lærer
        self.elever = [] # Liste med elevobjekter
    
    def __str__(self):
        utskrift = ""
        for elev in self.elever:
            utskrift += elev.fornavn + "\n"
        return utskrift
    
    def legg_til(self, elevobjekt):
        self.elever.append(elevobjekt)
    
    def fjern_elev(self,elevnavn):
        # Finner om eleven finnes.
        for elev in self.elever:
            if elev.fornavn == elevnavn:
                # Fjerner selve objektet fra listen med remove
                self.elever.remove(elev)
                return True
        return False
    
    def bytt_rom(self,nyttrom):
        self.rom = nyttrom
    
    def bytt_lærer(self, nytt_lærernavn):
        self.lærer = nytt_lærernavn


def main():
    elev1 = Elev("henrik")
    elev2 = Elev("amanda")
    elev3 = Elev("victor")

    kl3C = Klasse("3C","Øyvind Karlsen",304)

    kl3C.legg_til(elev1)
    kl3C.legg_til(elev2)
    kl3C.legg_til(elev3)

    print(kl3C)

    kl3C.fjern_elev("henrik")

    print(kl3C)

if __name__ == "__main__":
    main()