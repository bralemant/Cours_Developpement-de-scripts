# Ouvrir un fichier en écriture
chemin_fichier = "/workspaces/Cours_Developpement-de-scripts/semaine05/Cours09/tables_multiplication.txt"
with open(chemin_fichier, "w") as fichier:
    for i in range(1, 21):  # Boucle pour chaque table de multiplication
        fichier.write(f"Table de {i} :\n")
        for j in range(1, 21):  # Multiplication jusqu'à 20
            fichier.write(f"{i} x {j} = {i * j}\n")
        fichier.write("\n")  # Saut de ligne entre les tables

print("Le fichier 'tables_multiplication.txt' a été généré avec succès.")
