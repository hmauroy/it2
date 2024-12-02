"""
Grafikk med tkinter.
Knapper er i fokus!
"""
import tkinter as tk
window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)    # Setter vinduets størrelse ved oppstart.
window.configure(background="#00873E")

# 1) Lager første vindu en "Frame"
header = tk.Frame(window)
header.configure(
    background="#00873E",
    height=100,
    width=bredde,
)
header.pack()

hovedvindu = tk.Frame(window)
hovedvindu.configure(
    background="#00873E",
    height=350,
    width=bredde,
)
hovedvindu.pack()

# Legger et vindu inni et annet
innervindu = tk.Frame(hovedvindu)
innervindu.configure(
    background="red",
    height=100,
    width=bredde*0.8,
    highlightbackground="white",
    highlightthickness=5, # border-width
)
hovedvindu.pack_propagate(False) # Skrur av at children kan endre rammen.


innervindu.pack()

# Lager en usynlig boks som presser teksten lenger ned
usynlig_boks = tk.Frame(innervindu)
usynlig_boks.configure(
    height=10,
    background="red"
)
usynlig_boks.pack()

# Legger til litt tekst med Label-klassen.
hohoho = tk.Label(innervindu)
hohoho.configure(
    text="Ønskeliste",
    font = ("Comic sans MS", 50),
    foreground="white",
    background="red"
)

hohoho.pack()
innervindu.pack_propagate(False)

footer = tk.Frame(window)
footer.configure(
    background="white",
    height=50,
    width=bredde,
)
footer.pack_propagate(False)
footer.pack()

#---------------------  Slutt på GUI definisjonene -----------------------


# I) Lager entry-felt
entry1 = tk.Entry(hovedvindu)
entry1.configure(
    width=50,
    font=("Comic sans MS", 10),
)
entry1.pack()

# A) Lager knapper
avslutt_knapp = tk.Button(footer, text="Avslutt")
avslutt_knapp.pack()

knapp_ok = tk.Button(hovedvindu, text="legg_til")
knapp_ok.pack()

# II) Legger inn Label for å skrive ut ønskelisten
liste = tk.Label(hovedvindu,text="Ønskelisten kommer her...")
liste.configure(
    font=("Comic sans MS", 15),
    background="#00873E",
    foreground="white"
)
liste.pack()

# B) Lager funksjonene til knappene
def avslutt(eventet):
    """Avslutter vinduet og programmet."""
    window.destroy()

onskeliste = ""
def handle_knapp_ok(evt):
    """Lese av entryfeltet"""
    global onskeliste
    tekst = entry1.get()
    print(tekst)
    onskeliste += "- " + tekst + "\n"
    liste["text"] = onskeliste

    
    

# C) Binder knapper til funksjoner
avslutt_knapp.bind("<Button-1>", avslutt)
knapp_ok.bind("<Button-1>", handle_knapp_ok)


# Kjører GUI-tråden
window.mainloop()


