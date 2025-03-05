# Ouvrir et lire le fichier /etc/passwd
with open("/etc/passwd", "r") as fichier:
    for ligne in fichier:
        print(ligne, end="")  # end="" pour éviter les sauts de ligne en double


# Définir les mots-clés à rechercher
mots_cles = ["root", "admin", "nobody"]

# Lire et filtrer les lignes du fichier
with open("/etc/passwd", "r") as fichier:
    for ligne in fichier:
        if any(mot in ligne for mot in mots_cles):
            print(ligne, end="")
