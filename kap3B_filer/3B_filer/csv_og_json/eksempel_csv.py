import matplotlib.pyplot as plt
import pandas as pd

# Opprett en variabel med navn på filen du skal bruke
filnavn = "konsumprisindeks.csv"

# Noen datafiler har encoding som ikke er "vanlig". Prøv å lese ved å bruke utf-8 først, 
# deretter flere nordiske encodinger.
encodings = ["utf-8","utf-8-sig", "iso-8859-1", "latin1"]
for encoding in encodings:
    try:
        df = pd.read_csv(filnavn, header=0, delimiter=";") # Header betyr hvor mange linjer som skal skippes.
        break
    except Exception as e:  # or the error you receive
        print("Feil med innlesing: " + e)


# For å hente ut informasjon fra én kolonne: df["Navn_på_kolonne"]

# Plotter dataene plt.plot(x,y)
plt.plot(df["År"], df["Årsgj.snitt2"])
plt.show()

# Sorterer dataene
df.sort_values(by="År", ascending=True)

# Skriver sorterte data til ny fil
df.to_csv("ny_fil.csv", index=True)


