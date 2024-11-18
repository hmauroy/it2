# Her er en Python-implementasjon av klassene som er beskrevet 
# i oppgaven for VitaZoo.
from random import randint

class Dyr:
    teller = 1
    def __init__(self, art, alder, behov=[]):
        self.art = art
        self.alder = alder
        self.behov = behov
        self.identifikasjonskode = self.settId()
    
    def settId(self):
        Dyr.teller += 1000
        return Dyr.teller + randint(100,500)

    def __str__(self):
        return f"Art: {self.art}, Alder: {self.alder}, ID: {self.identifikasjonskode}, Behov: {self.behov}"


class Fugl(Dyr):
    def __init__(self, art, alder, vingespenn, behov):
        super().__init__(art, alder, behov)
        self.vingespenn = vingespenn

    def __str__(self):
        return f"{super().__str__()}, Vingespenn: {self.vingespenn} cm"


class Pattedyr(Dyr):
    def __init__(self, art, alder, pelsfarge, behov):
        super().__init__(art, alder, behov)
        self.pelsfarge = pelsfarge

    def __str__(self):
        return f"{super().__str__()}, Pelsfarge: {self.pelsfarge}"

class Ghost(Pattedyr):
    def __init__(self):
        super().__init__("Tiger", 8, "Hvit", ["trær", "gress"])
        self.identifikasjonskode = "Ghost"
        self.kosthold = "Rådyr"
    
    def __str__(self):
        return f"{super().__str__()}, kosthold: {self.kosthold}"



class Område:
    def __init__(self, navn, features=[]):
        self.navn = navn
        self.features = features
        self.dyr_i_område = []

    def legg_til_dyr(self, dyr) -> bool|str:
        kan_legges_til = True
        for behov in dyr.behov:
            if behov not in self.features:
                kan_legges_til = False
        if kan_legges_til:
            self.dyr_i_område.append(dyr)
            return True
        else:
            return f"Kan ikke plassere dyret i dette området pga. oppfyller ikke dyrets behov."

    def fjern_dyr(self, dyr):
        self.dyr_i_område.remove(dyr)

    def __str__(self):
        område_info = f"Område: {self.navn}\n"
        område_info += "Egenskaper: \n"
        for feat in self.features:
            område_info += "- " + feat + "\n"
        område_info += "\n"
        if len(self.dyr_i_område) == 0:
            område_info += "Tomt\n"
        for dyr in self.dyr_i_område:
            område_info += str(dyr)
            område_info += "\n"
        return område_info


class VitaZoo:
    def __init__(self):
        self.områder = {}

    def legg_til_område(self, område):
        self.områder[område.navn] = område

    def fjern_område(self, navn):
        if navn in self.områder:
            if len(self.områder[navn]) == 0:
                del self.områder[navn]
            print("Du må først flytte aktuelle dyr i området til andre plasser.")

    def finn_dyr_i_område(self, område_navn, identifikasjonskode):
        """
            Returnerer dyr-objektet fra id-koden og områdenavnet.
            Finnes ikke dyret returneres False.
        """
        område = self.områder[område_navn]
        if område:
            for dyr in område.dyr_i_område:
                if dyr.identifikasjonskode == identifikasjonskode:
                    return dyr
        return False

    def flytt_dyr(self, identifikasjonskode, fra_område, til_område):
        dyr = self.finn_dyr_i_område(fra_område, identifikasjonskode)
        if dyr:
            print(
                f"Flytter ID: {identifikasjonskode}: {dyr.art}")
            self.områder[fra_område].fjern_dyr(dyr)
            self.områder[til_område].legg_til_dyr(dyr)
            return True
        return False

    def __str__(self):
        # Bugger opp en streng med utskrift av hvert område med str() metoden.
        zoo_info = "\nVitaZoo\n"
        for område in self.områder.values():
            zoo_info += str(område) + "\n"
        return zoo_info


def main():
    # Eksempel på bruk:
    vitazoo = VitaZoo()

    savanne = Område("Savanne", ["trær","gress","vannhull"])
    regnskog = Område("Regnskog", ["bregner", "trær", "fuktighet", "drikkevann"])
    nordisk_skog = Område("Norden", ["trær", "gress", "drikkevann"])

    gnu = Pattedyr("Gnu", 5, "Brun", ["gress"])
    ørn = Fugl("Bald Eagle", 3, 180, ["trær"])
    ghost = Ghost()

    savanne.legg_til_dyr(gnu)
    savanne.legg_til_dyr(ghost)
    regnskog.legg_til_dyr(ørn)

    vitazoo.legg_til_område(savanne)
    vitazoo.legg_til_område(regnskog)
    vitazoo.legg_til_område(nordisk_skog)

    # Print ut informasjon om VitaZoo
    print(vitazoo)

    print(f'I Savanne finnes Ghost: {vitazoo.finn_dyr_i_område("Savanne","Ghost")}')

    # Flytter Ghost fra savannen til regnskogen
    vitazoo.flytt_dyr("Ghost", "Savanne", "Norden")

    # Print ut informasjon
    print(vitazoo)

    print(f'I Savanne finnes Ghost: {vitazoo.finn_dyr_i_område("Savanne","Ghost")}')

if __name__ == "__main__":
    main()