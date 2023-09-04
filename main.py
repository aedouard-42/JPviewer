import tkinter as tk
from tkinter import ttk
import strategies

# Fonction pour afficher les stratégies d'une décision
def afficher_strategie(categorie, decision):
    donnees = strategies.obtenir_donnees(categorie, decision)
    texte.config(state=tk.NORMAL)
    texte.delete(1.0, tk.END)
    for item in donnees:
        texte.insert(tk.END, item + "\n\n")
    texte.config(state=tk.DISABLED)

# Fonction pour gérer le clic sur les boutons d'interaction
def gestion_clic_bouton(interaction):
    categorie, action = interaction.split(" vs ")
    if categorie == "SB" and action == "BU":
        app.title("Calmos SBvBU")
        afficher_decision_strategie()
    else:
        texte.config(state=tk.NORMAL)
        texte.delete(1.0, tk.END)
        texte.insert(tk.END, f"Données pour la décision {interaction}")
        texte.config(state=tk.DISABLED)

def afficher_decision_strategie():
    # Création des onglets pour stratégies
    onglets_strategies = ttk.Notebook(app)
    categories = {
        "DS": "Double Suited",
        "SS": "Single Suited",
        "RB": "Rainbow"
    }
    frames = {categorie: ttk.Frame(onglets_strategies) for categorie in categories.keys()}
    for categorie, onglet_text in categories.items():
        onglets_strategies.add(frames[categorie], text=onglet_text)
    
    # Ajuster les étiquettes des onglets
    style = ttk.Style()
    style.configure("TNotebook.Tab", padding=[30, 10], font=("Tahoma", 14, "bold"))
    
    # Création des labels et boutons de sélection
    for categorie in categories:
        frame = frames[categorie]
        label = ttk.Label(frame, text=f"Sélectionnez une décision pour {categorie}:", font=("Tahoma", 12, "bold"))
        label.pack(pady=10)
        for decision in ["Fold", "Flat", "3Bet"]:
            couleur = "gray" if decision == "Fold" else "green" if decision == "Flat" else "red"
            bouton = tk.Button(frame, text=decision, font=("Tahoma", 12, "bold"), bg=couleur,
                               command=lambda cat=categorie, dec=decision: afficher_strategie(cat, dec))
            bouton.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
    onglets_strategies.pack()

# Création de l'application avec interface graphique
app = tk.Tk()
app.title("Jpviewer")

# Définition des interactions par position
interactions = {
    "EP": ["EP vs BU", "EP vs Blinds"],
    "CO": ["CO vs EP", "CO vs BU", "CO vs Blinds"],
    "BU": ["BU vs EP", "BU vs CO", "BU vs Blinds"],
    "SB": ["SB vs EP", "SB vs CO", "SB vs BU", "SB vs BB"],
    "BB": ["BB vs EP", "BB vs CO", "BB vs BU", "BB vs SB"]
}

# Création des onglets pour chaque position
onglets = ttk.Notebook(app)

for position, interactions_position in interactions.items():
    frame_principal = ttk.Frame(onglets)
    onglets.add(frame_principal, text=position)

    # Création des boutons d'interaction pour cette position
    for interaction in interactions_position:
        bouton = tk.Button(frame_principal, text=interaction, font=("Tahoma", 12, "bold"),
                           command=lambda int=interaction: gestion_clic_bouton(int))
        bouton.pack(pady=10)

# Ajout de l'onglet principal à la fenêtre principale
onglets.pack()

# Création de la zone de texte pour afficher les données
texte = tk.Text(app, wrap=tk.WORD, font=("Tahoma", 12, "bold"))
texte.pack(padx=20, pady=20)
texte.config(state=tk.DISABLED)

# Exécution de l'application
app.mainloop()
