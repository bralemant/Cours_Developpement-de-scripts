print("\n\033[94mÉtape 5. Manipulation de fichiers. Un outil interactif pour l'analyse de texte\033[0m\n")
print()

def compter_lignes(fichier):
    """Compte le nombre de lignes dans le fichier."""
    with open(fichier, 'r') as f:
        return sum(1 for _ in f)

def afficher_lignes_paires(fichier):
    """Affiche les lignes avec un numéro de ligne pair."""
    with open(fichier, 'r') as f:
        for numero_ligne, ligne in enumerate(f, start=1):
            if numero_ligne % 2 == 0:
                print(f"Ligne {numero_ligne}: {ligne.strip()}")

def compter_voyelles(fichier):
    """Compte le nombre de voyelles dans le fichier."""
    voyelles = "aeiouAEIOU"
    compteur = 0
    with open(fichier, 'r') as f:
        for ligne in f:
            for caractere in ligne:
                if caractere in voyelles:
                    compteur += 1
    return compteur

def main():
    fichier = "/workspaces/Cours_Developpement-de-scripts/02_420-278Developpement-de-scriptsgr7932/examen/etape_05/logfile.txt"  # Remplacez par le nom de votre fichier

    while True:
        print("\nChoisissez une option :")
        print("1. Compter le nombre de lignes")
        print("2. Afficher les lignes avec un numéro de ligne pair")
        print("3. Compter le nombre de voyelles")
        print("4. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            nombre_lignes = compter_lignes(fichier)
            print(f"Le fichier contient {nombre_lignes} lignes.")
        elif choix == "2":
            print("Lignes avec un numéro de ligne pair :")
            afficher_lignes_paires(fichier)
        elif choix == "3":
            nombre_voyelles = compter_voyelles(fichier)
            print(f"Le fichier contient {nombre_voyelles} voyelles.")
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()