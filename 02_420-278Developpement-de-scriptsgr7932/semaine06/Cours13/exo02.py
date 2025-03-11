#!/home/codespace/.python/current/bin/python3
import subprocess

print("Exo 2. Lister et filtrer les fichiers Python dans le répertoire courant")
print()

####### Script pour lister et filtrer les fichiers Python dans le répertoire courant #######

# Exécuter la commande 'pwd' pour obtenir le répertoire courant
pwd_process = subprocess.Popen(["pwd"], stdout=subprocess.PIPE, text=True)

# Exécuter la commande 'ls -l' pour lister les fichiers avec des détails
ls_process = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE, text=True)

# Exécuter la commande 'grep .py$' pour filtrer les fichiers se terminant par '.py'
grep_process = subprocess.Popen(["grep", ".py$"], stdin=ls_process.stdout, stdout=subprocess.PIPE, text=True)

# Récupérer la sortie et les erreurs de la commande 'grep'
output, error = grep_process.communicate()

# Afficher le répertoire courant obtenu avec 'pwd'
print("Allo depuis", pwd_process.communicate())

# Afficher la sortie filtrée par 'grep'
print("Ouput : \n", output)

# Afficher les erreurs s'il y en a
print("Erreur : ", error)