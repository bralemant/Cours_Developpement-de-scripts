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
    subprocess.run(cmd, check=True)
    print(f"Sauvegarde différentielle créée avec succès: {backup_file_tar}")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de la création de la sauvegarde: {e}")