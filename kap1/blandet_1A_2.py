"""
Volum av flaske. Ønsker 500 cm^2
Volum består av 
kjegle
sylinder
halvkule
"""
from math import pi
r = 3  # cm
h_k = 7.005 # cm
h_s = 13.35 # cm

v_k = pi * r**2 * h_k/3 # volum kjegle
v_s = pi * r**2 * h_s   # volum sylinder
v_kule = 4/3 * pi * r**3    # volum kule

v_total = v_k + v_s + v_kule/2

print(f"Volum er {v_total:.2f}.")

