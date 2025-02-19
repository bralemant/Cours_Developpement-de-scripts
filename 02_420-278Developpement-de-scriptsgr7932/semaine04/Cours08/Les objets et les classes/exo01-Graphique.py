print("\n\033[92mExo 1. Calculatrice de périmètre et aire d'un rectangle.\033[0m")
print()

import tkinter as tk

class Rectangle:
    def __init__(self):
        self.largeur = 0.0
        self.hauteur = 0.0

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)

    def aire(self):
        return self.largeur * self.hauteur

def calculer():
    largeur_str = entree_largeur.get()
    hauteur_str = entree_hauteur.get()

    if largeur_str and hauteur_str:
        rect.largeur = float(largeur_str)
        rect.hauteur = float(hauteur_str)

        perimetre_label.config(text=f"Périmètre : {rect.perimetre():.2f}")
        aire_label.config(text=f"Aire : {rect.aire():.2f}")
    else:
        perimetre_label.config(text="Périmètre : Erreur")
        aire_label.config(text="Aire : Erreur")

# Création de l'interface graphique
fenetre = tk.Tk()
fenetre.title("Rectangle")

tk.Label(fenetre, text="Largeur:").grid(row=0, column=0)
entree_largeur = tk.Entry(fenetre)
entree_largeur.grid(row=0, column=1)

tk.Label(fenetre, text="Hauteur:").grid(row=1, column=0)
entree_hauteur = tk.Entry(fenetre)
entree_hauteur.grid(row=1, column=1)

bouton = tk.Button(fenetre, text="Convertir", command=calculer)
bouton.grid(row=2, columnspan=2)

perimetre_label = tk.Label(fenetre, text="Périmètre : ")
perimetre_label.grid(row=3, columnspan=2)

aire_label = tk.Label(fenetre, text="Aire : ")
aire_label.grid(row=4, columnspan=2)

rect = Rectangle()
fenetre.mainloop()
