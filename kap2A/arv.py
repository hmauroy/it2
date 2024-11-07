"""
Eksempel som viser arv fra én klasse til underklasser.
"""
class Person:
    def __init__(self, fornavn, etternavn, alder=18) -> None:
        """Konstruktør-metoden for klassen."""
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.alder = alder
    
    def __str__(self):
        return f"{self.fornavn} {self.etternavn}, {self.alder} år"

class Elev(Person):
    def __init__(self,fornavn, etternavn, alder, klasse) -> None:
        super().__init__(fornavn, etternavn, alder)
        self.klasse = klasse
    def __str__(self):
        return super().__str__() + f", {self.klasse}"

class Laerer(Person):
    def __init__(self, fornavn, etternavn, alder, kontor, kontordager=[]) -> None:
        super().__init__(fornavn, etternavn, alder)
        self.kontor = kontor
        self.kontordager = kontordager
    def visKontorDager(self):
        dager = ""
        for dag in self.kontordager:
            dager += dag + ", "
        return dager
    def __str__(self):
        return super().__str__() + f", kontor: {self.kontor}, kontordager: {self.visKontorDager()}"


#print(help(Person))
def main():
    person1 = Person("Jan", "Johansen", 42)
    print(person1)
    elev1 = Elev("navn", "navnesen", 42, "3C")
    print(elev1)
    henrik = Laerer("henrik","mauroy",41,"02-28",["tirs","tors"])
    print(henrik)

if __name__ == "__main__":
    main()