"""
Prompt 1:
Lag grafikk som ser ut som et garnnøste.

Tegn en sirkel.

Lag streker som går fra et tilfeldig punkt langs sirkelen og ender i et annet tilfeldig punkt på sirkelen.

Hver strek skal tegnes etter et tilfeldig intervall så strekene ikke tegnes opp jevnt, men i rykk og napp.

Prompt 2:
cos is not defined.

Prompt 3:
koden kjører ikke med timeout mellom hver strek.
"""
import tkinter as tk
import random
from math import cos, sin, pi

class GarnNoste:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=600, height=600, bg='#1351d8')
        self.canvas.pack()
        self.center_x = 300
        self.center_y = 300
        self.radius = 200

        # Tegn sirkelen
        self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                                self.center_x + self.radius, self.center_y + self.radius, outline='#ffa803')

        self.lines_to_draw = [(random.uniform(0, 2 * pi), random.uniform(0, 2 * pi)) for _ in range(50)]
        self.current_line = 0

        self.draw_next_line()

    def draw_next_line(self):
        if self.current_line < len(self.lines_to_draw):  # Sjekk om det finnes flere linjer å tegne
            angle1, angle2 = self.lines_to_draw[self.current_line]

            # Beregn koordinater for punkt 1
            x1 = self.center_x + self.radius * cos(angle1)
            y1 = self.center_y + self.radius * sin(angle1)

            # Beregn koordinater for punkt 2
            x2 = self.center_x + self.radius * cos(angle2)
            y2 = self.center_y + self.radius * sin(angle2)

            # Tegn linjen
            self.canvas.create_line(x1, y1, x2, y2, fill='#ffa803')

            # Øk teller for nest linje og sett opp neste tegning etter en pause
            self.current_line += 1
            self.master.after(random.randint(100, 500), self.draw_next_line)  # Vent en tilfeldig tid før neste linje tegnes

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Garnnøste")
    garn_noste = GarnNoste(root)
    root.mainloop()