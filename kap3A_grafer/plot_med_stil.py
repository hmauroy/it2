import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)   # Lager matematisk array (vektor)
yverdier = xverdier**2              # Utfører matematisk operasjon på hele arrayet på én gang.

# Skriver ut en oversikt over tilgjengelige stiler
print(plt.style.available)

# Angir at vi vil bruke stilen "dark_background"
plt.style.use("dark_background")

plt.plot(xverdier, yverdier, color="salmon")

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(0, 20)
plt.ylim(0, 400)

plt.show()
