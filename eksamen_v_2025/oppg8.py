"""
Dataanalyse Eksamen V2025
"""

# a) Les datafil og lagre i egnet datastruktur.
# Regner ut totalt antall personer som har deltatt i hver aktivitet, på tvers av
# alle fylker.
# Programmet skal presentere resultatet i en tabelliknende oppsett som viser
# aktiviteter og totalt antall deltakere for hver aktivitet.

filnavn = "friluftsaktiviteter.csv"

linjer = []

with open(filnavn, encoding="utf-8") as fil:
  for linje in fil:
    linjer.append(linje.rstrip())
    #linjer.append(linje.rstrip())  # Fjerner linjeskift fra filens tekstkoding.
    #linjer.append(linje.rstrip().split(" "))  # Fjern linjeskift og del opp i ord

fylker = linjer[0].split(";")[1:]
for i in range(len(fylker)):
    fylker[i] = fylker[i][22:]
    # skreller vekk slutten av navnet for de tre siste fylkene ved å splitte på mellomrom.
    if "Trønd" in fylker[i] or "Nordland" in fylker[i] or "Troms" in fylker[i]:
       skille = fylker[i].index(" - ")
       fylker[i] = fylker[i][0:skille]
print()

# Datastrukturen
data = {
  "fylker": fylker,
  "kategorier": []
}

# Leser ut overskrifter og henter ut data
kategorier = []

for i in range(1,len(linjer)):
   buf = linjer[i].split(";")
   data["kategorier"].append(buf[0])
   kategori = buf[0]
   verdier = buf[1:]
   for j in range(len(verdier)):
      verdier[j] = int(verdier[j])
   data[kategori]=verdier



# Regner ut antall for hver aktivitet og skriver ut som tabell.
for kategori in data["kategorier"]:
   lengde = len(kategori)
   mellomrom = " " * (60-lengde)
   print(f"{kategori} {mellomrom} {sum(data[kategori])}")


