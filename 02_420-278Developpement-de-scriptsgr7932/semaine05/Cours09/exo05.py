print("\n\033[92mExo 5. Génération d'un fichier texte contenant les tables de multiplication de 1 à 20\033[0m")
print()

chemin_fichier = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/semaine05/Cours09/tables_multiplication.txt"
# Vérifier si le fichier 'tables_multiplication.txt' existe ou non
try:
    open(chemin_fichier, "r")                               # Ouvrir le fichier en mode lecture
    fichier_existe = True                                   # Si le fichier existe
except FileNotFoundError:                                   # Gestion des erreurs
    fichier_existe = False                                  # Si le fichier n'existe pas

# Demande de confirmation si le fichier existe
if fichier_existe:
    reponse = input(f"Le fichier 'tables_multiplication.txt' existe déjà. Voulez-vous le remplacer ? (o/n) : ").strip().lower()
    if reponse != 'o':
        print("\n\033[91mOpération annulée. Le fichier n'a pas été modifié.\033[0m")
        exit()

# Génération des tables de multiplication
fichier = open(chemin_fichier, "w")                         # Ouvrir le fichier en mode écriture
for i in range(1, 21):                                      # Boucle pour chaque table de multiplication
    fichier.write("\n")                                     # Saut de ligne entre les tables
    fichier.write(f"Table de {i} :\n")                      # En-tête de la table
    for j in range(1, 21):                                  # Multiplication jusqu'à 20
        fichier.write(f"{i} x {j} = {i * j}\n")             # Écrire la multiplication 
        
print("\n\033[92mLe fichier 'tables_multiplication.txt' a été généré avec succès.\033[0m")
print(f"\033[96mChemin du fichier \033[0m: {chemin_fichier}")