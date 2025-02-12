print("\n\033[32mExo 1. Vérifiez si la chaîne d'entrée représente un entier.\033[0m")
print()
chaine = input("Tapez une chaîne de caractères: ")

# Vérifier si la chaîne représente un entier avec isdigit()
if chaine[0] == '-' or chaine[0] == '+':
    if len(chaine) > 1 and chaine[1:].isdigit(): # Vérifie si la chaîne est composée de chiffres
        print("La chaîne représente un entier.")
    else:
        print("La chaîne ne représente pas un entier.")
else:
    if chaine.isdigit(): # Vérifie si la chaîne est composée de chiffres
        print("La chaîne représente un entier.")
    else:
        print("La chaîne ne représente pas un entier.")
