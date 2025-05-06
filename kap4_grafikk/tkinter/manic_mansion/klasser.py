"""
klasser for spillet Manic Mansion.
Implementert fra UML-klassediagrammet fra Eksamen Høst 2023.

Henrik Mauroy
hmauroy@gmail.com
"""

from random import randrange

class Spillebrett:
    def __init__(self,h,b,canvas,brikkebredde):
        self.høyde = h
        self.bredde = b
        self.objekter = []
        self.canvas = canvas
        self.brikkebredde = brikkebredde
    
    def leggTilObjekt(self, objekt):
        self.objekter.append(objekt)
    
    def fjernObjekt(self, objekt):
        """ Fjerner et unikt objekt fra listen objekter"""
        if objekt in self.objekter:
            self.objekter.remove(objekt)
            return True
        else:
            return False
    
    def friPlass(self, type):
        freePos = False
        while freePos == False:
            x,y = self.tilfeldigPos(type)
            # Søker gjennom objektene og leter etter like koordinater for samme type.
            for obj in self.objekter:
                if obj.text == type:
                    if (obj.xPosisjon - self.brikkebredde/2 <= x <= obj.xPosisjon + self.brikkebredde/2  and 
                    obj.yPosisjon - self.brikkebredde/2 <= y <= obj.yPosisjon + self.brikkebredde/2):
                        print("Opptatt posisjon")
            freePos = True
        return x,y

    def lagSpøkelse(self):
        x,y = self.friPlass("S")
        xFart = randrange(1,5)
        yFart = randrange(1,5)
        s = Spøkelse(x,y,self.brikkebredde,xFart,yFart,[100,0,self.bredde-100,self.høyde])
        self.objekter.append(s)

    def lagSau(self):
        x,y = self.friPlass("BÆ")
        sau = Sau(x,y,self.brikkebredde)
        self.objekter.append(sau)
                    
    def lagHindring(self):
        x,y = self.friPlass("H")
        hindring = Hindring(x,y,self.brikkebredde)
        self.objekter.append(hindring)

    def tegnAlleObjekt(self):
        """Går gjennom alle objekter og tegner dem."""
        # Sletter alle objekter fra canvas før tegning på nytt
        for obj in self.objekter:
            if obj.text == "M" or obj.text == "S":
                self.canvas.delete(obj.id)
        for objekt in self.objekter:
            # Må sjekke om det er sau og at den skal tegnes opp
            if objekt.text == "BÆ" and objekt.blirBåret == True:
                continue
            self.canvas.create_rectangle(
                objekt.xPosisjon - objekt.bredde/2,
                objekt.yPosisjon - objekt.bredde/2,
                objekt.xPosisjon + objekt.bredde/2,
                objekt.yPosisjon + objekt.bredde/2,
                fill=objekt.farge,
                outline=objekt.farge,
                width=1,
                tags = objekt.id
            )
            self.canvas.create_text(objekt.xPosisjon, objekt.yPosisjon, text=objekt.text, font=("Arial", 14), fill="black", tags=objekt.id)

    def oppdater(self, retning):
        """Oppdaterer alt
        1) 
        2) Sjekk for kollisjon mellom objekter eller vegger.
        
        5) Dersom avslutning eller game over returneres False, ellers True.
        """
        # 1) Flytt alle objekt og sjekk for kollisjoner.
        for obj in self.objekter:
            if obj.text == "M":
                obj.beveg(obj.fart,retning)
                # 2) Sjekk om menneske er tilbake i venstre frisone, da skal sau slippes løs.
                if obj.xPosisjon <= 80 and obj.bærerSau == True:
                    obj.poeng += 1
                    obj.bærerSau = False
                    obj.okFart(5)
                    obj.sau.fjernSau()  # Kan ikke plukkes opp igjen.
                    obj.sau.blirBåret = False
                    obj.sau.xPosisjon = obj.xPosisjon
                    obj.sau.yPosisjon = obj.yPosisjon
                    self.lagSau()
                    self.lagSpøkelse()
                    self.lagHindring()
                # 3) Håndterer kollisjoner ved å sjekke med alle andre objekter for kollisjon.
                for objekt2 in self.objekter:
                    if obj.text != objekt2.text:
                        kollisjon = obj.sjekkKollisjon(objekt2)
                        if kollisjon:
                            self.tegnAlleObjekt()
                            if objekt2.text == "S" or objekt2.text == "H":
                                print("Spiller tapte :(")
                                return False
                            elif objekt2.text == "BÆ" and obj.bærerSau == False:
                                if objekt2.aktiv == True:
                                    objekt2.blirBåret = True
                                    obj.bærerSau = True
                                    obj.reduserFart(5)
                                    obj.sau = objekt2   # Legger sau-objektet inni menneskeobjektet.
            if obj.text == "S":
                obj.flytt(obj.xFart,obj.yFart)
                obj.endreRetning()
        
        # 4) Tegn alle objekt fra canvas med nye posisjoner
        self.tegnAlleObjekt()
        return True
    
    def tilfeldigPos(self,type):
        """Genererer tilfeldig koordinat i forhold til hvor på brettet objektene skal starte."""
        boundingbox = [] # [x1,y1, x2,y2]
        if type == "M":
            boundingbox = [self.brikkebredde,self.brikkebredde,100-self.brikkebredde, self.høyde-self.brikkebredde]
        elif type == "S" or type == "H":
            boundingbox = [100 + self.brikkebredde,self.brikkebredde,self.bredde-100-self.brikkebredde, self.høyde-self.brikkebredde]
        elif type == "BÆ":
            boundingbox = [self.bredde-100+self.brikkebredde,self.brikkebredde,self.bredde-self.brikkebredde, self.høyde-self.brikkebredde]
        x = randrange(boundingbox[0],boundingbox[2])
        y = randrange(boundingbox[1],boundingbox[3])
        return x,y


