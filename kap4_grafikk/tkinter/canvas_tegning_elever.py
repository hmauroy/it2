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
sirkel = canvas.create_oval(50,100,100,150,
                            fill="white",
                            outline="black",
                            width=5,
                            tags="sirkel")

rekt_bredde = 100
rekt_hoyde = 50
x = 200
y = 200
rektangel = canvas.create_rectangle(
    x-rekt_bredde/2,y-rekt_hoyde/2,
    x+rekt_bredde/2, y+rekt_hoyde/2,
    fill="black",
    outline="white",
    width=5,
    tags="rektangel"

    )
window.mainloop()