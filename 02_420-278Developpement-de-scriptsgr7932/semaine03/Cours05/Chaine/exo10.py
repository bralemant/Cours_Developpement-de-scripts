print("\n\033[32mExo 10. Isoler et afficher le deuxième mot d'une chaîne.\033[0m")
print()
chaine = input("Entrez une chaîne de caractères: ")
mots = chaine.split() # Diviser la chaine en mots

if len(mots) >= 2:          # Verifier si la chaine contient au moins deux mots
    isol_2eme_mot = mots[1] # Isoler le deuxième mot
    print("Le deuxième mot est :", isol_2eme_mot)
else:
    print("La chaîne ne contient pas une deuxième mot.")



input("Appuyez sur Entrée pour fermer...")