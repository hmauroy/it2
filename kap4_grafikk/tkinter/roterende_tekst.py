#Import necessary libraries
import tkinter as tk
import math
#Create the Tkinter application and the canvas widget
root = tk.Tk()
# Set the geometry of Tkinter Window
root.geometry("700x500")
# Set the title of Tkinter Window
root.title("Rotating Text Around (or inside) a Circle)")
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
#Define the function to rotate the text around a circle
def rotate(angle=0):
   x = math.cos(angle) * 200 + 250
   y = math.sin(angle) * 200 + 250
   canvas.coords(txt, x, y)
   canvas.after(50, rotate, angle+0.05)
txt = canvas.create_text(250, 50, text="Rotated Text")
#Call the function
rotate()
#Run the Tkinter event loop
root.mainloop()