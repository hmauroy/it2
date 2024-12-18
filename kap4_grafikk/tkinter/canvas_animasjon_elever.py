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

# Lager en sirkel
x = bredde/2
y = 50
R = 20
sirkel = canvas.create_oval(x-R,y-R,x+R,y+R,
                            fill="yellow",
                            outline="black",
                            width=3,
                            tags="sirkel")

# Animasjonsloop
isRunning = True
teller = 0
while isRunning:
    if teller >= 300:
        isRunning = False
    canvas.after(10)   # delay i ms
    canvas.delete("sirkel")
    y += 1
    # Tegner opp på nytt
    canvas.create_oval(x-R,y-R,x+R,y+R,
                            fill="yellow",
                            outline="black",
                            width=3,
                            tags="sirkel")
    
    canvas.update()
    teller += 1
    


window.mainloop()