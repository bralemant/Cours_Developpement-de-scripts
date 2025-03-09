### Étape 5. Manipulation de fichiers. Un outil interactif pour l'analyse de texte"

import os
fichier = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/examen/etape_05/logfile.txt"

############ Fonctions pour l'analyse de texte ############
# Compter le nombre de lignes dans un fichier
def compter_lignes(fichier):
    f = open(fichier, 'r')
    return sum(1 for _ in f)

# Afficher les lignes avec un numéro de ligne pair
def afficher_lignes_paires(fichier):
    lignes_paires = []
    f = open(fichier, 'r')
    for numero_ligne, ligne in enumerate(f, start=1):
        if numero_ligne % 2 == 0:
            lignes_paires.append(f"Ligne {numero_ligne}: {ligne.strip()}")
    return "\n".join(lignes_paires)

# Compter le nombre de voyelles dans un fichier
def compter_voyelles(fichier):
    voyelles = "aeiouAEIOU"
    compteur = 0
    f = open(fichier, 'r')
    for ligne in f:
        for caractere in ligne:
            if caractere in voyelles:
                compteur += 1
    return compteur

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
        os.system("clear")                                  # Nettoyer l'écran avant d'afficher le menu
        afficher_titre()                                    # Afficher le titre du programme
        print(resultat)                                     # Afficher le résultat de la dernière opération
        print("\n🔍 \033[93m Choisissez une option :\033[0m\n")
        print("📅 \033[96m 1. Compter le nombre de lignes ⏫\033[0m")
        print("🔢 \033[96m 2. Afficher les lignes avec un numéro de ligne pair ⏫\033[0m")
        print("🕒 \033[96m 3. Compter le nombre de voyelles ⏫\033[0m\n")
        print("❌ \033[91m q. Quitter\033[0m\n")
        choix = input("Votre choix : ")

        if choix == "1":
            nombre_lignes = compter_lignes(fichier)
            resultat = f"✅   📅 \033[92m Le fichier contient {nombre_lignes} lignes.\033[0m\n"
        elif choix == "2":
            resultat = "✅   🔢 \033[92m Lignes avec un numéro de ligne pair\033[0m :\n" + afficher_lignes_paires(fichier) + ""
        elif choix == "3":
            nombre_voyelles = compter_voyelles(fichier)
            resultat = f"✅   🕒 \033[92m Le fichier contient {nombre_voyelles} voyelles.\033[0m\n"
        elif choix == "q":
            print("👋 \033[95m Au revoir !\033[0m")
            break
        else:
            resultat = "⚠️  \033[91m Choix invalide. Veuillez réessayer.\033[0m  ⚠️\n"

# Appeler la fonction principale pour l'interface utilisateur
if __name__ == "__main__":                                  
    main()
