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
    for ligne in lecteur:                                                   # Parcourir les lignes du fichier
        prenom = ligne[1]                                                   # Récupérer le prénom
        annee_naissance = int(ligne[2])                                     # Récupérer l'année de naissance
        age = 2020 - annee_naissance                                        # Calculer l'âge
        
        # Afficher le résultat
        print(f"{prenom} à {age} ans")