#!/usr/bin/env python3
print("\n\033[94mÉtape 3. Surveiller Plusieurs Processus depuis un Fichier avec Python \033[0m")
print()
import psutil
import time
 
### Lit les processus à surveiller depuis un fichier texte"""
def lire_processus_fichier(fichier_liste="/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/Laboratoire_02/Partie_01/etape_03/processus_a_surveiller.txt"):
    try:
        with open(fichier_liste, 'r') as fichier:
            processus = [ligne.strip() for ligne in fichier if ligne.strip()]                       # Lit les lignes, supprime les espaces et filtre les lignes vides
        
        if not processus:
            print("⚠️  \033[91mErreur : Le fichier est vide.\033[0m")
            print("Écrire la liste des processus à surveiller dans le fichier 'processus_a_surveiller.txt'")
            print("\033[93mEmplacement du fichier :\033[0m")
            print(f"'{fichier_liste}'")
            return None
        return processus
   


    except FileNotFoundError:
        print("⚠️  \033[91mErreur : Le fichier 'processus_a_surveiller.txt' n'a pas été trouvé  \033[0m⚠️")
        print("\033[93mEmplacement du fichier :\033[0m")
        print(f"'{fichier_liste}'")
        return None
    except PermissionError:
        print("⚠️  \033[91mErreur : Permission refusée pour lire le fichier 'processus_a_surveiller.txt'  \033[0m⚠️")
        print("\033[93mEmplacement du fichier :\033[0m")
        print(f"'{fichier_liste}'")
        return None
    except Exception as e:
        print(f"⚠️  \033[91mErreur inattendue lors de la lecture du fichier : {str(e)}  ⚠️  \033[0m")
        return None

# Intervalle de vérification (en secondes)
interval = 5

# Lecture initiale des processus
liste_processus = lire_processus_fichier()

if liste_processus is None:
    exit(1)

while True:
    for nom_processus in liste_processus:
        processus_trouvé = False
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == nom_processus:
                print(f"✅  Processus {nom_processus} trouvé (PID: {proc.pid})")
                processus_trouvé = True
                break
        
        if not processus_trouvé:
            print(f"❌  Processus {nom_processus} non trouvé.")
    
    print("-" * 50)  # Séparateur entre chaque cycle
    time.sleep(interval)