import pygame as pg

# Farger
TEKSTFARGE = (255, 255, 255)
MENYFARGE = (0, 0, 255)
HOVERFARGE = (0, 150, 255)

# Nedtrekksmeny
NEDTREKKS_BREDDE, NEDTREKKS_HOYDE = 200, 50

# Menyfelt
# MENYFELT_START = 400
# MENYFELT_BREDDE = 200

# Initialiserer/starter pygame
pg.init()

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Tahoma", 24)


class Knapp:
    """Klasse for å representere en knapp"""

    def __init__(self, xPosisjon, yPosisjon, tekst):
        self.xPosisjon = xPosisjon
        self.yPosisjon = yPosisjon
        self.bredde = len(tekst) * 14 + 20
        self.hoyde = 40
        self.tekst = tekst
        self.rektangel = pg.Rect(
            self.xPosisjon, self.yPosisjon, self.bredde, self.hoyde
        )

    def tegn(self, vindu, farge):
        pg.draw.rect(vindu, farge, self.rektangel)
        tekst = font.render(self.tekst, True, TEKSTFARGE)
        tekstRamme = tekst.get_rect(center=self.rektangel.center)
        vindu.blit(tekst, tekstRamme.topleft)


class Nedtrekksliste:
    def __init__(self, xPosisjon, yPosisjon, alternativer):
        self.xPosisjon = xPosisjon
        self.yPosisjon = yPosisjon
        self.alternativer = alternativer
        self.aktiv = False
        self.tekst = alternativer[0]
        self.bredde = self.lengsteTekst() * 14
        self.hoyde = 40
        self.rektangel = pg.Rect(
            self.xPosisjon, self.yPosisjon, self.bredde + 10, self.hoyde
        )

    def lengsteTekst(self):
        # Returnerer lengden til det lengste alternativet
        lengst = 0
        for alternativ in self.alternativer:
            if len(alternativ) > lengst:
                # Legger til litt pga forskyvning
                lengst = len(alternativ) + 3
        return lengst

    def tegn(self, vindu, farge):
        pg.draw.rect(vindu, farge, self.rektangel)
        rekt = self.rektangel
        tekst = font.render(self.tekst, True, TEKSTFARGE)
        tekstRamme = tekst.get_rect(center=self.rektangel.center)
        tekstRamme.left = rekt.left + 10  # Venstrejusterer teksten
        tekstRamme.centery = rekt.centery  # Sentraliserer teksten vertikalt
        vindu.blit(tekst, tekstRamme.topleft)

        if self.aktiv:
            i = 0
            for alternativ in self.alternativer:
                rekt = self.alternativRamme(i)
                pg.draw.rect(vindu, HOVERFARGE, rekt)
                tekst = font.render(alternativ, True, TEKSTFARGE)
                tekstRamme = tekst.get_rect(center=rekt.center)
                tekstRamme.left = rekt.left + 10  # Venstrejusterer teksten
                tekstRamme.centery = rekt.centery  # Sentraliserer teksten vertikalt
                vindu.blit(tekst, tekstRamme.topleft)
                i += 1

    def alternativRamme(self, i):
        return pg.Rect(
            self.xPosisjon + 10,
            self.yPosisjon + (i + 1) * self.hoyde,
            self.bredde,
            self.hoyde
        )

    def visAlternativer(self, pos):
        if self.rektangel.collidepoint(pos):
            self.aktiv = not self.aktiv
        elif self.aktiv:
            i = 0
            while i < len(self.alternativer):
                if self.alternativRamme(i).collidepoint(pos):
                    self.tekst = self.alternativer[i]
                    print(f"Valgt alternativ: {self.tekst}")
                    self.aktiv = False
                    break
                i += 1
        else:
            self.aktiv = False
            # Klikk utenfor alternativer deaktiverer nedtrekkslisten
