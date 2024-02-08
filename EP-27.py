#Day-27: Canvas

import tkinter as tk

window = tk.Tk()
window.title("Tkinter Canvas")

# Canvas widget (draw shapes on tkinter window)
canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()

# Draw on the canvas
canvas.create_line(0, 0, 200, 200, fill="blue")
canvas.create_rectangle(50, 50, 150, 150, fill="green")

window.mainloop()
