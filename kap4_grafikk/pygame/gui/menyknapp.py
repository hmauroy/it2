import pygame as pg
from pg_meny import Knapp
from pg_meny import MENYFARGE, HOVERFARGE

# Farge
BAKGRUNNSFARGE = (255, 255, 255)

# Definerer et vindu
VINDU_BREDDE = 600
VINDU_HOYDE = 400

# Definerer menyfeltet til høyre i vinduet
MENY_XSTART = 400
MENY_YSTART = 20
MENY_YAVSTAND = 60  # y-avstand for hver knapp

VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Initialiserer/starter pygame
pg.init()

# Funksjon som håndterer museklikk


def museklikk(posisjon):
    for m in meny:
        if m.rektangel.collidepoint(posisjon):
            print(f"Klikket på: {m.tekst}")


# En liste med menyelementer
meny = []

# Lager en knapp
meny.append(Knapp(MENY_XSTART, MENY_YSTART, "Første knapp"))

# Lager en knapp til
# meny.append(Knapp(MENY_XSTART, MENY_YSTART + MENY_YAVSTAND, "Neste knapp"))

# Lager en knapp til
# meny.append(Knapp(MENY_XSTART, MENY_YSTART + 2 * MENY_YAVSTAND, "Tredje knapp"))

# Gjenta helt til brukeren lukker vinduet
fortsett = True

while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        if event.type == pg.MOUSEBUTTONDOWN:
            museklikk(event.pos)

    VINDU.fill(BAKGRUNNSFARGE)
    muspos = pg.mouse.get_pos()

    for m in meny:
        if m.rektangel.collidepoint(muspos):
            m.tegn(VINDU, HOVERFARGE)
        else:
            m.tegn(VINDU, MENYFARGE)

    pg.display.flip()

pg.quit()
