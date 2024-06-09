# Day 27 Boss Challenge : Miles to Kilometers Converter Program

import tkinter as tk
from tkinter import ttk

# Conversion function
def miles_to_km():
    try:
        miles = float(miles_entry.get())
        km = miles * 1.60934
        km_result_label.config(text=f"{km:.2f} Kilometers")
    except ValueError:
        km_result_label.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Miles to Kilometers Converter")
root.geometry('400x200')  # Set window size

# Configure the grid layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create and grid the widgets
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Define a larger font size
large_font = ('Helvetica', 16)

miles_label = ttk.Label(frame, text="Miles:", font=large_font)
miles_label.grid(row=0, column=0, sticky=tk.W)

miles_entry = ttk.Entry(frame, width=10, font=large_font)
miles_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

convert_button = tk.Button(frame, text="Convert", command=miles_to_km, font=large_font)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)

km_result_label = ttk.Label(frame, text="0 Kilometers", font=large_font)
km_result_label.grid(row=2, column=0, columnspan=2)

# Add padding to all widgets
for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=10)

# Run the application
root.mainloop()