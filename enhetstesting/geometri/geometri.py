"""
Ulike formler som beregner areal og volum.
"""

import math


def rektangel_areal(bredde, høyde):
    """Beregner arealet av et rektangel."""
    return bredde * høyde


def sirkel_areal(radius):
    """Beregner arealet av en sirkel."""
    return math.pi * radius ** 2


def trekant_areal(bredde, høyde):
    """Beregner arealet av en trekant."""
    return (bredde * høyde) / 2


def kube_volum(sidelengde):
    """Beregner volumet av en kube."""
    return sidelengde ** 3


def sylinder_volum(radius, høyde):
    """Beregner volumet av en sylinder."""
    return math.pi * radius ** 2 * høyde


def kule_volum(radius):
    """Beregner volumet av en kule."""
    return (4/3) * math.pi * radius ** 3
