import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

app = tk.Tk()
app.title("CalmosPostflop")

def add_tabs(notebook, level=0, config_index=None, category_index=None):
    if level == 0:  # Configurations
        for config in configurations:
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=config)
            sub_notebook = ttk.Notebook(tab)
            sub_notebook.pack(fill=tk.BOTH, expand=True)
            add_tabs(sub_notebook, level + 1)
            sub_notebook.bind("<<NotebookTabChanged>>", lambda e: display_image())
    elif level == 1:  # Categories
        for category in categories:
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=category)
            sub_notebook = ttk.Notebook(tab)
            sub_notebook.pack(fill=tk.BOTH, expand=True)
            add_tabs(sub_notebook, level + 1)
            sub_notebook.bind("<<NotebookTabChanged>>", lambda e: display_image())
    elif level == 2:  # Floors
        for floor in floors:
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=floor)
            tab.bind("<Visibility>", lambda e: display_image())

def display_image():
    config_index = main_notebook.index(main_notebook.select())
    config_tab = main_notebook.nametowidget(main_notebook.select())
    category_notebook = config_tab.winfo_children()[0]
    category_index = category_notebook.index(category_notebook.select())
    category_tab = category_notebook.nametowidget(category_notebook.select())
    floor_notebook = category_tab.winfo_children()[0]
    floor_index = floor_notebook.index(floor_notebook.select())

    config = configurations[config_index]
    category = categories[category_index]
    floor = floors[floor_index]

    image_name = f"{config.replace(' ', '_')}_{category}_{floor}.jpg"
    print("image name : ", image_name)
    
    image_path = f"/home/jhown/projet_jp/{image_name}"
    
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

main_notebook = ttk.Notebook(app)
main_notebook.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

configurations = [
    "SH SRP CO vs BTN",
    "SH SRP BTN vs BB",
    "SH 3BP BTN vs CO",
    "SH 3BP SB vs BTN",
    "HU 3BP",
    "HU SRP"
]

categories = ["Unpaired", "Paired", "Straight", "Monotone"]
floors = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4"]

add_tabs(main_notebook)

image_label = ttk.Label(app)
image_label.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

app.mainloop()
