import pygame as pg
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

from pg_meny import Knapp, Nedtrekksliste
from pg_meny import MENYFARGE, HOVERFARGE

# Sett Matplotlib til ikke-interaktiv modus med 'Agg' som backend
matplotlib.use('Agg')

# Farger
BAKGRUNNSFARGE = (255, 255, 255)
MORK_GRA = (169, 169, 169)
LYS_GRA = (211, 211, 211)
BLA = (0, 120, 215)

# Definerer et vindu
VINDU_BREDDE = 800
VINDU_HOYDE = 600

# Definerer menyfeltet til høyre i vinduet
MENY_XSTART = 600
MENY_YSTART = 20
MENY_YAVSTAND = 60  # y-avstand for hvert element

VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Initialiserer/starter pygame
pg.init()

# Data
stortingsrepresentanter = [
    {"årstall": 2021, "representanter": {"AP": 48, "FrP": 21, "H": 36,
                                         "KrF": 3, "MDG": 3, "R": 8, "Sp": 28, "SV": 13, "V": 8, "PF": 1}},
    {"årstall": 2017, "representanter": {"AP": 49, "FrP": 27, "H": 45,
                                         "KrF": 8, "MDG": 1, "R": 1, "Sp": 19, "SV": 11, "V": 8, "PF": 0}}
]

# Funksjon som konverterer PyGame-farge (0-255) til Matplotlib-farge (0-1)


def pygameTilMatplotlibFarge(pygame_farge):
  return tuple([x / 255 for x in pygame_farge])

# Funksjon tegner opp valgt diagram for valgt årstall


def tegnMatplotlibDiagram(aarstall, diagramtype):
  # Tabell
  if diagramtype == "Tabell":
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig, axs = plt.subplots(1, 1)

    merkelapper = []
    antall = []

    # Henter aktuelle data
    for rep in stortingsrepresentanter:
      aar = rep["årstall"]

      if aar == int(aarstall):
        for parti in rep["representanter"]:
          merkelapper.append(parti)
          antall.append(rep["representanter"][parti])

    axs.axis('off')

    data = [antall, antall]

    # Juster fontstørrelse, cellepolstring, kantfarge og kanttykkelse
    tabell = axs.table(cellText=data, colLabels=merkelapper,
                       loc="top", cellLoc="center")
    tabell.auto_set_font_size(False)
    tabell.set_fontsize(16)
    tabell.scale(1, 2)  # Øk høyden på cellene

    # Juster kantene for å gjøre det mer leselig
    for key, celle in tabell.get_celld().items():
      celle.set_edgecolor("black")
      celle.set_linewidth(2)
      celle.set_text_props(ha="center", va="center")

  # Søylediagram
  elif diagramtype == "Søyle":
    fig, ax = plt.subplots()
    barWidth = 0.35

    merkelapper = []
    antall = []

    # Henter aktuelle data
    for rep in stortingsrepresentanter:
      aar = rep["årstall"]

      if aar == int(aarstall):
        for parti in rep["representanter"]:
          merkelapper.append(parti)
          antall.append(rep["representanter"][parti])

    x = np.arange(len(merkelapper))
    y = antall
    ax.bar(x, y, barWidth, color=[pygameTilMatplotlibFarge(
        BLA), pygameTilMatplotlibFarge(MORK_GRA)])
    ax.set_xticks(x)
    ax.set_xticklabels(merkelapper)
    ax.set_ylim(0, max(antall) + 20)

  # Sektordiagram
  elif diagramtype == "Sektor":
    merkelapper = []
    antall = []

    # Henter aktuelle data
    for rep in stortingsrepresentanter:
      aar = rep["årstall"]

      if aar == int(aarstall):
        for parti in rep["representanter"]:
          merkelapper.append(parti)
          antall.append(rep["representanter"][parti])

    plt.rcParams["figure.figsize"] = [5.00, 5.00]
    plt.rcParams["figure.autolayout"] = True
    fig, axs = plt.subplots(1, 1)
    plt.pie(antall, labels=merkelapper, textprops={"fontsize": 14})

  # Lagre diagrammet som en bildebuffer
  buf = BytesIO()
  plt.savefig(buf, format="png")
  buf.seek(0)
  plt.close(fig)
  bilde = pg.image.load(buf)

  # Skalerer bildet til å passe til vinduet.
  bilde = pg.transform.scale(bilde, (MENY_XSTART, VINDU_HOYDE))
  return bilde


# En liste med menyelementer
meny = []

# To nedtrekkslister
meny.append(
    Nedtrekksliste(
        MENY_XSTART, MENY_YSTART, ["2017", "2021"]
    )
)

meny.append(
    Nedtrekksliste(
        MENY_XSTART, MENY_YSTART + MENY_YAVSTAND, ["Tabell", "Søyle", "Sektor"]
    )
)

# OK-knapp
meny.append(Knapp(MENY_XSTART, MENY_YSTART + 2*MENY_YAVSTAND, "OK"))

# Funksjon som håndterer museklikk


def museklikk(posisjon):
  global diagramBilde

  for m in meny:
    # Hvis listen er aktiv så vises alternativene. Klikk utenfor deaktiverer listen.
    if isinstance(m, Nedtrekksliste) and m.aktiv:
      m.visAlternativer(posisjon)

    elif m.rektangel.collidepoint(posisjon):
      if isinstance(m, Nedtrekksliste):
        m.visAlternativer(posisjon)
      elif m.tekst == "OK":
        # Oppdater diagrammet basert på de valgte alternativene
        diagramBilde = tegnMatplotlibDiagram(meny[0].tekst, meny[1].tekst)


diagramBilde = None

# Gjenta helt til brukeren lukker vinduet
while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
    if event.type == pg.MOUSEBUTTONDOWN:
      museklikk(event.pos)

  VINDU.fill(BAKGRUNNSFARGE)
  musPos = pg.mouse.get_pos()

  for m in meny:
    if m.rektangel.collidepoint(musPos):
      m.tegn(VINDU, HOVERFARGE)
    else:
      m.tegn(VINDU, MENYFARGE)

  # Tegn diagrammet hvis det finnes
  if diagramBilde:
    VINDU.blit(diagramBilde, (0, 0), pg.Rect(
        0, 0, MENY_XSTART+200, VINDU_HOYDE+100))

  # Tegn de aktive nedtrekkslistene (som viser sine alternativer)
  for m in meny:
    if isinstance(m, Nedtrekksliste) and m.aktiv:
      m.tegn(VINDU, MENYFARGE)

  pg.display.flip()
