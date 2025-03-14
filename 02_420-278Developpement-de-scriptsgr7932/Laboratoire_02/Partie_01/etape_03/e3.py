#!/usr/bin/env python3
import psutil
import time
 
### Lit les processus à surveiller depuis un fichier texte"""
def lire_processus_fichier(fichier_liste="/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/Laboratoire_02/Partie_01/etape_03/processus_a_surveiller.txt"):
    try:
        with open(fichier_liste, 'r') as fichier:
            processus = [ligne.strip() for ligne in fichier if ligne.strip()]                       # Lit les lignes, supprime les espaces et filtre les lignes vides
        
        if not processus:
            print("Erreur : Le fichier est vide")
            return None
        return processus
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier_liste}' n'a pas été trouvé")
        return None
    except PermissionError:
        print(f"Erreur : Permission refusée pour lire le fichier '{fichier_liste}'")
        return None
    except Exception as e:
        print(f"Erreur inattendue lors de la lecture du fichier : {str(e)}")
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
                print(f"Processus {nom_processus} trouvé (PID: {proc.pid})")
                processus_trouvé = True
                break
        
        if not processus_trouvé:
            print(f"Processus {nom_processus} non trouvé.")
    
    print("-" * 50)  # Séparateur entre chaque cycle
    time.sleep(interval)