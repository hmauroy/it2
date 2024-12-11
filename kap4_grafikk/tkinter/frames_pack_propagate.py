"""
Grafikk med tkinter.
Frames er i fokus.
"""
import tkinter as tk
window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)    # Setter vinduets størrelse ved oppstart.
window.configure(background="hotpink")
window.title("Frames Pack propagate")

# 1) Lager første vindu en "Frame"
header = tk.Frame(window)
header.configure(
    background="lightpink",
    height=100,
    width=bredde,
)
header.pack()

hovedvindu = tk.Frame(window)
hovedvindu.configure(
    background="deeppink",
    height=350,
    width=bredde,
)
hovedvindu.pack()

# Legger et vindu inni et annet
innervindu = tk.Frame(hovedvindu)
innervindu.configure(
    background="MediumVioletRed",
    height=100,
    width=bredde*0.8,
)
hovedvindu.pack_propagate(False) # Skrur av at children kan endre rammen.
innervindu.pack()


footer = tk.Frame(window)
footer.configure(
    background="palevioletred",
    height=50,
    width=bredde,
)
footer.pack()




# Kjører GUI-tråden
window.mainloop()


