import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

app = tk.Tk()
app.title("Calmos Postflop")

 
configurations_one = [
    "SH SRP CO vs BTN",
    "SH SRP BTN vs BB",
    "SH 3BP BTN vs CO",
    "SH 3BP SB vs BTN",
]
    
configurations_two = [
    "HU 3BP",
    "HU SRP"
]

# Rename specific tabs
tab_names_to_change = {
    "SH SRP BTN vs BB": "BTN vs BB",
    "SH 3BP BTN vs CO": "BTN vs CO",
    "SH 3BP SB vs BTN": "SB vs BTN",
    "SH SRP CO vs BTN": "CO vs BTN"
}


# Create a ttk style
style = ttk.Style()
style.theme_use('default')

# Configure the focus style to be transparent
style.configure('TNotebook.Tab', focuscolor='')

# Configurer le padding de l'onglet sélectionné
style.configure('TNotebook.Tab', padding=[10, 16], state='selected')

# Configurer la police de caractères de l'onglet
style.configure('TNotebook.Tab', font=(None, 18))

# Configurer la couleur de fond de l'onglet sélectionné
style.map('TNotebook.Tab', background=[("selected", "blue2"), ("!selected", "black")])

# Configure the tab text color
style.map("TNotebook.Tab", foreground=[("selected", "white"), ("!selected", "grey")])

# Configurez les onglets avec des bordures arrondies
style.configure('TNotebook.Tab', background='white', font=(None, 16), padding=[10, 10], borderwidth=3)

# Create a Notebook widget
main_notebook = ttk.Notebook(app)
main_notebook.pack(pady=2, padx=2, expand=True, fill=tk.BOTH)



def add_tabs(notebook, level=0, config_index=None, category_index=None):
    if level == 0:  # Configurations
        for config in configurations_one:
            new_name = tab_names_to_change[config]
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=new_name, padding=(0, 15))
            sub_notebook = ttk.Notebook(tab)
            sub_notebook.pack(fill=tk.BOTH, expand=True)
            add_tabs(sub_notebook, level + 1)
            sub_notebook.bind("<<NotebookTabChanged>>", lambda e: display_image())
            # Vérifier si c'est l'onglet "SB vs BTN"
            if new_name == "SB vs BTN" or new_name == "BTN vs CO" :
                label = ttk.Label(tab, text="3BET POT")
                label.configure (foreground="red2")
                label.configure(font=(None, 40))
                label.pack()
            else :
                label = ttk.Label(tab, text="SRP")
                label.configure (foreground="black")
                label.configure(font=(None, 40))
                label.configure(justify="center")
                label.pack()
    elif level == 1:  # Categories
        for category in categories:
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=category, padding=(0, 10))
            sub_notebook = ttk.Notebook(tab)
            sub_notebook.pack(fill=tk.BOTH, expand=True)
            add_tabs(sub_notebook, level + 1)
            sub_notebook.bind("<<NotebookTabChanged>>", lambda e: display_image())
    elif level == 2:  # Floors
        for floor in floors:
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=floor, padding=(20, 0))
            #, background='orange')
            tab.bind("<Visibility>", lambda e: display_image())

def display_image():
    config_index = main_notebook.index(main_notebook.select())
    config_tab = main_notebook.nametowidget(main_notebook.select())
    category_notebook = config_tab.winfo_children()[0]
    category_index = category_notebook.index(category_notebook.select())
    category_tab = category_notebook.nametowidget(category_notebook.select())
    floor_notebook = category_tab.winfo_children()[0]
    floor_index = floor_notebook.index(floor_notebook.select())

    config = configurations_one[config_index]
    category = categories[category_index]
    floor = floors[floor_index]

    image_name = f"{config.replace(' ', '_')}_{category}_{floor}.jpg"
    print("image name : ", image_name)
    
    image_path = f"C:/Users/Joel/Desktop/JPviewer/{image_name}"
    
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    canvas = tk.Canvas(image_label)
    canvas.pack()

    scrollbar = tk.Scrollbar(image_label, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    canvas.config(yscrollcommand=scrollbar.set)

    canvas.create_image(0, 0, image=photo)

    scrollbar.config(command=canvas.yview)
   

    

categories = ["Unpaired", "Paired", "Straight", "Monotone"]
floors = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4"]

add_tabs(main_notebook)

image_label = ttk.Label(app)
image_label.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

app.mainloop()
