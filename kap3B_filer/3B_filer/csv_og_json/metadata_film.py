import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filnavn = "movies_metadata.csv"

# Lager en dataframe med informasjon
df = pd.read_csv(filnavn, usecols=["runtime","revenue","title", "budget"])

# Lager en array for klassebredde
klassebredde = np.arange(20,250,10)

# Plotte histogram over filmlengde
plt.figure("Filmlengde")
plt.hist(df["runtime"],bins=klassebredde, edgecolor = "white" , color="coral")
plt.grid(axis="y")
plt.xlabel("Minutter")
plt.ylabel("Antall filmer")
plt.title("Oversikt over lengden på 45 tusen filmer")
plt.gca().set_facecolor("lightgray")
plt.xticks(klassebredde,rotation=45)
plt.tight_layout()
# plt.show()

n = 10 #Antall filmer vi vil ha med
y = np.arange(n)
df.sort_values(by=["revenue"], inplace=True, ascending=False)
df["revenue"]=df["revenue"].div(1e9)
df["budget"]=pd.to_numeric(df["budget"], errors='coerce') #Endrer alle elementer til floats
df["budget"]=df["budget"].div(1e9)




# mask = df['budget'].apply(lambda x: isinstance(x, str))
# df = df[~mask]  # Keep rows where column does not contain strings

df["profitt"]=df["revenue"]-df["budget"]

plt.figure("Penger tjent", figsize=(10,7))
plt.barh(y+0.3, df["revenue"][:n], color="seagreen", edgecolor="gray",label="Inntjening", height=0.2)
plt.barh(y, df["budget"][:n], color="red", edgecolor="gray",label="Budsjett", height=0.2)
plt.barh(y-0.3, df["profitt"][:n], color="skyblue", edgecolor="gray",label="Profitt", height=0.2)
plt.title(f"Oversikt over de {n} mest innbringende filmene",loc="left")
plt.legend(loc="best")
plt.yticks(y,df["title"][:n])
plt.subplots_adjust(0.4)
plt.grid(axis="x")
plt.xlabel("Milliarder Dollar")
plt.gca().set_facecolor("lightgray")



plt.show()