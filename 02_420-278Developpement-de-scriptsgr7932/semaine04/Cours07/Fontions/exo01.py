print("\n\033[92mExo 1. Surface d'un rectangle.\033[0m")
print()
# Entrée utilisateur
longueur = input("Entrez la longueur du rectangle : ")
long = float(longueur)

largeur = input("Entrez la largeur du rectangle : ")
larg = float(largeur)

def surfaceRectangle(longueur, largeur):
    return longueur * largeur

# Appel de la fonction et affichage du résultat
print(f"\n\033[92mLa surface du rectangle est :\033[0m {surfaceRectangle(long, larg)}")
