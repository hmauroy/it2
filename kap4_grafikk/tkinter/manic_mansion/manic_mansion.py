import tkinter as tk
import time
from random import randrange

from klasser import *

window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
window_width = 700
window_height = 700
canvas_height = 600
canvas_width = window_width
window.minsize(window_width,window_height)
# MacOS har et nylig problem med fokus for popup-vinduer
# Sentrer vinduet på skjermen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Fjern vindu midlertidig
window.withdraw()  
window.update()
#vis vinduet igjen
window.deiconify()

# 1) Lager en header for overskrift
header = tk.Canvas(frame1, width=window_width, height=100)
header.pack()
overskrift = tk.Label(header, text="Manic Mansion")
overskrift.pack()

# 2) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

canvas = tk.Canvas(canvas_frame, width=canvas_width,
                   height=canvas_height, background="black")
canvas.pack()
# Lager frisonen til venstre
canvas.create_rectangle(0,0,100,canvas_height, fill="lightgray")
# Lager frisonen til høyre
canvas.create_rectangle(canvas_width-100,0,canvas_width,canvas_height, fill="green")


# avsluttknapp
footer = tk.Frame(window)
footer.pack()
avslutt = tk.Button(footer, text="Avslutt")
avslutt.pack()



def handle_avslutt(event):
    global isRunning
    isRunning = False
    window.destroy()        

avslutt.bind("<Button-1>", handle_avslutt)


def tilfeldigPos(type):
    global BREDDE
    """Genererer tilfeldig koordinat i forhold til hvor på brettet objektene skal starte."""
    boundingbox = [] # [x1,y1, x2,y2]
    if type == "M":
        boundingbox = [BREDDE,BREDDE,100-BREDDE, canvas_height-BREDDE]
    elif type == "S" or type == "H":
        boundingbox = [100 + BREDDE,BREDDE,canvas_width-100-BREDDE, canvas_height-BREDDE]
    elif type == "BÆ":
        boundingbox = [canvas_width-100+BREDDE,BREDDE,canvas_width-BREDDE, canvas_height-BREDDE]
    x = randrange(boundingbox[0],boundingbox[2])
    y = randrange(boundingbox[1],boundingbox[3])
    return x,y


# Oppretter spillbrett og spillbrikker.
# Spillbrettet har 100 px på hver side som er frisoner.
brett = Spillebrett(canvas_height, canvas_width)
BREDDE = 30
x,y = tilfeldigPos("M")
M = Menneske(x,y,BREDDE,5) # Starter på venstre side
brett.leggTileObjekt(M)
x,y = tilfeldigPos("BÆ")
S1 = Sau(x,y,BREDDE)
x,y = tilfeldigPos("BÆ")
S2 = Sau(x,y,BREDDE)
x,y = tilfeldigPos("BÆ")
S3 = Sau(x,y,BREDDE)

brett.leggTileObjekt(S1)
brett.leggTileObjekt(S2)
brett.leggTileObjekt(S3)

brett.tegnAlleObjekt(canvas)




# Her animinerer vi
start_tid = time.time()
forrige_tid = time.time()
isRunning = True
fps = 10
intervall = 1 / fps
while isRunning:
    if time.time() - forrige_tid >= intervall:
        forrige_tid = time.time()
        isRunning = brett.oppdater(canvas)


    # Refresh vindu
    window.update()


window.mainloop()
