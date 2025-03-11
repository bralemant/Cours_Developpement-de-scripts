print("\n\033[32mExo 6. Le mot le plus long dans une phrase donnée\033[0m")
print()

phrase = input("Veuillez entrer une phrase : ")

mots = phrase.split()           # Diviser la phrase en mots

plus_long_mot = mots[0]         # Variable pour stocker le mot le plus long
longueur_max = len(mots[0])     # Variable pour stocker la longueur du mot le plus long

# Rechercher le mot le plus long
for mot in mots:
    if len(mot) > longueur_max: # Si la longueur du mot actuel est plus grande que la longueur maximale
        longueur_max = len(mot) # Mettre à jour la longueur maximale
        plus_long_mot = mot     # Mettre à jour le mot le plus long

print("La mot le plus long est : '" + plus_long_mot + "' avec " + str(longueur_max) + " caractères.")
