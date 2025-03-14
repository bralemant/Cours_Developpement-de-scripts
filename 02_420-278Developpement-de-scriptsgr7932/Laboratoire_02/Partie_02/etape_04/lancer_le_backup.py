import subprocess
import datetime
import os
import sys

# Vérifier si les arguments sont fournis
if len(sys.argv) != 3:
    print("Usage : ./lancer_le_backup.py <chemin/dossier_source> <chemin/dossier_destination_sauvegarde>")
    sys.exit(1)

# Récupérer les paramètres
source_dir = sys.argv[1]  # Premier argument : dossier source
backup_dir = sys.argv[2]  # Deuxième argument : dossier destination

# Vérifier si le dossier source existe
if not os.path.exists(source_dir):
    print(f"Erreur : Le dossier source '{source_dir}' n'existe pas.")
    sys.exit(1)

# Vérifier si le dossier destination existe, sinon le créer
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
    print(f"Dossier destination '{backup_dir}' créé.")

# Obtenir la date actuelle
date_aujourdhui = datetime.date.today()
# Pour tester : décommentez et choisissez une date
# date_aujourdhui = datetime.date(2025, 3, 17)  # Exemple : lundi

jour_semaine = date_aujourdhui.weekday()

# Noms complets des jours en français
jours_complets = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
nom_jour_complet = jours_complets[jour_semaine]

# Nom de l'archive : "comp" pour vendredi, sinon nom complet
nom_jour_archive = "complet" if jour_semaine == 4 else nom_jour_complet
backup_file = os.path.join(backup_dir, f"{nom_jour_archive}.tar")

# Type de sauvegarde pour l'affichage
if jour_semaine in range(0, 4):
    type_sauvegarde = "différentielle"
elif jour_semaine == 4:
    type_sauvegarde = "complète"
else:
    type_sauvegarde = "aucune"

print(f"Date actuelle : {date_aujourdhui}")
print(f"Jour de la semaine : {nom_jour_complet} {type_sauvegarde} ({jour_semaine})")
print(f"Nom de l'archive : {backup_file}")

try:
    if jour_semaine in range(0, 4):  # Lundi à jeudi : différentielle
        print("Début de la sauvegarde différentielle...")
        cmd = ["find", source_dir, "-type", "f", "-mtime", "-1", "-exec", "tar", "-rvf", backup_file, "{}", "+"]
        subprocess.run(cmd, check=True)
        print(f"Sauvegarde différentielle terminée avec succès : {backup_file}")
    elif jour_semaine == 4:  # Vendredi : complète
        print("Début de la sauvegarde complète...")
        cmd = ["tar", "-cvf", backup_file, source_dir, "--exclude=*.tar"]
        subprocess.run(cmd, check=True)
        print(f"Sauvegarde complète terminée avec succès : {backup_file}")
    else:  # Week-end
        print("Aucune sauvegarde prévue le week-end.")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de la création de la sauvegarde : {e}")