#Day-28: Advanced Widgets

import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Tkinter Advanced Widgets")

# Create a Treeview widget
tree = ttk.Treeview(window)

# Define columns for the treeview
tree["columns"] = ("Name", "Age")

# Configure column properties
# Treeview item indicator and is set to 0 width (invisible)
tree.column("#0", width=0, stretch=tk.NO) 
tree.column("Name", anchor=tk.W)  # Set the anchor for the "Name" column to West
tree.column("Age", anchor=tk.W)   # Set the anchor for the "Age" column to West

# Set column headings
tree.heading("#0", text="", anchor=tk.W)  # Heading for the invisible treeview item indicator column
tree.heading("Name", text="Name", anchor=tk.W)  # Heading for the "Name" column
tree.heading("Age", text="Age", anchor=tk.W)    # Heading for the "Age" column

# Insert data into the treeview
tree.insert("", 0, text="Item 1", values=("John Doe", 25))  # Insert an item with values in the "Name" and "Age" columns
tree.insert("", 1, text="Item 2", values=("Jane Smith", 30))  # Insert another item

# Pack the treeview widget into the window
tree.pack()

# Start the Tkinter event loop
window.mainloop()


