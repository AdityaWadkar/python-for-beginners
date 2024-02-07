#Day-23: Buttons and events

import tkinter as tk

window = tk.Tk()
window.title("Tkinter Buttons and Events")
window.geometry('350x350')

# Button widget
def button_click():
    label.config(text="Button Clicked!")

button = tk.Button(window, text="Click Me", command=button_click)
button.pack()

# Label widget to display event response
label = tk.Label(window, text="")
label.pack()

window.mainloop()
