"""Klasse for NisseMan (pacman med nissedrakt)"""
from tkinter import PhotoImage
class Nisse:
    def __init__(self):
        self.bilde = PhotoImage(file="nissen_small.png")
        self.x = 100
        self.y = 45
        self.x_retning = 0
        self.y_retning = 1
        self.fart = 20
    
    def oppdater(self):
        self.x += self.x_retning * self.fart
        self.y += self.y_retning * self.fart
    
    def tegn(self, canvas):
        canvas.coords(self.bilde, self.x, self.y)
        


