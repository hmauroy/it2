import tkinter as tk
import math

class RotatingOvalApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.width = 150  # Bredde av ovalen
        self.height = 75  # Høyde av ovalen
        self.angle = 0  # Startvinkel
        self.center_x = 200
        self.center_y = 200
        self.num_points = 100  # Antall punkter for å jevnt tegne ovalen

        self.update_oval()
        self.rotate_oval()

    def update_oval(self):
        # Beregn punktene på ovalen
        points = []
        for i in range(self.num_points):
            theta = (i / self.num_points) * (2 * math.pi)  # Vinkel for nåværende punkt
            x = (self.width / 2) * math.cos(theta)  # X-koordinat
            y = (self.height / 2) * math.sin(theta)  # Y-koordinat

            # Roter punktene
            x_rotated = (x * math.cos(self.angle)) - (y * math.sin(self.angle))
            y_rotated = (x * math.sin(self.angle)) + (y * math.cos(self.angle))
            points.append((x_rotated + self.center_x, y_rotated + self.center_y))

        # Tøm canvas og tegn ovalen med de roterte punktene
        self.canvas.delete("all")
        self.canvas.create_polygon(points, fill="blue", outline="black")

    def rotate_oval(self):
        # Oppdater vinkelen og roter ovalen
        self.angle += 0.05  # Juster rotasjonshastighet
        if self.angle >= 2 * math.pi:
            self.angle = 0  # Resett vinkelen

        self.update_oval()
        self.master.after(50, self.rotate_oval)  # Oppdater hvert 50ms

if __name__ == "__main__":
    root = tk.Tk()
    app = RotatingOvalApp(root)
    root.mainloop()
