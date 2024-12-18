import tkinter as tk

window = tk.Tk()
window.title("Button med lambda")
bredde = 500
hoyde = 500
window.minsize(bredde, hoyde)

knapp = tk.Button(window,text="OK", command=lambda: handle_knapp(5))
knapp.pack(expand=True)

def handle_knapp(tall):
    print(tall) # Informasjon kan sendes fra lambda-uttrykket til funksjonen.
    knapp["text"] = "Trykket!"

window.mainloop()