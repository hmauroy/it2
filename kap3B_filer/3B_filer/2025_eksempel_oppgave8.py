"""
Oppgavetekst:
Du skal lage et program som leser inn og presenterer informasjon fra et datasett. 
Du skal bruke det vedlagte datasettet.
 
Tips: Du står fritt til å velge hvordan programmet skal presentere informasjon, 
så lenge presentasjonen er godt egnet til å vise det oppgaven spør etter. 
Du kan også velge om du vil besvare a og b i en samlet oversikt eller lage 
en oversikt for hvert oppgavepunkt.

Programmet du lager i denne oppgaven, skal inneholde en flerlinjekommentar øverst som beskriver de 
vurderingene og valgene du har gjort for å forberede datasettet til bruk i programmering, 
hvis du har gjort det.

a) Lag et program som presenterer data fra datasettet i en tabellignende visning med 
    kolonnene «fødselstall», «innflyttinger» og «utflyttinger».

b) Utvid programmet ved å legge til kolonnen «netto folkevekst» i visningen. 
    Feltene i denne skal være beregnet ut ifra de tre andre.

Formelen for netto folkevekst er:
netto folkevekst = fødselstall + innflyttinger - utflyttinger
 
c) Utvid programmet til å vise et egnet diagram som viser utviklingen for 
«netto folkevekst» for en valgfri periode mellom 1945 og 2024.  
    Man skal kunne velge start- og sluttår i brukergrensesnittet.
"""

"""
Valg jeg har gjort med datasettet:
- endret ? til å og ø i kolonnenavnene
- endret kolonnenavnet 'levendefødte i alt' til 'fødselstall' ¨
"""

import pandas as pd
import matplotlib.pyplot as plt

filnavn = "2025_Datasett_fodselstall.csv"

df = pd.read_csv(filnavn, sep="\t",na_values="..", index_col="År")

print(df.to_string())

print(df.dtypes)


df["Netto folkevekst"] = df["Fødselstall"] + df["Innflyttinger"] - df["Utflyttinger"]

print(df.to_string())


år_start = int(input("Skriv inn startårstall [1945-2024]"))
år_slutt = int(input("Skriv inn sluttårstall [1945-2024]"))
år_start = år_start - 1945
år_slutt = år_slutt - 1945 + 1


df["Netto folkevekst"][år_start:år_slutt].plot()
plt.show()


