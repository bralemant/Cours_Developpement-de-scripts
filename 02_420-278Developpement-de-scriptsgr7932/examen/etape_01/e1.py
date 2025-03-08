print("\n\033[94mÉtape 1. Introduction aux Variables. Saisie et affichage des informations utilisateur\033[0m")
print()

# Demander à l'utilisateur de saisir son nom
nom = input("Entrez votre nom : ")

# Vérification de l'âge (entrée numérique valide)
while True:
    age_input = input("Entrez votre âge : ")
    if age_input.isdigit():  # Vérifie si c'est un entier positif
        age = int(age_input)
        break
    else:
        print("\033[93m⚠️  Entrée invalide ! Veuillez entrer un nombre entier positif pour l'âge.\033[0m")

# Vérification de la valeur de PI
while True:
    pi_input = input("Entrez la valeur de PI : ").replace(",", ".")  # Supporte la virgule
    try:
        pi = float(pi_input)
        if 3.14 <= pi <= 3.1416:  # Vérifie si PI est réaliste
            break
        else:
            print("\033[93m⚠️  Veuillez entrer une valeur réaliste pour PI (ex: 3.141592).\033[0m")
    except ValueError:
        print("\033[93m⚠️  Entrée invalide ! Veuillez entrer un nombre valide pour PI.\033[0m")


# Afficher les informations avec une f-string 
print(f"\n\033[92mNom : {nom}, Âge : {age}, Valeur de PI : {pi:.8f}\033[0m")
