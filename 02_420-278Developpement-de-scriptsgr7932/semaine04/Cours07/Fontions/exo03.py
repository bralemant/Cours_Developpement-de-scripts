print("\n\033[92mExo 3. Surface d'un cercle.\033[0m")
print()
# Entrée utilisateur séparée de la conversion
R = input("Entrez le rayon du cercle : ")
rayon = float(R)

import math  # Pour utiliser π

def surfCercle(R):
    return math.pi * R**2  # Aire du cercle

# Appel de la fonction et affichage du résultat
print(f"\n\033[92mLa surface du cercle est :\033[0m {surfCercle(rayon):.3f}")