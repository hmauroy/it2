import tkinter as tk
import random
import time


class Person:
    FRISK = "frisk"
    SMITTET = "smittet"
    SYK = "syk"
    IMMUN = "immun"
    DOD = "dod"
    VAKRSINERT ="vaksinert"

    def __init__(self):
        self.tilstand = Person.FRISK
        self.dager_smittet = 0
        self.dager_syk = 0
        self.død_sannsynlighet = 0.2

    def smitt(self):
        if self.tilstand == Person.FRISK:
            self.tilstand = Person.SMITTET
            self.dager_smittet = 0

    def oppdater(self):
        if self.tilstand == Person.SMITTET:
            self.dager_smittet += 1
            if self.dager_smittet >= 3:
                self.tilstand = Person.SYK
                # self.dager_syk = 0

        elif self.tilstand == Person.SYK:
            self.dager_syk += 1
            if random.random() < self.død_sannsynlighet:
                self.tilstand = Person.DOD
            elif self.dager_syk >= 4:
                self.tilstand = Person.IMMUN

    def er_smittsom(self):
        return self.tilstand in [Person.SMITTET, Person.SYK]


class Populasjon:
    def __init__(self, rader:int, kolonner:int):
        self.rader = rader
        self.kolonner = kolonner
        self.grid = [[Person() for _ in range(kolonner)] for _ in range(rader)]
        self.smitte_sannsynlighet = 0.5

    def hent_naboer(self, rad:int, kol:int):
        naboer = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r = rad + dr
            c = kol + dc
            if 0 <= r < self.rader and 0 <= c < self.kolonner: #Passer på at "naboene" ikke er utenfor brettet
                naboer.append((r, c))
        return naboer

    def smitt_naboer(self):
        smittede = []

        for r in range(self.rader):
            for c in range(self.kolonner):
                person = self.grid[r][c]
                if person.er_smittsom():
                    for nr, nc in self.hent_naboer(r, c):
                        nabo = self.grid[nr][nc]
                        if nabo.tilstand == Person.FRISK:
                            if random.random() < self.smitte_sannsynlighet:
                                smittede.append((nr, nc))

        for r, c in smittede:
            self.grid[r][c].smitt()

    def tell_statistikk(self):
        statistikk = {
            "frisk": 0,
            "smittet": 0,
            "syk": 0,
            "immun": 0,
            "dod": 0,
            "vaksinert":0
        }
        for rad in self.grid:
            for person in rad:
                if person.tilstand == Person.FRISK:
                    statistikk["frisk"] += 1
                elif person.tilstand == Person.SMITTET:
                    statistikk["smittet"] += 1
                elif person.tilstand == Person.SYK:
                    statistikk["syk"] += 1
                elif person.tilstand == Person.IMMUN:
                    statistikk["immun"] += 1
                elif person.tilstand == Person.DOD:
                    statistikk["dod"] += 1
                elif person.tilstand == Person.VAKRSINERT:
                    statistikk["vaksinert"] += 1
        return statistikk

    def oppdater(self):
        self.smitt_naboer()
        for rad in self.grid:
            for person in rad:
                person.oppdater()

# Tkinter-visning
class Simulering:
    def __init__(self, window, rader=49, kolonner = 49, celle=12, andel_vaksinert=0.3):
        self.rader = rader
        self.kolonner = kolonner
        self.celle = celle
        self.label = tk.Label(window, text="", font=("Courier", 12), anchor="w")
        self.label.pack()
        self.canvas = tk.Canvas(window, width=kolonner * celle, height=rader * celle)
        self.canvas.pack()
        self.populasjon = Populasjon(rader, kolonner)

        # Vaksiner en andel av befolkningen
        for r in range(rader):
            for c in range(kolonner):
                if random.random() < andel_vaksinert:
                    self.populasjon.grid[r][c].tilstand = Person.VAKRSINERT

        # Starter med en syk person i midten og fire smittede naboer
        midt_kol = kolonner // 2
        midt_rad = rader // 2
        self.populasjon.grid[midt_rad][midt_kol].tilstand = Person.SYK

        for c, r in [(midt_kol - 1, midt_rad), (midt_kol + 1, midt_rad), (midt_kol, midt_rad - 1), (midt_kol, midt_rad + 1)]:
            if self.populasjon.grid[r][c].tilstand == Person.FRISK:
                self.populasjon.grid[r][c].smitt()

        self.dag = 0
        self.oppdater_gui()


    def farge_for(self, person):
        if person.tilstand == Person.FRISK:
            return "light gray"
        elif person.tilstand == Person.SMITTET:
            return "pink"
        elif person.tilstand == Person.SYK:
            return "red"
        elif person.tilstand == Person.IMMUN:
            return "dark gray"
        elif person.tilstand == Person.DOD:
            return "black"
        elif person.tilstand == Person.VAKRSINERT:
            return "green"

    def tegn_person(self, rad, kol, person):
        x1 = kol * self.celle
        y1 = rad * self.celle
        x2 = x1 + self.celle
        y2 = y1 + self.celle
        farge = self.farge_for(person)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=farge, outline="white")

        if person.tilstand == Person.SMITTET:
            self.canvas.create_line(x1, y2, x2, y1, fill="black")
        elif person.tilstand == Person.SYK:
            self.canvas.create_line(x1, y2, x2, y1, fill="white")
        elif person.tilstand == Person.IMMUN:
            self.canvas.create_oval(x1 + 3, y1 + 3, x2 - 3, y2 - 3, fill="black")
        elif person.tilstand == Person.DOD:
            self.canvas.create_oval(x1 + 3, y1 + 3, x2 - 3, y2 - 3, fill="white")
        elif person.tilstand == Person.VAKRSINERT:
            self.canvas.create_oval(x1 + 3, y1 + 3, x2 - 3, y2 - 3, fill="green", outline="white")

    def oppdater_statistikk_label(self):
        stats = self.populasjon.tell_statistikk()
        tekst = (
            f"Dag {self.dag:3} | "
            f"Friske: {stats['frisk']:4} "
            f"Vaks: {stats['vaksinert']:3} "
            f"Smit: {stats['smittet']:2} "
            f"Syke: {stats['syk']:3} "
            f"Imm: {stats['immun']:4} "
            f"Død: {stats['dod']:2}"
        )
        self.label.config(text=tekst)


    def oppdater_gui(self):
        self.canvas.delete("all")
        for r in range(self.rader):
            for c in range(self.kolonner):
                person = self.populasjon.grid[r][c]
                self.tegn_person(r, c, person)

        self.oppdater_statistikk_label()

        if self.dag < 100:
            self.populasjon.oppdater()
            self.dag += 1
            self.canvas.after(200, self.oppdater_gui)

# Kjør programmet
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Virusspredning")
    window_width = 800
    window_height = 800
    window.minsize(window_width,window_height)
    # MacOS har et nylig problem med fokus for popup-vinduer
    # Sentrer vinduet på skjermen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    # Fjern vindu midlertidig
    window.withdraw()  
    window.update()
    #vis vinduet igjen
    window.deiconify()
    sim = Simulering(window)
    window.mainloop()
