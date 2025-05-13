"""
Dataanalyse Eksamen V2025
"""
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
    # Plukker ut fylket etter all tulletekst.
    fylker[i] = fylker[i][23:]
    # skreller vekk slutten av navnet for de tre siste fylkene ved å splitte på mellomrom.
    if "Trønd" in fylker[i] or "Nordland" in fylker[i] or "Troms" in fylker[i]:
       skille = fylker[i].index(" - ")
       fylker[i] = fylker[i][0:skille]

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



# Regner ut antall for hver aktivitet og skriver ut som tabell. Huske å gange med 1000
print(f'Kategori {" " * (60-len("Kategori"))} antall personer')
for kategori in data["kategorier"]:
    lengde = len(kategori)
    mellomrom = " " * (71-lengde)
    print(f"{kategori} {mellomrom} {sum(data[kategori])}")


# b) Utvid så bruker kan angi fylke.
# Programmet skal deretter vise alle aktivitetene for det valgte fylket i stigende rekkefølge, 
# både som antall og som prosentandel.
def finnVerdier(fylke) -> dict:
    indeks = data["fylker"].index(fylke)
    verdier = {}
    # Går gjennom dataene og henter ut verdier.
    for kategori in data["kategorier"]:
       # Plukker ut på indeksen til fylket fra listen av data.
       verdi = data[kategori][indeks] 
       verdier[kategori] = verdi*1000
    return verdier  # {"Sykkeltur": 151, "Fisket": 143, ...}

def sorterVerdi(verdier,):
   return dict(sorted(verdier.items(), key=lambda item: item[1], reverse=False))

def sorterProsent(verdier):
    totalsum = 0
    for key,val in verdier.items():
        totalsum += val
    prosentandeler = {}
    for kategori,val in verdier.items():
        prosentandeler[kategori] = val/totalsum * 100
    return dict(sorted(prosentandeler.items(), key=lambda item: item[1], reverse=False))

def visTabellFylke(ordbok,fylke,overskrift,heltall=True):
    print()
    print()
    print(f"Antall personer per aktivitet for {fylke} fylke sortert i stigende rekkefølge.")
    print(f'Kategori {" " * (50-len("Kategori"))} {overskrift}')
    for kategori,val in ordbok.items():
        lengde = len(kategori)
        mellomrom = " " * (60-lengde)
        if heltall:
            print(f"{kategori} {mellomrom} {val}")
        else:
            print(f"{kategori} {mellomrom} {val:.1f}")

def finnMestPopulære(sortert) -> tuple:
    teller = 1
    revers = dict(sorted(sortert.items(), key=lambda item: item[1], reverse=True))
    x = []
    y = []
    # Går gjennom ordboken og plukker ut de tre første elementene.
    for kategori,verdi in revers.items():
        x.append(kategori)
        y.append(verdi)
        teller += 1
        if teller > 3:
            # Hopper ut av loopen når de tre første er hentet ut.
            break
    return x,y


def plot_bar_chart(chart_frame,categories,values,fylke,prosent=False):
    # Clear any existing chart in the frame
    for widget in chart_frame.winfo_children():
        widget.destroy()

    # Create a matplotlib figure
    fig = Figure(figsize=(20, 8), dpi=60)
    ax = fig.add_subplot(111)

    # Plot bar chart
    ax.bar(categories, values, color="skyblue")

    # Add titles and labels
    ax.set_title(f"De tre mest populære aktivitetene for {fylke} fylke ")
    ax.set_xlabel("Kategorier")
    if prosent:
        ax.set_ylabel("Prosentvis antall personer")
    else:
        ax.set_ylabel("Antall personer")

    # Embed the plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def visMeny():
    teller = 1
    for fylke in data["fylker"]:
        print(f"{teller}. {fylke}")
        teller += 1

def main():
    visMeny()
    antall = len(fylker)
    fylkeindeks = int(input(f"Hvilket fylke 1-{antall}? ")) # Antar at bruker skriver tall.
    fylke = fylker[fylkeindeks - 1]
    #fylke = "Oslo"
    verdier = finnVerdier(fylke)
    # Sorter etter verdi
    sortert = sorterVerdi(verdier)
    visTabellFylke(sortert,fylke,"antall personer")
    # Sorter etter prosentandel
    prosentandeler = sorterProsent(verdier)
    visTabellFylke(prosentandeler,fylke,"antall personer (%)",False)

    # c) Utvid så man kan finne de tre mest populære aktivitetene for et valgt fylke
    # og presentere dem i et stolpediagram.
    x,y = finnMestPopulære(sortert)

    x_pros,y_pros = finnMestPopulære(prosentandeler)

    # Main Tkinter window
    root = tk.Tk()
    root.title("Tkinter Bar Chart Example")
    root.geometry("800x600")

    # Button to trigger the bar chart plot
    plot_button = ttk.Button(root, text="Vis verdier", command=lambda: plot_bar_chart(chart_frame,x,y,fylke))
    plot_button.pack(pady=10)

    plot_button = ttk.Button(root, text="Vis prosentvis", command=lambda: plot_bar_chart(chart_frame,x_pros,y_pros,fylke,prosent=True))
    plot_button.pack(pady=10)

    # Frame to hold the chart
    chart_frame = tk.Frame(root)
    chart_frame.pack(fill=tk.BOTH, expand=True)

    #plot_bar_chart(chart_frame,x,y,fylke)

    # Start the Tkinter event loop
    root.mainloop()





if __name__ == "__main__":
   main()