print("\n\033[94mÉtape 2. Structures de contrôle. Devinez le nombre \033[0m")
print()

import random

# Générer un nombre aléatoire entre 1 et 10
nombre_aleatoire = random.randint(1, 10)

# Demander à l'utilisateur de deviner le nombre
while True:
    entree = input("Devinez un nombre entre 1 et 10 : ")  # Récupérer l'entrée utilisateur
    if entree.isdigit():  # Vérifier si c'est un nombre entier
        devine = int(entree)
        if 1 <= devine <= 10:
            break  # Sortir de la boucle si l'entrée est correcte
        else:
            print("\033[93m⚠️  Veuillez entrer un nombre entre 1 et 10.\033[0m")
    else:
        print("\033[93m⚠️  Entrée invalide ! Veuillez entrer un nombre entier entre 1 et 10.\033[0m")


# Vérifier si l'utilisateur a deviné correctement
if devine == nombre_aleatoire:
    print("\n\033[92m🎉🎉🎉  Félicitations !!! Vous avez deviné correctement.  🎉🎉🎉\033[0m")
else:
    print(f"\n\033[91m😢  Désolé, vous avez perdu. Le nombre correct était {nombre_aleatoire}.\033[0m")
    