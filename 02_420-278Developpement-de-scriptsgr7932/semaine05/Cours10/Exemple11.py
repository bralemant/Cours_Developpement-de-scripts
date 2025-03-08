import csv

chemin_fichier = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/semaine05/Cours10/info.csv"

fichier_csv = open(chemin_fichier, newline='')
lecteur = csv.reader(fichier_csv)
    
entete = next(lecteur, None)
    
for ligne in lecteur:
    print(ligne)