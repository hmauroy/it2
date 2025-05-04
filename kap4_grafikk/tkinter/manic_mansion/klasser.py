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

class Spillobjekt:
    def __init__(self,xStart,yStart):
        self.xPosisjon = xStart
        self.yPosisjon = yStart
        self.farge = "grey"
        self.text = "H"
    
    def plassering(self,x,y):
        self.xPosisjon = x
        self.yPosisjon = y

    def flytt(self, dx,dy):
        self.plassering(self.xPosisjon + dx, self.yPosisjon + dy)



class Menneske(Spillobjekt):
    def __init__(self, xStart, yStart,fart):
        super().__init__(xStart, yStart)
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
    def __init__(self, xStart, yStart, xFart, yFart):
        super().__init__(xStart, yStart)
        self.xFart = xFart
        self.yFart = yFart
        self.farge = "darkgrey"
        self.text = "S"
    
    def plassering(self, x, y):
        """Unødvendig metode."""
        super().plassering(x, y)
    
    def endreRetning(self,vegg):
        """Ved kollisjon med en av veggene så skal en akse endre retning."""
        if vegg == "L" or vegg == "R":
            self.xFart = -self.xFart
        elif vegg == "U" or vegg == "D":
         self.yFart = -self.yFart
    
class Hindring(Spillobjekt):
    def __init__(self, xStart, yStart):
        super().__init__(xStart, yStart)

    def plassering(self, x, y):
        """Unødvendig metode."""
        return super().plassering(x, y)

class Sau(Spillobjekt):
    def __init__(self, xStart, yStart):
        super().__init__(xStart, yStart)
        self.blirBåret = False
        self.aktiv = True
        self.farge = "pink"
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

a = Spillobjekt(10,10)
b = Spillobjekt(300,300)
s = Spillebrett(500,500)
s.leggTileObjekt(a)
s.leggTileObjekt(b)
s.fjernObjekt(a)
for obj in s.objekter:
    print(obj.xPosisjon)