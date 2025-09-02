import tkinter as tk
import random

class Tre:
    TOMT = "tomt"
    TRE = "tre"
    BRENNER = "brenner"
    LYN = "lyn"

    def __init__(self):
        self.tilstand = Tre.TOMT
        self.lyn_sannsynlighet = 0.0003
        self.dager_i_brann = 0

    def voks(self):
        if self.tilstand==Tre.TOMT:
            self.tilstand=Tre.TRE
    
    def brenner(self):
        if self.tilstand==Tre.TRE:
            self.tilstand=Tre.BRENNER
            self.dager_i_brann = 0
    
    def oppdater(self,tilstand):
        if tilstand in [Tre.BRENNER, Tre.LYN]:
            print(tilstand)
            if self.dager_i_brann >= 1: #Mulig denne må flyttes
                self.tilstand = Tre.TOMT
            else:
                self.dager_i_brann += 1

    def brannfare(self):
        return self.tilstand in [Tre.BRENNER, Tre.LYN]
    

class Skog:
    def __init__(self, rader:int, kolonner:int):
        self.rader = rader
        self.kolonner = kolonner
        self.grid = [[Tre() for _ in range(kolonner)] for _ in range(rader)]
        self.tre_sannsynlighet = 0.003
        self.skogbrann = False


    def hent_naboer(self, rad:int, kol:int):
        naboer = []
        for dr, dc in [(-1, 0),(1, 0),(0, -1),(0, 1),(-1, 1),(-1,-1),(1,1),(1,-1)]:
            r = rad + dr
            c = kol + dc
            if 0 <= r < self.rader and 0 <= c < self.kolonner: #Passer på at "naboene" ikke er utenfor brettet
                naboer.append((r, c))
        return naboer
    
    def skog_vekst(self):
        trær = []

        for r in range(self.rader):
            for c in range(self.kolonner):
                tre = self.grid[r][c]
                if tre.tilstand == Tre.TOMT:
                    if random.random() <self.tre_sannsynlighet:
                        # print(random.random())
                        tre.voks()
                elif tre.tilstand == Tre.TRE:
                    if random.random() < 0.0003:
                        tre.tilstand = Tre.LYN
                        self.skogbrann = True

    
    def brenn_naboer(self):
        skal_brenne = []

        for r in range(self.rader):
            for c in range(self.kolonner):
                tre = self.grid[r][c]
                if tre.brannfare():
                    for nr, nc in self.hent_naboer(r, c):
                        nabo = self.grid[nr][nc]
                        if nabo.tilstand == Tre.TRE:
                            skal_brenne.append((nr, nc))
        if len(skal_brenne)==0:
            self.skogbrann=False
            return
        for r, c in skal_brenne:
            self.grid[r][c].brenner()
    
    def oppdater(self):
        if self.skogbrann:
            self.brenn_naboer()
            for rad in self.grid:
                for tre in rad:
                    tre.oppdater(tre.tilstand)
        else:
            self.skog_vekst()
            # print("Hallo")

            for rad in self.grid:
                for tre in rad:
                    tre.oppdater(tre.tilstand)

class Simulering():
    def __init__(self, window, størrelse:int=49, celle:int=10):
        self.størrelse = størrelse
        self.celle = celle
        self.canvas = tk.Canvas(window, width=størrelse * celle, height=størrelse * celle)
        self.canvas.pack()
        self.skog = Skog(størrelse, størrelse)

        midt = størrelse // 2
        self.skog.grid[midt][midt].tilstand = Tre.TRE
        self.dag = 0
        self.oppdater_gui()

    
    def oppdater_gui(self):
        self.canvas.delete("all")
        for r in range(self.størrelse):
            for c in range(self.størrelse):
                tre = self.skog.grid[r][c]
                self.tegn_tre(r, c, tre)

        if self.dag < 1000:
            self.skog.oppdater()
            self.dag += 1
            print(self.dag)
            self.canvas.after(100, self.oppdater_gui)

    def tegn_tre(self,rad, kol, tre):
        x1 = kol * self.celle
        y1 = rad * self.celle
        x2 = x1 + self.celle
        y2 = y1 + self.celle
        farge = self.farge_for(tre)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=farge, outline="white")

        if tre.tilstand == Tre.BRENNER:
            self.canvas.create_line(x1, y2, x2, y1, fill="black")
        elif tre.tilstand == Tre.LYN:
            self.canvas.create_line(x1, y2, x2, y1, fill="yellow")
        # elif tre.tilstand == Tre.IMMUN:
        #     self.canvas.create_oval(x1 + 3, y1 + 3, x2 - 3, y2 - 3, fill="black")
        # elif tre.tilstand == Tre.DOD:
        #     self.canvas.create_oval(x1 + 3, y1 + 3, x2 - 3, y2 - 3, fill="white")

    def farge_for(self, tre):
        if tre.tilstand == Tre.TOMT:
            return "light gray"
        elif tre.tilstand == Tre.LYN:
            return "yellow"
        elif tre.tilstand == Tre.BRENNER:
            return "red"
        elif tre.tilstand == Tre.TRE:
            return "green"
        

# Kjør programmet
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Skogbrann")
    sim = Simulering(window)
    window.mainloop()