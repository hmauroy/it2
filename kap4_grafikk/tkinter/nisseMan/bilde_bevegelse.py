import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Click to Reposition Image")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Load and add an image
image = Image.open("nissen_small.png")  # Replace with your image file
photo = ImageTk.PhotoImage(image)
# Initially place at (200, 200)
image_id = canvas.create_image(200, 200, image=photo)

# Function to reposition the image where the user clicks


def click_reposition(event):
    # Move image to the clicked position
    canvas.coords(image_id, event.x, event.y)


# Bind left mouse click to reposition the image
canvas.bind("<Button-1>", click_reposition)

# Start the main loop
root.mainloop()
