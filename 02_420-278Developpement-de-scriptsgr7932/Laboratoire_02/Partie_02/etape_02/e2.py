print("\n\033[94mÉtape 2. Sauvegarde les fichiers récents en Python avec subprocess \033[0m")
print()
import subprocess

# Chemin du répertoire à sauvegarder
source_dir = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/Laboratoire_02/Partie_02/Dossier_Test"
# Nom du fichier de sauvegarde
backup_file_tar = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/Laboratoire_02/Partie_02/Dossier_Test/diff.tar"

# Commande pour la sauvegarde différentielle
cmd = [
    "find", source_dir, "-type", "f", "-mtime", "-1",
    "-exec", "tar", "-rvf", backup_file_tar, "{}", "+"
]

try:
    subprocess.run(cmd, check=True)                                                                 # Créer une sauvegarde différentielle   
    print("\n✅  \033[92mSauvegarde différentielle créée avec succès\033[0m")                          
    print("\033[93mEmplacement du fichier :\033[0m")
    print(f"'{backup_file_tar}'")
except subprocess.CalledProcessError as e:                                                          # Gestion des erreurs         
    print(f"\n⚠️  \033[91mErreur lors de la création de la sauvegarde: {e}  ⚠️\033[0m")