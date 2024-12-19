import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample data for the bar chart
categories = ["Category A", "Category B", "Category C", "Category D"]
values = [10, 20, 15, 25]

# Function to plot the bar chart


def plot_bar_chart():
    # Clear any existing chart in the frame
    for widget in chart_frame.winfo_children():
        widget.destroy()

    # Create a matplotlib figure
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Plot bar chart
    ax.bar(categories, values, color="skyblue")

    # Add titles and labels
    ax.set_title("Sample Bar Chart")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Values")

    # Embed the plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def plot_line_chart():
    # Clear any existing chart in the frame
    for widget in chart_frame.winfo_children():
        widget.destroy()

    # Create a matplotlib figure
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Plot bar chart
    ax.plot(categories, values, color="skyblue", linestyle="dotted", marker="o")

    # Add titles and labels
    ax.set_title("Sample Line Chart")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Values")

    # Embed the plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Main Tkinter window
root = tk.Tk()
root.title("Tkinter Bar Chart Example")
root.geometry("600x500")

# Button to trigger the bar chart plot
plot_button = ttk.Button(root, text="Plot Bar Chart", command=plot_bar_chart)
plot_button.pack(pady=10)

# Knapp for linjegraf
plot_button_line = ttk.Button(root, text="Plot Line Chart", command=plot_line_chart)
plot_button_line.pack(pady=10)

# Frame to hold the chart
chart_frame = tk.Frame(root)
chart_frame.pack(fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()
