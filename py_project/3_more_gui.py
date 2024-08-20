import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ttkbootstrap as tb
from tkinter import messagebox, simpledialog, scrolledtext

# Load the CSV file
DFGI = pd.read_csv('GroceryItems.csv', sep=',')

# Function to display all grocery items
def display_all():
    text_output.delete(1.0, 'end')
    # Display with index starting from 1
    text_output.insert('end', DFGI.reset_index(drop=True).to_string(index=True, header=True))

# Function to display a particular column
def display_column():
    columns = {'1': 'Item Name:', '2': 'Quantity:', '3': 'Price (Rs):'}
    col = simpledialog.askstring("Input", "Enter column number (1: Item Name, 2: Quantity, 3: Price):")
    if col in columns:
        text_output.delete(1.0, 'end')
        text_output.insert('end', DFGI[columns[col]].reset_index(drop=True).to_string(index=True, header=True))

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
        DFGI.plot(kind='bar', x='Item Name:', y='Quantity:', title='Quantity of items', color='blue')
    elif graph_type == 2:
        DFGI.plot(kind='barh', x='Item Name:', y='Quantity:', title='Quantity of items', color='green')
    elif graph_type == 3:
        DFGI.plot(kind='line', x='Item Name:', y='Price (Rs):', title='Price of items', color='red', marker='o', markersize=5, linewidth=2)
    elif graph_type == 4:
        DFGI['Price (Rs):'].plot(kind='hist', title='Items in the same price range', color='orange', edgecolor='black', linewidth=1.2)
    plt.show()

# Function to save and exit
def save_and_exit():
    DFGI.to_csv('GroceryItems.csv', sep=',', index=False)
    root.destroy()

# Function to exit without saving
def exit_without_saving():
    root.destroy()

# GUI setup
root = tb.Window(themename="cosmo")
root.title("Grocery Items Data Management")
root.geometry("900x600")

frame = tb.Frame(root, padding="20")
frame.pack(fill='both', expand=True)

# Title label
title_label = tb.Label(frame, text="Grocery Items Data Management", bootstyle="info", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Buttons
button_style = {"bootstyle": "outline-primary", "padding": 10, "width": 20}
tb.Button(frame, text="Display All Items", command=display_all, **button_style).grid(row=1, column=0, padx=10, pady=10)
tb.Button(frame, text="Display Column", command=display_column, **button_style).grid(row=1, column=1, padx=10, pady=10)
tb.Button(frame, text="Add Item", command=add_item, **button_style).grid(row=2, column=0, padx=10, pady=10)
tb.Button(frame, text="Remove Item", command=remove_item, **button_style).grid(row=2, column=1, padx=10, pady=10)
tb.Button(frame, text="Vertical Bar Graph", command=lambda: display_graph(1), **button_style).grid(row=3, column=0, padx=10, pady=10)
tb.Button(frame, text="Horizontal Bar Graph", command=lambda: display_graph(2), **button_style).grid(row=3, column=1, padx=10, pady=10)
tb.Button(frame, text="Line Graph", command=lambda: display_graph(3), **button_style).grid(row=4, column=0, padx=10, pady=10)
tb.Button(frame, text="Histogram", command=lambda: display_graph(4), **button_style).grid(row=4, column=1, padx=10, pady=10)
tb.Button(frame, text="Save and Exit", command=save_and_exit, **button_style).grid(row=5, column=0, padx=10, pady=10)
tb.Button(frame, text="Exit Without Saving", command=exit_without_saving, **button_style).grid(row=5, column=1, padx=10, pady=10)

# Text output area with a scrollbar
text_frame = tb.Frame(frame)
text_frame.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew")
text_output = scrolledtext.ScrolledText(text_frame, width=100, height=20)
text_output.pack(fill='both', expand=True)

# Start GUI loop
root.mainloop()
 