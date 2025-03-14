import psutil
import time

# Nom du processus à surveiller
nom_processus = "sshd"

# Intervalle de vérification (en secondes)
interval = 5

while True:
    processus_trouvé = False
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == nom_processus:
            print(f"Processus {nom_processus} trouvé (PID: {proc.pid})")
            processus_trouvé = True
            break

    if not processus_trouvé:
        print(f"Processus {nom_processus} non trouvé.")
    
    time.sleep(interval)