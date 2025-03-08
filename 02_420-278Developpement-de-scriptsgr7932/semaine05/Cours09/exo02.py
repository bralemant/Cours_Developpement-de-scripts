# Ouvrir et lire le fichier /etc/passwd
with open("/etc/passwd", "r") as fichier:
    for ligne in fichier:
        print(ligne, end="")  # end="" pour éviter les sauts de ligne en double



