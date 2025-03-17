print("\n\033[94mÉtape 3. Exécuter des commandes de sauvegarde selon le jour en Python \033[0m")
print()
import subprocess
import datetime
import os

# Chemin du répertoire à sauvegarder
source_dir = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/Laboratoire_02/Partie_02/Dossier_Test"
backup_dir = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/Laboratoire_02/Partie_02/Backup_Test"

# Obtenir la date actuelle
date_aujourdhui = datetime.date.today()
# Pour tester : décommentez et choisissez une date
# date_aujourdhui = datetime.date(2025, 3, 17)  # Exemple : lundi

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
    if jour_semaine in range(0, 4):                                                                                         # Lundi à jeudi : différentielle
        print("\n\033[93mDébut de la sauvegarde différentielle...\033[0m")
        cmd = ["find", source_dir, "-type", "f", "-mtime", "-1", "-exec", "tar", "-rvf", backup_file, "{}", "+"]            # Exclure les fichiers .tar
        subprocess.run(cmd, check=True)                                                                                     # Créer une sauvegarde différentielle   
        print("\n✅  \033[92mSauvegarde différentielle terminée avec succès\033[0m")
    elif jour_semaine == 4:                                                                                                 # Vendredi : complète
        print("\n\033[93mDébut de la sauvegarde complète...\033[0m")
        cmd = ["tar", "--exclude=*.tar", "-cvf", backup_file, source_dir]                                                   # Exclure les fichiers .tar
        subprocess.run(cmd, check=True)                                                                                     # Créer une sauvegarde complète  
        print("\n✅  \033[92mSauvegarde complète terminée avec succès\033[0m")
    else:                                                                                                                   # Week-end
        print("\n\033[93mAucune sauvegarde prévue le week-end.\033[0m")
except subprocess.CalledProcessError as e:                                                                                  # Gestion des erreurs 
    print(f"\n⚠️  \033[91mErreur lors de la création de la sauvegarde : {e}  ⚠️\033[0m")