import tkinter as tk
import random

# Definere konstanter for tilstandene
EMPTY = 0
TREE = 1
BURNING = 2
BURNED = 3

# Simuleringsparametere
WIDTH = 20       # Antall kolonner
HEIGHT = 20      # Antall rader
TREE_GROWTH_PROB = 0.003  # 0.3% sannsynlighet for at et tre vokser
LIGHTNING_STRIKE_CHANCE = 0.01  # Sannsynlighet for lynnedslag

class ForestFireSimulator:
    def __init__(self, root):
        self.root = root
        self.grid = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.canvas = tk.Canvas(root, width=WIDTH*20, height=HEIGHT*20, bg='white')
        self.canvas.pack()
        
        # Plasser noen trær tilfeldig i skogen
        self.init_forest()
        
        self.running = True
        self.update()  # Start oppdateringssløyfen

    def init_forest(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if random.random() < 0.5:  # 50% sjanse for å plante ett tre
                    self.grid[y][x] = TREE

    def update(self):
        if self.running:
            self.simulate_fire()
            self.grow_trees()
            self.redraw()
            self.root.after(100, self.update)  # Oppdater hvert 100 ms
            
    def simulate_fire(self):
        # Finn alle brennende trær
        burning_trees = [(x, y) for y in range(HEIGHT) for x in range(WIDTH) if self.grid[y][x] == BURNING]

        # Hvis det finnes brennende trær vil vi stoppe veksten i skogen
        if burning_trees:
            self.running = False

        # Oppdater brennende trær til brent
        for x, y in burning_trees:
            self.grid[y][x] = BURNED

        # Spre brannen til naboene
        for x, y in burning_trees:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Opp, ned, venstre, høyre
                nx, ny = x + dx, y + dy
                if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and self.grid[ny][nx] == TREE:
                    self.grid[ny][nx] = BURNING

        # Slå lynet ned
        if random.random() < LIGHTNING_STRIKE_CHANCE:
            lightning_x = random.randint(0, WIDTH - 1)
            lightning_y = random.randint(0, HEIGHT - 1)
            if self.grid[lightning_y][lightning_x] == TREE:
                self.grid[lightning_y][lightning_x] = BURNING

    def grow_trees(self):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if self.grid[y][x] == EMPTY and not self.running:
                    if random.random() < TREE_GROWTH_PROB:
                        self.grid[y][x] = TREE

    def redraw(self):
        self.canvas.delete(tk.ALL)  # Tøm canvaset
        for y in range(HEIGHT):
            for x in range(WIDTH):
                color = 'white'
                if self.grid[y][x] == TREE:
                    color = 'green'
                elif self.grid[y][x] == BURNING:
                    color = 'red'
                elif self.grid[y][x] == BURNED:
                    color = 'gray'
                self.canvas.create_rectangle(x*20, y*20, (x+1)*20, (y+1)*20, fill=color)

if __name__ == '__main__':
    root = tk.Tk()
    simulator = ForestFireSimulator(root)
    root.mainloop()