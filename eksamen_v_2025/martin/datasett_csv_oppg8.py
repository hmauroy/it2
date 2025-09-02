import pandas as pd
import matplotlib.pyplot as plt

#Oppgave 8a)
filnavn = "friluftsaktiviteter.csv"

df = pd.read_csv(filnavn, sep=";")

kolonne_navn = ["Friluftsaktivitet","Østfold","Akershus","Oslo", 
                "Innlandet","Buskerud","Vestfold","Telemark",
                "Agder","Rogaland","Vestland","Møre og Romsdal",
                "Trøndelag","Nordland","Troms"]
df.columns=kolonne_navn

#Lager en kolonne med totalen på tvers av fylkene
df["Total"] = df.sum(1,numeric_only=True)
print(df.head(15))#Viser data i tabell

#Oppgave 8b) - Valgt fylke i stigende rekkefølge og med prosentandel
#Lager en tekst til inputfunksjonen slik at bruker enkelt kan velge et fylke
valg_string = "\nVelg et fylke:\n(Skriv tallet til fylket du ønsker)\n1 Østfold\n2 Akershus\n3 Oslo\n4 Innlandet\n5 Buskerud\n6 Vestfold\n7 Telemark\n8 Agder\n9 Rogaland\n10 Vestland\n11 Møre og Romsdal\n12 Trøndelag\n13 Nordland\n14 Troms\n"
try:
    valgt_fylke = int(input(valg_string))
except:
    raise ValueError("Du må skrive inn et tall mellom 1-14 for å velge fylke")
fylke = kolonne_navn[valgt_fylke]

#Lager en kopi av dfen kun med informasjon for valgt fylke
df_valgt=df[[fylke]].copy()
df_valgt.index = df[kolonne_navn[0]]


#Lager en kolonne med prosentandel
total_antall = df_valgt[fylke].sum() #Finner summen av antall deltakere
df_valgt["Prosent"]=round(df_valgt[fylke]/total_antall*100,1)

#Sorterer og printer ut verdiene i stigende rekkefølge
sortering = df_valgt.sort_values(by=[fylke])
print(sortering)


#Oppgave 8c) - Stolpediagram

#Finner topp 3
topp_3 = df_valgt.nlargest(3,fylke)

plt.bar(topp_3.index, topp_3[fylke])
plt.title(f"Topp 3 friluftsaktiviteter i {fylke}")
plt.ylabel("Antall deltakere [x1000]")
plt.xlabel("Aktivitet")
plt.xticks(rotation=25) 
plt.tight_layout()
plt.show()
