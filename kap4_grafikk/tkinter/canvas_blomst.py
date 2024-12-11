import tkinter as tk


window = tk.Tk()
window.title("Canvas-tegning")
bredde = 500
hoyde = 500
window.minsize(bredde, hoyde)
window.configure(
    background="black"
)

# 1) Legger canvas direkte i vinduet
canvas = tk.Canvas()
canvas.configure(
    width = bredde,
    height = hoyde,
    background="#235E6F"
)
canvas.pack(expand=True)

# Lager en blomst på 
x = bredde/2
y = hoyde/2

R = 50
sirkel = canvas.create_oval(x-R,y-R,x+R,y+R,
                            fill="yellow",
                            outline="black",
                            width=3,
                            tags="sentrum")

def kronblad_vannrett(x, y, r, ovalhet, tag):
    """Lager et kronblad med posisjon x,y og radius r og ovalhet."""
    canvas.create_oval(x-r*ovalhet,y-r,x+r*ovalhet,y+r,
                            fill="white",
                            outline="black",
                            width=2,
                            tags=tag)

def kronblad_loddrett(x, y, r, ovalhet, tag):
    """Lager et kronblad med posisjon x,y og radius r og ovalhet."""
    canvas.create_oval(x-r,y-r*ovalhet,x+r,y+r*ovalhet,
                            fill="white",
                            outline="black",
                            width=2,
                            tags=tag)

kronblad_loddrett(x,y-R-50,30,1.6,"a")
kronblad_loddrett(x,y+R+50,30,1.6,"b")
kronblad_vannrett(x-R-50,y,30,1.6,"c")
kronblad_vannrett(x+R+50,y,30,1.6,"d")


window.mainloop()