import tkinter as tk
from tkinter import filedialog
#from picklistgenerator import functions as pg
from picklistgenerator.utils import Picklist

def browse_annotation():
    file_path = filedialog.askopenfilename()
    if file_path:
        annotation_var.set(file_path)

def browse_panel():
    file_path = filedialog.askopenfilename()
    if file_path:
        panel_var.set(file_path)

def browse_directory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        directory_var.set(dir_path)

def run_functions():
    picklist = Picklist(annotation_var.get(),panel_var.get())
    #annotation = import_file(annotation_var.get())
    #panel = import_file(panel_var.get())
    picklist.generate_picklist()
    picklist.export_picklist(directory_var.get(), experimentName_var.get())

root = tk.Tk()
root.title("Picklist Generator")

# Annotation file
annotation_label = tk.Label(root, text="Select Annotation file:")
annotation_label.pack()

annotation_var = tk.StringVar()
annotation_entry = tk.Entry(root, textvariable=annotation_var, width=50)
annotation_entry.pack()

annotation_button = tk.Button(root, text="Browse", command=browse_annotation)
annotation_button.pack()

# Panel library
panel_label = tk.Label(root, text="Select panel library:")
panel_label.pack()

panel_var = tk.StringVar()
panel_entry = tk.Entry(root, textvariable=panel_var, width=50)
panel_entry.pack()

panel_button = tk.Button(root, text="Browse", command=browse_panel)
panel_button.pack()

# Directory
directory_label = tk.Label(root, text="Select Directory:")
directory_label.pack()

directory_var = tk.StringVar()
directory_entry = tk.Entry(root, textvariable=directory_var, width=50)
directory_entry.pack()

directory_button = tk.Button(root, text="Browse", command=browse_directory)
directory_button.pack()

# Experiment name
experimentName_label = tk.Label(root, text="Enter name of experiment:")
experimentName_label.pack()

experimentName_var = tk.StringVar()
experimentName_entry = tk.Entry(root, textvariable=experimentName_var, width=50)
experimentName_entry.pack()

# run picklist generator
run_button = tk.Button(root, text="Generate picklist", command=run_functions)
run_button.pack()


root.mainloop()

# After the main loop, you can access the selected values using the variables
print("Annotation file:", annotation_var.get())
print("Panel library:", panel_var.get())
print("Save:", directory_var.get())
print("Experiment name:", experimentName_var.get())
