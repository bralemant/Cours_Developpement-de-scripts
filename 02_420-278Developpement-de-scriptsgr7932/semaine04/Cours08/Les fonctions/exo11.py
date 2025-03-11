print("\n\033[92mExo 11. Trouver le premier jour du mois.\033[0m")
print()
# Entrée utilisateur
annee_str = input("Entrez l'année : ")
annee = int(annee_str)

mois_str = input("Entrez le mois (1-12) : ")
mois = int(mois_str)

from datetime import date
def premierJour(annee, mois):
    return date(annee, mois, 1).weekday()  # Jour de la semaine

# Affichage du résultat
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
print("\nLe premier jour du mois est :", jours[premierJour(annee, mois)])
print()
