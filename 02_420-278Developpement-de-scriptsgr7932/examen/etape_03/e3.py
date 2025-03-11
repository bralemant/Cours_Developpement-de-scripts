print("\n\033[94mÉtape 3. Listes et boucles. Liste de 1 à 10 et addition de 11\033[0m\n")
print()

# Création d'une liste de nombres de 1 à 10
nombres = list(range(1, 11))

# Parcourir la liste et afficher chaque nombre additionné de 11
for nombre in nombres:
    print(f"\033[7m{nombre} + 11 = {nombre + 11}\033[0m")