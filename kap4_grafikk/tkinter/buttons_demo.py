"""
Grafikk med tkinter.
Labels er i fokus.
"""
import tkinter as tk
window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)    # Setter vinduets størrelse ved oppstart.
window.configure(background="blue")

# 1) Lager første vindu en "Frame"
header = tk.Frame(window)
header.configure(
    background="green",
    height=100,
    width=bredde,
)
header.pack()

#help(tk.Frame)

hovedvindu = tk.Frame(window)
hovedvindu.configure(
    background="green",
    height=350,
    width=bredde,
    borderwidth="5",

)
hovedvindu.pack()

# Legger et vindu inni et annet
innervindu = tk.Frame(hovedvindu)
innervindu.configure(
    background="red",
    height=100,
    width=bredde*0.8,
    highlightbackground="white",
    highlightthickness="5"
)
hovedvindu.pack_propagate(False) # Skrur av at children kan endre rammen.


innervindu.pack()

# Lager en usynlig boks som presser teksten lenger ned
usynlig_boks = tk.Frame(innervindu)
usynlig_boks.configure(
    height="10",
    background="red",
)
usynlig_boks.pack()

# Legger til litt tekst med Label-klassen.
hohoho = tk.Label(innervindu)
hohoho.configure(
    text="ho ho ho!",
    font = ("Comic sans", 50),
    foreground="white",
    background="red",
)

hohoho.pack()
innervindu.pack_propagate(False)


footer = tk.Frame(window)
footer.configure(
    background="white",
    height=50,
    width=bredde,
)
footer.pack()

# Legger til knapper
footer.pack_propagate(False)
avslutt = tk.Button(footer, text="Avslutt")
avslutt.pack()

knapp_ok = tk.Button(hovedvindu, text="OK")
knapp_ok.pack()


# Funksjoner for knappene
teller = 0
def handle_avslutt(eventet):
    """Avslutter hele programmet og vinduet."""
    window.destroy()

def handle_ok(eventet):
    """Endrer teksten på knappen."""
    global teller
    print(eventet)
    knapp_ok["text"] = f"{teller}"
    teller += 1


# Binder knapper til funksjoner
avslutt.bind("<Button-1>", handle_avslutt)
knapp_ok.bind("<Button-1>", handle_ok)





# Kjører GUI-tråden
window.mainloop()