class Spillobjekt:
    teller = 0
    def __init__(self,xStart,yStart,bredde):
        self.xPosisjon = xStart
        self.yPosisjon = yStart
        self.farge = "grey"
        self.text = "H"
        self.bredde = bredde
        #self.id = f"{Spillobjekt.teller}"
        self.id = "brikke"
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
        self.sau = None # Kan holde på en sau.
    
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
            self.fart = 1
    
    def okFart(self, okning):
        self.fart += okning
    
    def økPoeng(self, antall):
        self.poeng += antall
    
    def bærSau(self, sauobjekt):
        if self.bærerSau:
            return False
        else:
            self.bærerSau = True
            return True
    
    def sjekkKollisjon(self,objekt2):
        """Sjekker for kollisjon med alle andre objekter"""
        # Sjekker for om det IKKE er overlapp med det andre objektet
        # Returnerer motsatt boolean verdi.
        if (self.xPosisjon + self.bredde / 2 <= objekt2.xPosisjon - objekt2.bredde / 2 or  # this right edge is left of objekt2's left edge
            self.xPosisjon - self.bredde / 2 >= objekt2.xPosisjon + objekt2.bredde / 2 or  # this left edge is right of objekt2's right edge
            self.yPosisjon + self.bredde / 2 <= objekt2.yPosisjon - objekt2.bredde / 2 or  # this bottom edge is above objekt2's top edge
            self.yPosisjon - self.bredde / 2 >= objekt2.yPosisjon + objekt2.bredde / 2):  # this top edge is below other's bottom edge
            return False
        return True


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
        """Ved kollisjon med en av veggene så skal en akse endre retning.
        self.bb = [x1,y1,x2,y2] setter grensene til hvor spøkelset kan bevege seg.
        """
        if self.xPosisjon <= self.bb[0]:    # venstre vegg
            self.xPosisjon = self.bb[0] + self.bredde/2  # flytter inn på brettet hvis utenfor.
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
