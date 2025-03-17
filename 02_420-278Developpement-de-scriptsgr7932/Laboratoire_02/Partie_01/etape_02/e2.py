#!/usr/bin/env python3
print("\n\033[94mÉtape 2. Convertir un Script Python en Exécutable avec Paramètres \033[0m")
print()
import psutil
import time
import sys

# Nom du processus à surveiller
if len(sys.argv) > 1:
    nom_processus = sys.argv[1]
else:
    nom_processus = input("Veuillez entrer le nom du processus à surveiller : ").strip()
    if not nom_processus:
        print("Erreur : Aucun nom de processus n'a été fourni. Le script va s'arrêter.")
        sys.exit(1)

# Intervalle de vérification (en secondes)
interval = 5

while True:
    processus_trouvé = False
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == nom_processus:
            print(f"✅  Processus {nom_processus} trouvé (PID: {proc.pid})")
            processus_trouvé = True
            break

    if not processus_trouvé:
        print(f"❌  Processus {nom_processus} non trouvé.")
    
    time.sleep(interval)
