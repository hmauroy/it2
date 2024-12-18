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

rekt_bredde = 100
rekt_hoyde = 100
x = bredde/2
y = hoyde/2
rektangel = canvas.create_rectangle(
    x-rekt_bredde/2,y-rekt_hoyde/2,
    x+rekt_bredde/2, y+rekt_hoyde/2,
    outline="red",
    width=5,
    tags="rektangel"

    )

R = rekt_bredde/2
sirkel = canvas.create_oval(x-R,y-R,x+R,y+R,
                            fill="red",
                            outline="white",
                            width=3,
                            tags="sirkel")

window.mainloop()