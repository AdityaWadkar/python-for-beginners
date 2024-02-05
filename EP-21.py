# Day-21: Introduction to tkinter

import tkinter as tk

# Create the main window
window = tk.Tk()

window.title("My First Tkinter App")
window.geometry('350x450')

window.resizable(0, 0)
window.configure(background='black')

# Start the main loop
window.mainloop()
