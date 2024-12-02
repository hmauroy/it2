"""
Grafikk med tkinter.
Labels er i fokus.
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
    text="ho ho ho!",
    font = ("Comic sans", 50),
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
footer.pack()




# Kjører GUI-tråden
window.mainloop()


