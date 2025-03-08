print("\n\033[92mExo 7. Calcul de l'âge de chacune des personnes (fichier : info.csv) à la fin de l'année 2020\033[0m")
print()

import csv

# Chemin complet du fichier CSV
chemin_fichier_csv = '/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/semaine05/Cours10/info.csv'

# Ouvrir le fichier CSV
with open(chemin_fichier_csv, newline='') as fichier_csv:
    lecteur = csv.reader(fichier_csv)
    
    # Sauter la ligne d'en-tête
    entete = next(lecteur, None)
    
    # Parcourir les lignes restantes
    for ligne in lecteur:
        # Extraire le prénom et l'année de naissance
        prenom = ligne[1]
        annee_naissance = int(ligne[2])
        
        # Calculer l'âge à la fin de l'année 2020
        age = 2020 - annee_naissance
        
        # Afficher le résultat
        print(f"{prenom} à {age} ans")