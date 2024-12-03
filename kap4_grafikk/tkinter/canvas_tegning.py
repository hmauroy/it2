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

# 1) Lager en ramme der canvas skal ligge inni
hovedvindu = tk.Frame(window)
hovedvindu.configure(
    background="red",
    height= hoyde,
    width= 0.9 * bredde,
    highlightbackground="white",
    highlightthickness=5, # border-width
)
hovedvindu.pack()

hovedvindu.pack_propagate(False) # Skrur av at children kan endre rammen.

# 2) Lager canvas der tegningene skal komme opp.
canvas = tk.Canvas(
    hovedvindu, 
    width=350, 
    height=350, 
    background="#00873E",
    highlightbackground="white",
    highlightthickness=5, # border-width,
    )
canvas.pack(expand=True) # expand midtstiller inni mor-vinduet.

footer = tk.Frame(window)
footer.configure(
    background="white",
    height=50,
    width=bredde,
)
footer.pack_propagate(False)
footer.pack()

#---------------------  Slutt på GUI definisjonene -----------------------

# Tegning med canvas
# I) Lager en sirkel med fyll.
x = 50
y = 100
R = 20
canvas.create_oval(x-R, y-R, x+R, y+R,
                    fill="red", 
                    outline="white", 
                    width=3,    # Bredde på omriss
                    tags="sirkel")

# II) Lager et rektangel med fyll.
L = 50
H = 30
x2 = 200
y2 = 300
canvas.create_rectangle(x2-L/2, y2-H/2, x2+L/2, y2+H/2,
                    fill="blue", 
                    outline="red", 
                    width=6,    # Bredde på omriss
                    tags="rektangel")


# A) Lager knapper
avslutt_knapp = tk.Button(footer, text="Avslutt")
avslutt_knapp.pack()

# B) Lager funksjonene til knappene
def avslutt(eventet):
    """Avslutter vinduet og programmet."""
    window.destroy()


# C) Binder knapper til funksjoner
avslutt_knapp.bind("<Button-1>", avslutt)


# Kjører GUI-tråden
window.mainloop()


