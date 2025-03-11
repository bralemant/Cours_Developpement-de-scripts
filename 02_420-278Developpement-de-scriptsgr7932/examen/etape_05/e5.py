### Étape 5. Manipulation de fichiers. Un outil interactif pour l'analyse de texte"

import os
fichier = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/examen/etape_05/logfile.txt"

############ Fonctions pour l'analyse de texte ############
# Compter le nombre de lignes dans le fichier logfile.txt
def compter_lignes(fichier):                                                            # Compter le nombre de lignes dans le fichier
    f = open(fichier, 'r')                                                              # Ouvrir le fichier en mode lecture
    return sum(1 for _ in f)                                                            # Compter le nombre de lignes

# Afficher les lignes avec un numéro de ligne pair
def afficher_lignes_paires(fichier):                                                    # Afficher les lignes avec un numéro de ligne pair
    lignes_paires = []                                                                  # Initialiser une liste vide pour stocker les lignes paires
    f = open(fichier, 'r')                                                              # Ouvrir le fichier en mode lecture
    for numero_ligne, ligne in enumerate(f, start=1):                                   # Parcourir les lignes avec un numéro de ligne
        if numero_ligne % 2 == 0:                                                       # Vérifier si le numéro de ligne est pair
            lignes_paires.append(f"Ligne {numero_ligne}: {ligne.strip()}")              # Ajouter la ligne à la liste
    return lignes_paires                                                                # Retourner la liste des lignes paires

# Compter le nombre de voyelles non accentuées dans le fichier logfile.txt
def compter_voyelles(fichier):                                                          # Compter le nombre de voyelles non accentuées
    voyelles = "aeiouAEIOU"                                                             # Définir les voyelles non accentuées
    compteur = 0                                                                        # Initialiser le compteur de voyelles
    f = open(fichier, 'r')                                                              # Ouvrir le fichier en mode lecture
    for ligne in f:                                                                     # Parcourir chaque ligne du fichier
        for caractere in ligne:                                                         # Parcourir chaque caractère de la ligne 
            if caractere in voyelles:                                                   # Vérifier si le caractère est une voyelle non accentuée
                compteur += 1                                                           # Incrémenter le compteur de voyelles
    return compteur                                                                     # Retourner le nombre de voyelles

############ Fonctions pour l'interface utilisateur ############
# Afficher le titre du programme
def afficher_titre():
    titre = """
📂️ ######################################################
#                                                       #
#   🌟 \033[92m** ANALYSEUR DU FICHIER TEXTE 'LOGFILE' **\033[0m 🌟    #
#                                                       #
#########################################################
    """
    print(titre)

# Fonction principale pour l'interface utilisateur
def main():
    resultat = ""
    while True:
        os.system("clear")                                                              # Nettoyer l'écran avant d'afficher le menu
        afficher_titre()                                                                # Afficher le titre du programme
        print(resultat)                                                                 # Afficher le résultat de la dernière opération
        print("\n🔍 \033[93m Choisissez une option :\033[0m\n")
        print("📅 \033[96m 1. Compter le nombre de lignes ⏫\033[0m")
        print("🔢 \033[96m 2. Afficher les lignes avec un numéro de ligne pair ⏫\033[0m")
        print("🕒 \033[96m 3. Compter le nombre de voyelles ⏫\033[0m\n")
        print("❌ \033[91m q. Quitter\033[0m\n")
        choix = input("Votre choix : ")

        if choix == "1":
            nombre_lignes = compter_lignes(fichier)
            resultat = f"✅   📅 \033[92m Le fichier contient \033[0m {nombre_lignes} \033[92m lignes.\033[0m\n"
        elif choix == "2":
            lignes_paires = afficher_lignes_paires(fichier)
            resultat = "\n".join(lignes_paires) + f"\n\n✅   🔢 \033[92m Lignes avec un numéro de ligne pair\033[0m ({len(lignes_paires)} trouvées) ⬆️\n"
        elif choix == "3":
            nombre_voyelles = compter_voyelles(fichier)
            resultat = f"✅   🕒 \033[92m Le fichier contient \033[0m {nombre_voyelles} \033[92m voyelles non accentuées.\033[0m\n"
        elif choix == "q":
            print("\n👋 \033[95m Au revoir !\033[0m")
            break
        else:
            resultat = "⚠️  \033[91m Choix invalide. Veuillez réessayer.\033[0m  ⚠️\n"

# Appeler la fonction principale pour l'interface utilisateur
if __name__ == "__main__":                                  
    main()
