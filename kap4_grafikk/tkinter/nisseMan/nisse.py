"""Klasse for NisseMan (pacman med nissedrakt)"""
from tkinter import PhotoImage
class Nisse:
    def __init__(self):
        self.bilde = PhotoImage(file="nissen_small.png")
        self.x = 100
        self.y = 45
        self.x_retning = 0
        self.y_retning = 1
        self.fart = 3
        self.R = 20
    
    def oppdater(self):
        self.x += self.x_retning * self.fart
        self.y += self.y_retning * self.fart
    
    def tegn(self, canvas):
        canvas.delete("nisse")
        canvas.create_oval(self.x-self.R,self.y-self.R,self.x+self.R,self.y+self.R,
        fill="yellow",
        outline="black",
        width=5,
        tags="nisse")
    
    def kollisjon(self, bredde, hoyde):
        if self.x >= bredde + self.R:
            self.x = -self.R
        elif self.x <= -self.R:
            self.x = bredde + self.R
        


