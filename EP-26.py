#Day-26: Menu

import tkinter as tk

def file_new():
    print("File > New")

window = tk.Tk()
window.title("Tkinter Menu")
window.geometry('350x350')

# Create a menu
menu = tk.Menu(window)
window.config(menu=menu)

# File menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)

window.mainloop()
