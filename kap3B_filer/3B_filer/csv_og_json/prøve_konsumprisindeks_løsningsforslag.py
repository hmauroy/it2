import pandas as pd
import matplotlib.pyplot as plt

filnavn = "konsumprisindeks.csv"

df = pd.read_csv(filnavn,  decimal=",", delimiter=";",na_values=['.'])
kolonne_navn = df.columns.values
# kolonne_navn = ["År","Årsgj.snitt2","Jan","Feb","Mar","Apr","Mai","Jun","Jul","Aug","Sep","Okt","Nov","Des"]

# Oppgave 1a - Finne minste og største verdi fra dataen

max_verdi = 0
min_verdi = 100
for navn in kolonne_navn[2:]: #Dobbel løkke som kjører gjennom alle månedsverdiene i df-en
    for i,element in enumerate(df[navn]): # Enumerate slår sammen "for i in range()" og "for element in list:". i teller og element henter ut innholdet i listen
        if element>max_verdi:
            max_verdi = element
            max_måned = navn
            max_år = df["År"][i]
        if element<min_verdi:
            min_verdi = element
            min_måned = navn
            min_år = df["År"][i]

print("\nOppgave 1a")
print(f"Konsumprisindeksen var størst i {max_måned} {max_år} og var på {max_verdi}")
print(f"Konsumprisindeksen var minst i {min_måned} {min_år} og var på {min_verdi}")


# Oppgave 1b - Finne størst differanse

differanse = 0
for i, year in enumerate( df["År"][1:],start=1):
    # print(df["Des"][i])
    if df["Des"][i]-df["Jan"][i]>differanse:
        differanse  = df["Des"][i]-df["Jan"][i]
        verdi_jan   = df["Jan"][i]
        verdi_des   = df["Des"][i]
        år          = year
       

print(f"\nOppgave 1b\nDen største differansen mellom Januar og Desember skjedde i {år}\n\
hvor differansen var {differanse:.1f} (Januar:{verdi_jan}  Desember:{verdi_des} )\n")


# Oppgave 2 - Tegne graf

# 2a - Gjennomsnittlig konsumprisindeks per år

df.plot(x="År", y="Årsgj.snitt2", kind="line", legend=False)
plt.ylabel("Konsumprisindeks")
plt.title("Utvikling av årlig gjennomsnitt av konsumprisindeksen")
plt.grid(axis="y")
plt.show()

#2b - Stolpediagram av 2022

values = df.loc[0, kolonne_navn[2:-3]] # Henter ut første (0) rad av månedskolonnene, men ikke de tre siste siden de er uten data
values.plot(kind="bar") 
plt.title("Månedlig utvikning for konsumprisindeksen i 2022")
plt.ylabel("Konsumprisindeks")
plt.show()    


# Oppgave 3 - Kalkulator
print("Oppgave 3 - Kpi-kalkulator\n")

def kpi_kalk(beløp:float, fra_år:float, til_år:float):
    """Funksjon som tar inn parameterne beløp, fra år og til år.
    Leser deretter inn konsumprisindeksen og finner 
    verdier tilhørende de valgte årene.
    Bruker valgt beløp og regner ny pris."""

    # Henter inn df med kun kolonnene "År" og "Årsgj.snitt2",
    # og bruker kolonnen "År" som indeks
    df = pd.read_csv("konsumprisindeks.csv", sep=";",decimal=",",\
                     na_values=".", index_col="År", usecols=["År","Årsgj.snitt2"])
    
    kpi_fra =  float(df.loc[fra_år, "Årsgj.snitt2"])
    kpi_til =  float(df.loc[til_år, "Årsgj.snitt2"])
    nytt_beløp = kpi_til*beløp/kpi_fra # Formelen for å regne om KPI
    return nytt_beløp


def valider_heltall_input(prompt:str):
    """En funksjon som tar in paramenteren 'prompt' 
        og validerer at input er et heltall"""
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            return value
        except ValueError:
            print(f"Feil: '{user_input}' er ikke et heltall. Prøv igjen.")

fra_år  = valider_heltall_input("Fra år [1929-2021] : ")
til_år  = valider_heltall_input("Til år [1929-2021] : ")
beløp   = valider_heltall_input("Beløp              : ")

nytt_beløp = kpi_kalk(beløp, fra_år, til_år)

print(f"{beløp:_} kroner i år {fra_år} er verdt {nytt_beløp:_.1f} kroner i år {til_år}")