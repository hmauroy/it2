import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Passordgenerator")

        # Variabler for innstillinger
        self.length = tk.IntVar(value=8)  # Standard passordlengde
        self.include_uppercase = tk.BooleanVar(value=False)
        self.include_numbers = tk.BooleanVar(value=False)

        # GUI-komponenter
        self.create_widgets()

    def create_widgets(self):
        # Lengde på passordet
        tk.Label(self.master, text="Lengde på passord:").pack()
        self.length_scale = tk.Scale(self.master, from_=1, to=20, orient=tk.HORIZONTAL, variable=self.length)
        self.length_scale.pack()

        # Innstillinger for store bokstaver
        self.uppercase_checkbox = tk.Checkbutton(self.master, text="Inkluder store bokstaver", variable=self.include_uppercase, command=self.update_selected_options)
        self.uppercase_checkbox.pack()

        # Innstillinger for tall
        self.numbers_checkbox = tk.Checkbutton(self.master, text="Inkluder tall", variable=self.include_numbers, command=self.update_selected_options)
        self.numbers_checkbox.pack()
        
        # Valgt innhold
        self.selected_options_label = tk.Label(self.master, text="Valgt: ")
        self.selected_options_label.pack()

        # Generer passord-knapp
        self.generate_button = tk.Button(self.master, text="Generer passord", command=self.generate_password)
        self.generate_button.pack()

        # Felt for å vise generert passord
        self.password_label = tk.Label(self.master, text="", font=('Arial', 14))
        self.password_label.pack()

        # Oppdaterer valgte alternativer ved oppstart
        self.update_selected_options()

    def update_selected_options(self):
        options_text = "Valgt: "
        if self.include_uppercase.get():
            options_text += "Store bokstaver, "
        if self.include_numbers.get():
            options_text += "Tall, "
        if options_text == "Valgt: ":
            options_text = "Ingen tillegg valgt"
        self.selected_options_label.config(text=options_text[:-2])  # Fjerner siste komma

    def generate_password(self):
        length = self.length.get()
        characters = string.ascii_lowercase  # Standard tegn (små bokstaver)

        if self.include_uppercase.get():
            characters += string.ascii_uppercase  # Legg til store bokstaver
        if self.include_numbers.get():
            characters += string.digits  # Legg til tall

        # Generer passord
        if characters:
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text=f"Generert passord: {password}")
        else:
            messagebox.showwarning("Ingen valg", "Vennligst velg minst én type tegn.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()