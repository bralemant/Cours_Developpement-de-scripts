print("\n\033[92mExo 12. Nombre de jours dans un mois.\033[0m")
print()
# Entrée utilisateur
annee_str = input("Entrez l'année : ")
annee = int(annee_str)

mois_str = input("Entrez le mois (1-12) : ")
mois = int(mois_str)

def nbJour(annee, mois):
    if mois == 2:  # Février, vérifier si bissextile
        if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
            return 29
        return 28
    elif mois in [1, 3, 5, 7, 8, 10, 12]:  # Mois à 31 jours
        return 31
    else:  # Mois à 30 jours
        return 30

# Affichage du résultat
print(f"\nLe mois {mois} de l'année {annee} a {nbJour(annee, mois)} jours.")
print()
