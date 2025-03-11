print("\n\033[92mExo 5. Trouver le maximum de trois nombres.\033[0m")
print()

# Entrée utilisateur
n1 = float(input("Entrez le premier nombre : "))
n2 = float(input("Entrez le deuxième nombre : "))
n3 = float(input("Entrez le troisième nombre : "))
def maximum(n1, n2, n3):
    return max(n1, n2, n3)  # Utilisation de max() pour trouver le plus grand

# Affichage du résultat
print(f"\n\033[92mLe maximum est : {maximum(n1, n2, n3)}\033[0m\n")
