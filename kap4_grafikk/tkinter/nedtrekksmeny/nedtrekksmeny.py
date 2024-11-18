import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Dropdown Menu Example")

# Set the window size
root.geometry("300x200")

# Define the options for the dropdown menu
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Variable to hold the current selection
selected_option = tk.StringVar()
selected_option.set(options[0])  # Default value

# Create a dropdown (combobox) widget
dropdown = ttk.Combobox(root, textvariable=selected_option, values=options)
dropdown.pack(pady=20)  # Adds some vertical padding around the widget

# Function to display the selected option


def show_selection():
    selected = selected_option.get()
    print(f"Selected option: {selected}")
    # Display selection in a label as feedback
    label.config(text=f"Selected: {selected}")


# Button to confirm selection
button = tk.Button(root, text="Show Selection", command=show_selection)
button.pack(pady=10)

# Label to show selected option
label = tk.Label(root, text="Selected: ")
label.pack(pady=10)

# Start the main event loop
root.mainloop()
