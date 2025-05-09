"""
En kloss er spinnvill.

To-do:
Animere

"""

import tkinter as tk  # Import tkinter


# Lag vindu
window = tk.Tk()  # Create a window
window.title("Spiral")  # Set title
# MacOS har et nylig problem med fokus for popup-vinduer i tkinter.
# Koden under fikser dette. Legg det inn rett etter at window er opprettet.

# Sentrer vinduet på skjermen
window_width = 400
window_height = 400
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

# Lag klokke-objekt
canvas = tk.Canvas(window, bg="#2e2e2e", width=400,
                   height=400)    # Lager et canvas-objekt
canvas.pack()    # Legg klokken inn i vinduet
canvas_width = 400
canvas_height = 400


class Firkant:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.l = 10
        self.border = 3
        self.bredde = 2*self.l + 2*self.border
        self.fart = 20
        self.x_retning = 1
        self.y_retning = 0
        self.posisjon_x = 0
        self.posisjon_y = 0
        self.fill = "dodgerblue"
        self.outline = "#fd6496"

    def tegn(self):
        canvas.create_rectangle(self.x-self.l, self.y-self.l,
                                self.x+self.l, self.y+self.l,
                                outline=self.outline,width=self.border, tags="firkant")

    def fjern(self):
        canvas.delete("firkant")


firkant = Firkant()
firkant.tegn()

teller = 0
isRunning = True
offset_x = 20 # Avstand for å lage spiral
offset_y = 20
teller = 0
høyreOffset = 0
bunnOffset = 0
venstreOffset = 0
toppOffset = 0
while isRunning == True:
    firkant.tegn()
    canvas.after(10)
    canvas.update()
    firkant.fjern()
    firkant.x += firkant.fart * firkant.x_retning
    firkant.y += firkant.fart * firkant.y_retning
    # Høyre
    if firkant.x+firkant.bredde/2 >= canvas_width - høyreOffset and firkant.x_retning == 1:
        firkant.x_retning = 0
        firkant.y_retning = 1
        firkant.x = canvas_width - firkant.bredde/2 - høyreOffset
        høyreOffset += offset_x
    # Bunn
    if firkant.y+firkant.bredde/2 >= canvas_height - bunnOffset and firkant.y_retning == 1:
        firkant.x_retning = -1
        firkant.y_retning = 0
        firkant.y = canvas_height - firkant.bredde/2 - bunnOffset
        bunnOffset += offset_y
    # Venstre
    if firkant.x-firkant.bredde/2 <= venstreOffset and firkant.x_retning == -1:
        firkant.x_retning = 0
        firkant.y_retning = -1
        firkant.x = firkant.bredde/2 + venstreOffset
        venstreOffset += offset_x
    # Topp
    if firkant.y-firkant.bredde/2 <= toppOffset and firkant.y_retning == -1:
        firkant.x_retning = 1
        firkant.y_retning = 0
        firkant.y = firkant.bredde/2 + toppOffset
        toppOffset += offset_y
    # Sjekker om firkanten har nådd omtrentlig sentrum
    print(f"høyreOffset,toppOffset {høyreOffset},{toppOffset}")
    if 0.98*høyreOffset > canvas_width/2:
        isRunning = False
        firkant.tegn()

    teller += 1
    if teller >= 10000000:
        isRunning = False
        firkant.tegn()



window.mainloop()  # Hovedloopen til programmet
