"""Hentet fra ki.osloskolen.no"""
import tkinter as tk
import math

class RotatingRectangleApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.rect_width = 100
        self.rect_height = 50
        self.angle = 0  # Startvinkel
        self.center_x = 200
        self.center_y = 200

        self.update_rectangle()
        self.rotate_rectangle()

    def update_rectangle(self):
        # Beregn de fire hjørnene av rektangelet
        corners = [
            (-self.rect_width / 2, -self.rect_height / 2),
            (self.rect_width / 2, -self.rect_height / 2),
            (self.rect_width / 2, self.rect_height / 2),
            (-self.rect_width / 2, self.rect_height / 2)
        ]

        rotated_corners = []
        for x, y in corners:
            # Roter hjørnene
            x_rotated = (x * math.cos(self.angle)) - (y * math.sin(self.angle))
            y_rotated = (x * math.sin(self.angle)) + (y * math.cos(self.angle))
            rotated_corners.append((x_rotated + self.center_x, y_rotated + self.center_y))

        # Tøm canvas og tegn rektangelet med de roterte hjørnene
        self.canvas.delete("all")
        self.canvas.create_polygon(rotated_corners, fill="blue")

    def rotate_rectangle(self):
        # Oppdater vinkelen og roter rektangelet
        self.angle += 0.05  # Endre denne verdien for å justere rotasjonshastigheten
        if self.angle >= 2 * math.pi:
            self.angle = 0  # Resett vinkelen

        self.update_rectangle()
        self.master.after(50, self.rotate_rectangle)  # Oppdater hvert 50ms

if __name__ == "__main__":
    root = tk.Tk()
    app = RotatingRectangleApp(root)
    root.mainloop()