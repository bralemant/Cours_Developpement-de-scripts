print("\n\033[32mExo 7. Le mot le plus court dans une phrase donnée\033[0m")
print()

phrase = input("Veuillez entrer une phrase : ")

mots = phrase.split()

plus_court_mot = mots[0]        # Variable pour stocker le mot le plus court
longueur_min = len(mots[0])     # Variable pour stocker la longueur du mot le plus court

# Rechercher le mot le plus court
for mot in mots:                # Pour chaque mot dans la liste de mots de la phrase
    if len(mot) < longueur_min: # Si la longueur du mot actuel est plus petite que la longueur minimale
        longueur_min = len(mot) # Mettre à jour la longueur minimale
        plus_court_mot = mot    # Mettre à jour le mot le plus court 

print("Le mot le plus court est : '" + plus_court_mot + "' avec " + str(longueur_min) + " caractères.")
