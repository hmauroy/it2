import tkinter as tk
import random
class Person:
    FRISK = "frisk"
    SMITTET = "smittet"
    SYK = "syk"
    IMMUN = "immun"
    DØD = "død"
    def __init__(self):
        self.tilstand = Person.FRISK
        self.dager_smittet = 0
        self.dager_syk = 0 
        self.død_sannsynlighet = 0.01
    def smitt(self):
        if self.tilstand == Person.FRISK:
            self.tilstand = Person.SMITTET
    def er_smittsom(self):
        return self.tilstand in [Person.SMITTET, Person.SYK]
    
    def oppdater(self):
        if self.tilstand == Person.SMITTET:
            self.dager_smittet += 1
            if self.dager_smittet >= 3:
                self.tilstand = Person.SYK
        
        elif self.tilstand == Person.SYK:
            self.dager_syk += 1
            if random.random()<self.død_sannsynlighet:
                self.tilstand = Person.DØD
            elif self.dager_syk >= 4:
                self.tilstand = Person.IMMUN
    
class Populasjon:
    def __init__(self, rader=49, kolonner=49):
        self.rader = rader
        self.kolonner = kolonner
        self.smitte_sannsynlighet = 0.3
        self.grid = [[Person() for _ in range(kolonner)] for _ in range(rader)]
    
    def hent_naboer(self, rad, kol):
        naboer = []
        for dr, dk in [(-1,0), (1,0), (0,-1), (0,1)]:
            r = rad + dr
            k = kol + dk
            if 0 <= r < self.rader and 0 <= k < self.kolonner:
                naboer.append((r,k))
        return naboer
    
    def smitt_naboer(self):
        smittede = []
        for r in range(self.rader):
            for k in range(self.kolonner):
                person = self.grid[r][k]
                if person.er_smittsom():
                    for nr, nk in self.hent_naboer(r, k):
                        nabo = self.grid[nr][nk]
                        if nabo.tilstand == Person.FRISK:
                            if random.random() < self.smitte_sannsynlighet:
                                smittede.append((nr,nk))
        
        for r, k in smittede:
            self.grid[r][k].smitt()
    
    def oppdater(self):
        self.smitt_naboer()
        for rad in self.grid:
            for person in rad:
                person.oppdater()
    
class Simulering:
    def __init__(self, window, størrelse = 49, celle = 10):
        self.størrelse = størrelse
        self.celle = celle
        self.canvas = tk.Canvas(window, width= størrelse*celle, height=størrelse*celle )
        self.canvas.pack()
        self.populasjon = Populasjon(størrelse, størrelse)
        midt = størrelse // 2
        self.populasjon.grid[midt][midt].tilstand = Person.SYK
        for r, k in [(midt -1, midt), (midt +1,midt), (midt, midt -1), (midt, midt +1)]:
            self.populasjon.grid[r][k].smitt()
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
        elif person.tilstand == Person.DØD:
            return "black"
    
    def tegn_person(self, rad, kol, person):
        x1 = kol * self.celle
        y1 = rad * self.celle
        x2 = x1 + self.celle
        y2 = y1 + self.celle
        farge = self.farge_for(person)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=farge, outline="white")
        if person.tilstand == Person.SMITTET:
            self.canvas.create_line(x1, y1, x2, y2, fill="black")
        elif person.tilstand == Person.SYK:
            self.canvas.create_line(x1, y2, x2, y1, fill="white")
        elif person.tilstand == Person.IMMUN:
            self.canvas.create_oval(x1+3, y1+3, x2-3, y2-3, fill="black")
        elif person.tilstand == Person.DØD:
            self.canvas.create_oval(x1+3, y1+3, x2-3, y2-3, fill="white")
    
    def oppdater_gui(self):
        self.canvas.delete("all")
        for r in range(self.størrelse):
            for k in range(self.størrelse):
                person = self.populasjon.grid[r][k]
                self.tegn_person(r, k, person)
        
        if self.dag < 100:
            self.populasjon.oppdater()
            self.dag += 1
            self.canvas.after(500, self.oppdater_gui)
        
#Kjør programmet
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Virusspredning")
    sim = Simulering(window)
    window.mainloop()