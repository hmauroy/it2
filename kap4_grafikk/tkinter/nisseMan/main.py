"""
Grafikk med tkinter.
Knapper er i fokus!
"""
import tkinter as tk
from nisse import *
import time



window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde, hoyde)    # Setter vinduets størrelse ved oppstart.
window.configure(background="#00873E")


canvas = tk.Canvas(window)
canvas.configure(
    width=bredde,
    height=hoyde,
    background="#00873E"
)
canvas.pack(expand=True)




footer = tk.Frame(window)
footer.configure(
    background="white",
    height=50,
    width=bredde,
)
footer.pack_propagate(False)
footer.pack()

# ---------------------  Slutt på GUI definisjonene -----------------------


# Lager nisse-objekt
nisse = Nisse()
canvas.create_image(nisse.x, nisse.y, image=nisse.bilde)

# A) Lager knapper
avslutt_knapp = tk.Button(footer, text="Avslutt")
avslutt_knapp.pack()

# 6) Tastaturkontroll med piltaster.


def processKeypress(evt):
    key = evt.keysym
    print(f'key: {key}')
    if key == "Left":
        nisse.x_retning = -1
        nisse.y_retning = 0
    elif key == "Up":
        nisse.x_retning = 0
        nisse.y_retning = -1
    elif key == "Right":
        nisse.x_retning = 1
        nisse.y_retning = 0
    elif key == "Down":
        nisse.x_retning = 0
        nisse.y_retning = 1


window.bind("<Key>", processKeypress)


# B) Lager funksjonene til knappene


def avslutt(eventet):
    """Avslutter vinduet og programmet."""
    window.destroy()


teller = 0


# C) Binder knapper til funksjoner
avslutt_knapp.bind("<Button-1>", avslutt)


# Her animinerer vi
start_tid = time.time()
forrige_tid = time.time()
isRunning = True
fps = 60
intervall = 1 / fps
while isRunning:
    if time.time() - forrige_tid >= intervall:
        forrige_tid = time.time()
        nisse.oppdater()
        print(nisse.x,nisse.y)
        nisse.tegn(canvas)

    # Refresh vindu
    window.update()


# Kjører GUI-tråden
window.mainloop()
