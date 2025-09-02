import json
import matplotlib.pyplot as plt
import numpy as np

# Hente ned json-filen
filnavn = "lonnstabell.json"

with open(filnavn, "r", encoding="utf-8") as fil:
    data = json.load(fil)

# Lage lister med årstall, lønn for kvinner og lønn for menn
aarstall = data["dataset"]["dimension"]["Tid"]["category"]["label"]
alle_aarstall = list(aarstall.values()) # Henter ut vediene fra ordboka

lonn_kvinner = data["dataset"]["value"][6:]
lonn_menn = data["dataset"]["value"][:6]


# Plotting av gjennomsnittslønn for kvinner og menn
plt.figure("Linjegraf")
plt.plot(alle_aarstall, lonn_kvinner, label = "Kvinner")
plt.plot(alle_aarstall, lonn_menn, label = "Menn")

plt.legend()
plt.xlabel("Årstall")
plt.ylabel("Gjennomsnittslønn [kr]")
plt.title("Utvikling av gjennomsnittslønn")
plt.grid(axis="y")


# Plotting av gruppert stolpediagram
bar_width = 0.35
index = np.arange(len(alle_aarstall))

plt.figure("Stolpediagram")
plt.bar(index, lonn_kvinner, bar_width, label = "Kvinner")
plt.bar(index + bar_width, lonn_menn, bar_width, label = "Menn")
plt.xticks(index + bar_width/2, alle_aarstall)

plt.legend()
plt.xlabel("Årstall")
plt.ylabel("Gjennomsnittslønn [kr]")
plt.title("Utvikling av gjennomsnittslønn")
plt.grid(axis="y")

plt.show()