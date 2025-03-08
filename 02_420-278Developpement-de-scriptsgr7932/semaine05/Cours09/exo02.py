print("\n\033[92mExo 2. Ouvrir et lire le fichier /etc/passwd\033[0m")
print()

### Ouvrir et lire le fichier /etc/passwd
## Fonction pour afficher le contenu du fichier /etc/passwd
def afficher_contenu_passwd():
    try:
        fichier = open("/etc/passwd", "r")                  # Ouvrir le fichier en mode lecture
        contenu = fichier.readlines()                       # Lire toutes les lignes du fichier
        for ligne in contenu:                               # Parcourir les lignes
            print(ligne.strip())                            # Affichage sans saut de ligne supplémentaire
    except Exception as e:                                  # Gestion des erreurs
        print(f"Erreur : {e}")                              # Afficher le message d'erreur


## Fonction pour filtrer les lignes contenant les mots-clefs "root", "admin" ou "nobody"
def filtrer_lignes_passwd():
    mots_cles = ["root", "admin", "nobody"]                 # Mots-clefs à rechercher
    try:                                                    
        fichier = open("/etc/passwd", "r")                  # Ouvrir le fichier en mode lecture
        for ligne in fichier:                               # Parcourir les lignes 
            if any(mot in ligne for mot in mots_cles):      # Vérifier si un des mots-clefs est présent
                print(ligne.strip())                        # Afficher la ligne sans saut de ligne supplémentaire
    except Exception as e:                                  # Gestion des erreurs
        print(f"Erreur : {e}")                              # Afficher le message d'erreur

# Exécuter les fonctions
print("\033[94m######## Contenu du fichier /etc/passwd ########\033[0m")
afficher_contenu_passwd()

print("\n\033[94m######## Lignes contenant 'root', 'admin' ou 'nobody' ########\033[0m")
filtrer_lignes_passwd()
