print("\n\033[92mExo 1. Ouvrir et lire le fichier inform.txt.\033[0m")
print()

chemin_fichier = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/semaine05/Cours09/inform.txt"
fichier = open(chemin_fichier, "r")                 # Ouvrir le fichier en mode lecture
contenu = fichier.read()                            # Lire le contenu du fichier

print(contenu)                                      # Afficher le contenu du fichier