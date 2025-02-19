print("\n\033[92mExo 6. Trouver l'index du maximum dans une liste.\033[0m")
print()
# Entrée utilisateur
liste_str = input("Entrez une liste de nombres séparés par des espaces : ")

def indexMax(liste):
    return liste.index(max(liste))  # Trouver le max et son index

# Séparer la chaîne en une liste de sous-chaînes (chaque élément est encore une chaîne)
elements = liste_str.split()

# Initialiser une liste vide pour stocker les nombres convertis
liste = []

# Convertir chaque élément en entier et l'ajouter à la liste
for x in elements:
    nombre = int(x)  # Conversion de chaîne à entier
    liste.append(nombre)  # Ajout à la liste

# Affichage pour vérifier
print("Liste convertie :", liste)

# Affichage du résultat
print("\n\033[92mL'index du maximum est :\033[0m", indexMax(liste))
print()
