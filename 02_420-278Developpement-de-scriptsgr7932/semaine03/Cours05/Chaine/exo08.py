print("\n\033[32mExo 8. Séparer le denier caractère des autres par trois tirets.\033[0m")
print()

chaine = input("Tapez une chaîne de caractères: ")

if len(chaine) > 0:                 # Vérifie si la chaîne n'est pas vide
    premier_partie = chaine[:-1]    # Tous les caractères sauf le dernier
    dernier_car = chaine[-1]        # Le dernier caractère

    resultat = premier_partie + '---' + dernier_car # Ajoute '---' entre les deux parties
    print("Résultat:", resultat)
else:
    print("La chaîne ne peut pas être vide.")


input("Appuyez sur Entrée pour fermer...")