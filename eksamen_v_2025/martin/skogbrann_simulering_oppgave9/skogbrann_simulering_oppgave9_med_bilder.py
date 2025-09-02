import tkinter as tk
import random
from PIL import Image, ImageTk


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
    def __init__(self, window, bredde:int=49, høyde:int=49, celle:int=10):
        self.bredde = bredde
        self.høyde = høyde
        self.celle = celle
        self.canvas = tk.Canvas(window, width=bredde * celle, height=høyde * celle)
        self.canvas.pack()
        # Last inn bilder
        self.bilde_tre = ImageTk.PhotoImage(Image.open("tre.png").resize((self.celle, self.celle)))
        self.bilde_brenner = ImageTk.PhotoImage(Image.open("flamme.png").resize((self.celle, self.celle)))
        self.bilde_lyn = ImageTk.PhotoImage(Image.open("lyn.png").resize((self.celle, self.celle)))
        self.skog = Skog(høyde, bredde)

        midt_h = høyde // 2
        midt_b = bredde // 2
        self.skog.grid[midt_h][midt_b].tilstand = Tre.TRE
        self.dag = 0
        self.oppdater_gui()

    
    def oppdater_gui(self):
        self.canvas.delete("all")
        for r in range(self.høyde):
            for c in range(self.bredde):
                tre = self.skog.grid[r][c]
                self.tegn_tre(r, c, tre)

        if self.dag < 1000:
            self.skog.oppdater()
            self.dag += 1
            print(self.dag)
            self.canvas.after(500, self.oppdater_gui)

    def tegn_tre(self, rad, kol, tre):
        x1 = kol * self.celle
        y1 = rad * self.celle

        if tre.tilstand == Tre.TRE:
            self.canvas.create_image(x1, y1, anchor="nw", image=self.bilde_tre)
        elif tre.tilstand == Tre.BRENNER:
            self.canvas.create_image(x1, y1, anchor="nw", image=self.bilde_brenner)
        elif tre.tilstand == Tre.LYN:
            self.canvas.create_image(x1, y1, anchor="nw", image=self.bilde_lyn)
        else:
            self.canvas.create_rectangle(x1, y1, x1 + self.celle, y1 + self.celle, fill="tan", outline="white")


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
    sim = Simulering(window,celle=14,bredde=80)
    window.mainloop()