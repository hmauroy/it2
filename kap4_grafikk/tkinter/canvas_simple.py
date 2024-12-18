"""
Grafikk med tkinter.
Knapper er i fokus!
"""
import tkinter as tk
window = tk.Tk()
bredde = 500
hoyde = 600
window.minsize(bredde,hoyde)    # Setter vinduets størrelse ved oppstart.
window.configure(background="#00873E")
window.title("Canvas-tegning")

# 1) Lager canvas der tegningene skal komme opp.
canvas = tk.Canvas(
    window, 
    width=bredde, 
    height=0.9 * hoyde, 
    background="#235E6F",
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
                    fill="black", 
                    outline="white", 
                    width=3,    # Bredde på omriss
                    tags="sirkel")

# II) Lager et rektangel med fyll.
L = 50
H = 30
x2 = 200
y2 = 300
canvas.create_rectangle(x2-L/2, y2-H/2, x2+L/2, y2+H/2,
                    fill="white", 
                    outline="black", 
                    width=6,    # Bredde på omriss
                    tags="rektangel")

# III) Lager en arc

# IV) Lager en blomst som består av flere sirkler


# A) Lager knapper
avslutt_knapp = tk.Button(footer, text="Avslutt", command=lambda: avslutt())
avslutt_knapp.pack()

# B) Lager funksjonene til knappene
def avslutt():
    """Avslutter vinduet og programmet."""
    window.destroy()



# Kjører GUI-tråden
window.mainloop()


