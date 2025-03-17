print("\n\033[94mÉtape 4. Paramétrer le Dossier Source et la Destination du fichier en Python. Faire un CRON job \033[0m")
print()
import subprocess
import datetime
import os
import sys

# Vérifier si les arguments sont fournis
if len(sys.argv) != 3:
    print("\n⚠️  \033[93mTapez una ligne de commande dans le terminal avec la syntaxe suivante :\033[0m")
    print("./lancer_le_backup.py <chemin/dossier_source> <chemin/dossier_destination_sauvegarde>\033[0m")
    print("\n\033[93mN'oubliez pas d'écrire correctement l'emplacement du dossier source et l'emplacement du dossier de destination\033[0m")
    sys.exit(1)

# Récupérer les paramètres
source_dir = sys.argv[1]  # Premier argument : dossier source
backup_dir = sys.argv[2]  # Deuxième argument : dossier destination

# Vérifier si le dossier source existe
if not os.path.exists(source_dir):
    print(f"\n⚠️  \033[91mErreur : Le dossier source '{source_dir}' n'existe pas.\033[0m")
    sys.exit(1)

# Vérifier si le dossier destination existe, sinon le créer
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
    print(f"\n✅  \033[92mDossier destination '{backup_dir}' créé.\033[0m")

# Obtenir la date actuelle
date_aujourdhui = datetime.date.today()
# Pour tester : décommentez et choisissez une date
#date_aujourdhui = datetime.date(2025, 3, 21)  # Exemple : lundi

jour_semaine = date_aujourdhui.weekday()

# Noms complets des jours en français
jours_complets = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
nom_jour_complet = jours_complets[jour_semaine]

# Générer le nom de l'archive avec strftime et type de sauvegarde
nom_jour = date_aujourdhui.strftime("%a").lower()
jours_map = {"mon": "lu", "tue": "ma", "wed": "me", "thu": "je", "fri": "comp", "sat": "sa", "sun": "di"}
nom_jour = jours_map.get(nom_jour, "inconnu")
backup_file = os.path.join(backup_dir, f"{nom_jour}.tar")

# Type de sauvegarde pour l'affichage
if jour_semaine in range(0, 4):
    type_sauvegarde = "différentielle"
elif jour_semaine == 4:
    type_sauvegarde = "complète"
else:
    type_sauvegarde = "aucune"

print(f"📅  Date actuelle : \033[96m{date_aujourdhui}\033[0m")
print(f"📆  Jour de la semaine : \033[96m{nom_jour_complet} {type_sauvegarde} ({jour_semaine})\033[0m")
print(f"📂  Nom du fichier : \033[96m{nom_jour}.tar\033[0m")
print(f"📁  Emplacement du fichier : \033[94m {backup_file}\033[0m")

try:
    if jour_semaine in range(0, 4):  # Lundi à jeudi : différentielle
        print("\n\033[93mDébut de la sauvegarde différentielle...\033[0m")
        cmd = ["find", source_dir, "-type", "f", "-mtime", "-1", "-exec", "tar", "-rvf", backup_file, "{}", "+"]
        subprocess.run(cmd, check=True)
        print("\n✅  \033[92mSauvegarde différentielle terminée avec succès : \033[0m")
    elif jour_semaine == 4:  # Vendredi : complète
        print("\n\033[93mDébut de la sauvegarde complète...\033[0m")
        cmd = ["tar", "--exclude=*.tar", "-cvf", backup_file, source_dir]
        subprocess.run(cmd, check=True)
        print("\n✅  \033[92mSauvegarde complète terminée avec succès : \033[0m")
    else:  # Week-end
        print("\n\033[93mAucune sauvegarde prévue le week-end.\033[0m")
except subprocess.CalledProcessError as e:
    print(f"\n⚠️  \033[91mErreur lors de la création de la sauvegarde : {e}\033[0m")