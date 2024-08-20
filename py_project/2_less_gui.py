import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Load the CSV file
DFGI = pd.read_csv('GroceryItems.csv', sep=',')

# Function to display all grocery items
def display_all():
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, DFGI)

# Function to display a particular column
def display_column():
    columns = {'1': 'Item Name:', '2': 'Quantity:', '3': 'Price (Rs):'}
    col = simpledialog.askstring("Input", "Enter column number (1: Item Name, 2: Quantity, 3: Price):")
    if col in columns:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, DFGI[columns[col]])

# Function to add a new item
def add_item():
    item = simpledialog.askstring("Input", "Enter item name:")
    if item in DFGI['Item Name:'].values:
        messagebox.showerror("Error", "Item already present!")
    else:
        quantity = simpledialog.askinteger("Input", "Enter quantity:")
        price = simpledialog.askinteger("Input", "Enter price:")
        DFGI.loc[len(DFGI)] = [item, quantity, price]
        messagebox.showinfo("Success", f"Item {item} added!")
        display_all()

# Function to remove an item
def remove_item():
    item = simpledialog.askstring("Input", "Enter item name to remove:")
    if item in DFGI['Item Name:'].values:
        DFGI.drop(DFGI[DFGI['Item Name:'] == item].index, inplace=True)
        messagebox.showinfo("Success", f"Item {item} removed!")
        display_all()
    else:
        messagebox.showerror("Error", "Item not present!")

# Function to display graphs
def display_graph(graph_type):
    if graph_type == 1:
        DFGI.plot(kind='bar', x='Item Name:', y='Quantity:', title='Quantity of items', color='red')
    elif graph_type == 2:
        DFGI.plot(kind='barh', x='Item Name:', y='Quantity:', title='Quantity of items', color='red')
    elif graph_type == 3:
        DFGI.plot(kind='line', x='Item Name:', y='Price (Rs):', title='Price of items', color='red', marker='H', markersize=10, linewidth=2)
    elif graph_type == 4:
        DFGI['Price (Rs):'].plot(kind='hist', title='Items in the same price range', color='orange', edgecolor='lime', linewidth=2, linestyle=':')
    plt.show()

# Function to save and exit
def save_and_exit():
    DFGI.to_csv('GroceryItems.csv', sep=',', index=False)
    root.destroy()

# Function to exit without saving
def exit_without_saving():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Grocery Items Data Management")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Buttons
ttk.Button(frame, text="Display All Items", command=display_all).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame, text="Display Column", command=display_column).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame, text="Add Item", command=add_item).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(frame, text="Remove Item", command=remove_item).grid(row=1, column=1, padx=5, pady=5)
ttk.Button(frame, text="Vertical Bar Graph", command=lambda: display_graph(1)).grid(row=2, column=0, padx=5, pady=5)
ttk.Button(frame, text="Horizontal Bar Graph", command=lambda: display_graph(2)).grid(row=2, column=1, padx=5, pady=5)
ttk.Button(frame, text="Line Graph", command=lambda: display_graph(3)).grid(row=3, column=0, padx=5, pady=5)
ttk.Button(frame, text="Histogram", command=lambda: display_graph(4)).grid(row=3, column=1, padx=5, pady=5)
ttk.Button(frame, text="Save and Exit", command=save_and_exit).grid(row=4, column=0, padx=5, pady=5)
ttk.Button(frame, text="Exit Without Saving", command=exit_without_saving).grid(row=4, column=1, padx=5, pady=5)

# Text output area
text_output = tk.Text(frame, width=80, height=20)
text_output.grid(row=5, column=0, columnspan=2, pady=5)

# Start GUI loop
root.mainloop()
