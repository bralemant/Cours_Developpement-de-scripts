def afficher_contenu_passwd():
    try:
        with open("/etc/passwd", "r") as fichier:
            contenu = fichier.readlines()
            for ligne in contenu:
                print(ligne.strip())  # Affichage sans saut de ligne supplémentaire
    except Exception as e:
        print(f"Erreur : {e}")

def filtrer_lignes_passwd():
    mots_cles = ["root", "admin", "nobody"]
    try:
        with open("/etc/passwd", "r") as fichier:
            for ligne in fichier:
                if any(mot in ligne for mot in mots_cles):
                    print(ligne.strip())
    except Exception as e:
        print(f"Erreur : {e}")

# Exécuter les fonctions
print("=== Contenu du fichier /etc/passwd ===")
afficher_contenu_passwd()

print("\n=== Lignes contenant 'root', 'admin' ou 'nobody' ===")
filtrer_lignes_passwd()
