# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Che Mack
# Assignment Number: Assignment 3
# Due Date: 10/10/2026
# Purpose: This program creates a GUI that converts Miles per Gallon (MPG)
#          into Kilometers per Liter (KM/L). The conversion updates automatically
#          as the user types and handles blank or invalid entries without crashing.
# Resources Used: Course materials and Python tkinter documentation.

import tkinter as tk


# This function converts MPG to KM/L
def convert_mpg(*args):
    try:
        # Get the MPG value entered by the user
        mpg = float(mpg_entry.get())

        # Convert MPG to KM/L
        km_l = mpg * 0.425143707

        # Display the converted result
        result_var.set(f"{km_l:.2f}")

    except ValueError:
        # Clear the result if the box is blank or contains letters
        result_var.set("")


# Create the main GUI window
window = tk.Tk()
window.title("MPG to KM/L Converter")
window.geometry("400x220")


# Create the title
title_label = tk.Label(
    window,
    text="MPG to KM/L Converter",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=15)


# Create the MPG input area
mpg_label = tk.Label(window, text="Miles per Gallon (MPG):")
mpg_label.pack()

mpg_var = tk.StringVar()
mpg_entry = tk.Entry(
    window,
    textvariable=mpg_var,
    width=20
)
mpg_entry.pack(pady=5)


# Create the KM/L result area
result_label = tk.Label(window, text="Kilometers per Liter (KM/L):")
result_label.pack(pady=(10, 0))

result_var = tk.StringVar()

result_display = tk.Label(
    window,
    textvariable=result_var,
    font=("Arial", 14, "bold")
)
result_display.pack(pady=5)


# Update the conversion automatically whenever the user types
mpg_var.trace_add("write", convert_mpg)


# Place the cursor in the MPG box when the program starts
mpg_entry.focus()


# Keep the GUI window open
window.mainloop()
