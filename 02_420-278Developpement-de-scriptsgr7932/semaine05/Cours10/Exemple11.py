import csv

chemin_fichier = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/semaine05/Cours10/info.csv"

fichier_csv = open(chemin_fichier, newline='')                              # Ouvrir le fichier CSV
lecteur = csv.reader(fichier_csv)                                           # Créer un lecteur CSV
    
entete = next(lecteur, None)                                                # Lire la première ligne (en-tête)
    
for ligne in lecteur:                                                       # Parcourir les lignes restantes
    print(ligne)                                                            # Afficher la ligne