# Day-22: Label and entry widgets

import tkinter as tk

window = tk.Tk()
window.title("Tkinter Labels and Entry")
window.geometry('350x450')

# Label widget
label = tk.Label(window, text="Hello, Tkinter!",font=25)
label.pack()

# Entry widget (user input)
entry = tk.Entry(window,foreground="blue")
entry.pack()

window.mainloop()
