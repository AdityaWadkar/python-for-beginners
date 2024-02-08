#Day-25: Tkinter messagebox

import tkinter as tk
from tkinter import messagebox


def show_info():
    messagebox.showinfo("Information", "This is an information message.")

window = tk.Tk()
window.title("Tkinter Messagebox")
window.geometry('350x350')

# Button to trigger messagebox
button = tk.Button(window, text="Show Info", command=show_info)
button.pack()

window.mainloop()
