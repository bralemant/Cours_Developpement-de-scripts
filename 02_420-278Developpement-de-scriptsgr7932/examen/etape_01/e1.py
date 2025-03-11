print("\n\033[94mÉtape 1. Introduction aux Variables. Saisie et affichage des informations utilisateur\033[0m")
print()

# Vérification du nom (lettres, espaces et tirets uniquement)
while True:
    nom = input("📝 Entrez votre nom : ").strip()
    valide = True                                                       # On suppose que le nom est valide

    for c in nom:                                                       # Vérification caractère par caractère
        if not (c.isalpha() or c == " " or c == "-"):                   # Vérifie si le caractère est alphabétique, un espace ou un tiret
            valide = False                                              # Si un caractère invalide est trouvé, on arrête
            break                                                       # Arrêter dès qu'on trouve un caractère invalide

    if valide and nom:                                                  # Vérification finale
        break
    else:
        print("\033[93m⚠️  Entrée invalide ! Veuillez entrer un nom valide (lettres, espaces, tirets et accents uniquement).\033[0m")

# Vérification de l'âge (entrée numérique valide)
while True:
    age_input = input("📝 Entrez votre âge : ").strip()                                       
    if age_input.isdigit():                                             # Vérifie si l'entrée est un nombre entier positif
        age = int(age_input)                                            # Convertit l'entrée en entier
        if 0 < age <= 125:                                              # Vérifie que l'âge est réaliste
            break                                                       # Sort de la boucle si l'entrée est valide
        else:
            print("\033[93m⚠️  Veuillez entrer un âge réaliste (entre 1 et 125 ans).\033[0m")
    else:
        print("\033[93m⚠️  Entrée invalide ! Veuillez entrer un nombre entier positif pour l'âge.\033[0m")

# Vérification de la valeur de PI
while True:
    pi_input = input("📝 Entrez la valeur de PI : ").replace(",", ".")  # Supporte la virgule
    try:                                                            
        pi = float(pi_input)                                            # Convertit l'entrée en décimal
        if 3.14 <= pi <= 3.1416:                                        # Vérifie si PI est réaliste
            break                                                       # Sort de la boucle si l'entrée est valide
        else:
            print("\033[93m⚠️  Veuillez entrer une valeur réaliste pour PI (entre 3.14 - 3.1416. Ex: 3.141592).\033[0m")
    except ValueError:
        print("\033[93m⚠️  Entrée invalide ! Veuillez entrer un nombre valide pour PI.\033[0m")


# Afficher les informations saisies
print("\n✅ Résultat : ")
print(f"\033[92m Nom \033[0m: {nom}, \033[92m Âge \033[0m: {age}, \033[92m Valeur de PI \033[0m: {pi:.8f}")
