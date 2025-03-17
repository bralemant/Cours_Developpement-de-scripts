print("\n\033[94mÉtape 1. Créer une Archive Tar en Python avec Subprocess \033[0m")
print()
import subprocess

# Chemin du répertoire à sauvegarder
source_dir = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/Laboratoire_02/Partie_02/Dossier_Test"
# Nom du fichier de sauvegarde
backup_file_tar = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/Laboratoire_02/Partie_02/Dossier_Test/comp.tar"

# Commande tar exécutée via subprocess
try:
    subprocess.run(["tar", "-cvf", backup_file_tar, source_dir], check=True)
    print("\n✅  \033[92mSauvegarde complète créée avec succès\033[0m")
    print("\033[93mEmplacement du fichier :\033[0m")
    print(f"'{backup_file_tar}'")
except subprocess.CalledProcessError as e:
    print(f"\n⚠️  \033[91mErreur lors de la création de la sauvegarde: {e}  ⚠️\033[0m")