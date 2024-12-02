"""
Frames med tkinter
"""
import tkinter as tk
window = tk.Tk()
bredde = 500 # størrelse i pixler
hoyde = 500
window.minsize(bredde, hoyde)
window.configure(background="#FFFFFF") # Bruke web colors, white, black, peachpuff, maroon...

"""
Farger
#233142 mørk gråblå
#455d7a mørk grå
#f95959 rødorange
"""

# 1) Lage en header boks
header = tk.Frame(window,
    width = bredde,
    height=100,
    background="#233142"
    )
header.pack() # Legger rammen til vinduet.

# 2) Lage en hovedramme der innhold skal ligge
hovedramme = tk.Frame(window,
    width=bredde,
    height=350,
    background="#455d7a"
)
hovedramme.pack()

# 3) Lage en footer
footer = tk.Frame(window,
    width=bredde,
    height=50,
    background="#f95959"
    )
footer.pack()

window.mainloop()
