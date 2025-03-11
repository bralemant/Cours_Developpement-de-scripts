print("\n\033[92mExo 1. Calculatrice de périmètre et aire d'un rectangle.\033[0m")
print()

class Rectangle:
    def __init__(self, largeur=0, hauteur=0):
        self.largeur = largeur
        self.hauteur = hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)

    def aire(self):
        return self.largeur * self.hauteur

# Entrée utilisateur
largeur = float(input("Introduisez la largeur du rectangle : "))
hauteur = float(input("Introduisez la hauteur du rectangle : "))

# Créer un objet Rectangle avec les valeurs fournies
rect = Rectangle(largeur, hauteur)

# Afficher les résultats
print("\nInformations sur le rectangle :")
print("Largeur :", rect.largeur)
print("Hauteur :", rect.hauteur)
print("Périmètre :", rect.perimetre())
print("Aire :", rect.aire())