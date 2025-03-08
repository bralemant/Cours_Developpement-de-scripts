import random

# Générer un nombre aléatoire entre 1 et 10
nombre_aleatoire = random.randint(1, 10)

# Demander à l'utilisateur de deviner le nombre
devine = int(input("Devinez un nombre entre 1 et 10 : "))

# Vérifier si l'utilisateur a deviné correctement
if devine == nombre_aleatoire:
    print("Félicitations ! Vous avez deviné correctement.")
else:
    print(f"Désolé, vous avez perdu. Le nombre correct était {nombre_aleatoire}.")