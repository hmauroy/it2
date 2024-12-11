import tkinter as tk
import math

window = tk.Tk()
window.title("Canvas-tegning")
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)
window.configure(
    background="black"
)

# 1) Legger canvas direkte i vinduet
canvas = tk.Canvas()
canvas.configure(
    width=bredde,
    height=hoyde,
    background="#235E6F"
)
canvas.pack(expand=True)

x = 250
y = 250
r = 40

sirkel1 = canvas.create_oval(x-r,y-r,x+r,y+r,
                            fill="yellow",
                            outline="black",
                            width=5,
                            tags="sirkel")

sirkel2 = canvas.create_oval(x-r-70,y-r/2,x-r,y+r/2,
                            fill="white",
                            outline="black",
                            width=5,
                            tags="sirkel")

sirkel3 = canvas.create_oval(x+r,y-r/2,x+r+70,y+r/2,
                            fill="white",
                            outline="black",
                            width=5,
                            tags="sirkel")

sirkel4 = canvas.create_oval(x-r/2,y-r-70,x+r/2,y-r,
                            fill="white",
                            outline="black",
                            width=5,
                            tags="sirkel")

sirkel5 = canvas.create_oval(x-r/2,y+r+70,x+r/2,y+r,
                            fill="white",
                            outline="black",
                            width=5,
                            tags="sirkel")

polygon1 = canvas.create_polygon(x+(r*math.cos(math.pi/4)),y+(r*math.sin(math.pi/4)),x+100,y+50,x+100,y+100,x+50,y+100,
                            fill="white",
                            outline="black",
                            width=5,
                            tags="polygon"
)

polygon2 = canvas.create_polygon(x-(r*math.cos(math.pi/4)),y-(r*math.sin(math.pi/4)),x-100,y-50,x-100,y-100,x-50,y-100,
                            fill="white",
                            outline="black",
                            width=5,
                            tags="polygon"
)

polygon3 = canvas.create_polygon(x-(r*math.cos(math.pi/4)),y+(r*math.sin(math.pi/4)),x-100,y+50,x-100,y+100,x-50,y+100,
                            fill="white",
                            outline="black",
                            width=5,
                            tags="polygon"
)

polygon4 = canvas.create_polygon(x+(r*math.cos(math.pi/4)),y-(r*math.sin(math.pi/4)),x+100,y-50,x+100,y-100,x+50,y-100,
                            fill="white",
                            outline="black",
                            width=5,
                            tags="polygon"
)

window.mainloop()