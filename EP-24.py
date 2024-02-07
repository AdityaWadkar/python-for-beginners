#Day-24: Frames and layout

#frames are use to organize the group of widgets
import tkinter as tk

window = tk.Tk()
window.title("Tkinter Frames and Layout")
window.geometry('350x350')

# Frame widgets
frame1 = tk.Frame(window, padx=10, pady=10,background="black",width=300,height=100)
frame1.pack_propagate(False)  #prevent frame from resizing while adding widgets
frame1.pack()

frame2 = tk.Frame(window, padx=10, pady=10,background="blue",width=300,height=100)
frame2.pack_propagate(False) #prevent frame from resizing while adding widgets
frame2.pack()

# Add widgets to frames

button1 = tk.Button(frame1, text="In frame1",)
button1.pack()

button2 = tk.Button(frame2, text="In frame2",)
button2.pack()

window.mainloop()
