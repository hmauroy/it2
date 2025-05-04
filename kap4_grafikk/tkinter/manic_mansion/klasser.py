"""
klasser for spillet Manic Mansion.
Implementert fra UML-klassediagrammet fra Eksamen Høst 2023.

Henrik Mauroy
hmauroy@gmail.com
"""

class Spillebrett:
    def __init__(self,h,b):
        self.høyde = h
        self.bredde = b
        self.objekter = []
    
    def leggTileObjekt(self, objekt):
        self.objekter.append(objekt)
    
    def fjernObjekt(self, objekt):
        """ Fjerner et unikt objekt fra listen objekter"""
        if objekt in self.objekter:
            self.objekter.remove(objekt)
            return True
        else:
            return False
    
    def tegnAlleObjekt(self, canvas):
        """Går gjennom alle objekter og tegner dem."""
        for objekt in self.objekter:
            canvas.create_rectangle(
                objekt.xPosisjon - objekt.bredde/2,
                objekt.yPosisjon - objekt.bredde/2,
                objekt.xPosisjon + objekt.bredde/2,
                objekt.yPosisjon + objekt.bredde/2,
                fill=objekt.farge,
                outline=objekt.farge,
                width=1,
                tags = objekt.id
            )
            canvas.create_text(objekt.xPosisjon, objekt.yPosisjon, text=objekt.text, font=("Arial", 14), fill="black")

    def oppdater(self, canvas):
        """Oppdaterer alt
        1) Flytt alle objekt
        2) Sjekk for kollisjon mellom objekter eller vegger.
        3) Flytt alle objekt fra canvas
        4) Dersom avslutning eller game over returneres False, ellers True.
        """
        return True
    
    


class Spillobjekt:
    teller = 0
    def __init__(self,xStart,yStart,bredde):
        self.xPosisjon = xStart
        self.yPosisjon = yStart
        self.farge = "grey"
        self.text = "H"
        self.bredde = bredde
        self.id = Spillobjekt.teller
        Spillobjekt.teller += 1 # Øker med én så neste objekt får en ny id.
    
    def plassering(self,x,y):
        self.xPosisjon = x
        self.yPosisjon = y

    def flytt(self, dx,dy):
        self.plassering(self.xPosisjon + dx, self.yPosisjon + dy)



class Menneske(Spillobjekt):
    def __init__(self, xStart, yStart, bredde,fart):
        super().__init__(xStart, yStart, bredde)
        self.fart = fart
        self.poeng = 0
        self.bærerSau = False
        self.farge = "peachpuff"
        self.text = "M"
    
    def plassering(self, x, y):
        """Denne metoden bør ikke finns men er i UML-diagrammet."""
        super().plassering(x, y)
    
    def beveg(self,lengde,retning):
        """
        Beveger et antall px i x- eller y-akse.
        """
        if retning == "L":
            self.flytt(-lengde,0)
        elif retning == "U":
            self.flytt(0,-lengde)
        elif retning == "R":
            self.flytt(lengde,0)
        elif retning == "D":
            self.flytt(0,lengde)
        else:
            return False
        return True
    
    def reduserFart(self, reduksjon):
        self.fart -= reduksjon
        if self.fart <= 0:
            self.fart = 0
    
    def økPoeng(self, antall):
        self.poeng += antall
    
    def bærSau(self, sauobjekt):
        if self.bærerSau:
            return False
        else:
            self.bærerSau = True
            return True
    
    def sjekkKollisjon(self):
        """Sjekker for kollisjon med alle andre objekter"""

class Spøkelse(Spillobjekt):
    def __init__(self, xStart, yStart, bredde, xFart, yFart, bounding_box=[0,0,500,500]):
        super().__init__(xStart, yStart, bredde)
        self.xFart = xFart
        self.yFart = yFart
        self.farge = "#eeeeee"
        self.text = "S"
        self.bb = bounding_box
    
    def plassering(self, x, y):
        """Unødvendig metode."""
        super().plassering(x, y)
    
    def endreRetning(self):
        """Ved kollisjon med en av veggene så skal en akse endre retning."""
        if self.xPosisjon <= self.bb[0]:    # venstre vegg
            self.xPosisjon = self.bredde/2  # flytter inn på brettet hvis utenfor.
            self.xFart = -self.xFart
        elif self.xPosisjon >= self.bb[2]:  # høyre vegg
            self.xPosisjon = self.bb[2] - self.bredde/2
            self.xFart = -self.xFart
        elif self.yPosisjon >= self.bb[3]:  # bunnen
            self.yPosisjon = self.bb[3] - self.bredde/2
            self.yFart = -self.yFart
        elif self.yPosisjon <= self.bb[1]:  # toppen
            self.yPosisjon = self.bredde/2
            self.yFart = -self.yFart

    
class Hindring(Spillobjekt):
    def __init__(self, xStart, yStart, bredde):
        super().__init__(xStart, yStart, bredde)

    def plassering(self, x, y):
        """Unødvendig metode."""
        return super().plassering(x, y)

class Sau(Spillobjekt):
    def __init__(self, xStart, yStart, bredde):
        super().__init__(xStart, yStart, bredde)
        self.blirBåret = False
        self.aktiv = True
        self.farge = "deeppink"
        self.text = "BÆ"
    
    def plassering(self, x, y):
        """Unødvendig metode."""
        return super().plassering(x, y)

    def blirLøftet(self):
        self.blirBåret = True
    
    def fjernSau(self):
        """Fjerner sauen fra spillet ved å sette den inaktiv.
        Hadde vært bedre om Spillbrettet hadde håndtert dette."""
        self.aktiv = False


def main():
    s = Spillebrett(500,500)
    m = Menneske(30,30,5)
    sau1 = Sau(400,100)
    sau2 = Sau(400,150)
    sau3 = Sau(400,200)
    spøk = Spøkelse(500,500,10,12)
    h = Hindring(200,200)
    s.leggTileObjekt(m)
    s.leggTileObjekt(sau1)
    s.leggTileObjekt(sau2)
    s.leggTileObjekt(sau3)
    s.leggTileObjekt(spøk)
    s.leggTileObjekt(h)
    s.fjernObjekt(sau1)
    for obj in s.objekter:
        print(f"tekst: {obj.text}, farge: {obj.farge}")

if __name__ == "__main__":
    main()
