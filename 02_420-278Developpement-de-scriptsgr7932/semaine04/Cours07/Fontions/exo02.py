print("\n\033[92mExo 2. Répétition d'une chaîne de caractères.\033[0m")
print()
# Entrée utilisateur séparée de la conversion
n = input("Entrez le nombre de répétitions : ")
nb_repetitions = int(n)

ca = input("Entrez la chaîne de caractères : ")

def ligneCar(n, ca):
    return ca * n  # Répétition de la chaîne

# Affichage du résultat
print("\n\033[92mRésultat :\033[0m")
print(ligneCar(nb_repetitions, ca))
print()