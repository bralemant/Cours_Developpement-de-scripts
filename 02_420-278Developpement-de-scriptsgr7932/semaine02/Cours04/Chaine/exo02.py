print("\n\033[32mExo 2. Met en majuscule la première lettre d'un mot.\033[0m")
print()
mot = input("Entrez n'importe quel mot sans : ")

if mot:
    if mot[0].isalpha():        # Vérifie si le premier caractère est une lettre
        print(mot.capitalize()) # Met en majuscule la première lettre du mot
    else:
        print("Veuillez entrer un mot valide (uniquement des lettres).")
else:
    print("Veuillez entrer un mot.")