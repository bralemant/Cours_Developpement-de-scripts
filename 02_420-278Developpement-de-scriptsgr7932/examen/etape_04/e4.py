print("\n\033[94mÉtape 4. Fonctions. Création et test de la fonction somme (addition ou concaténation).\033[0m\n")
print()

# Demander à l'utilisateur d'entrer les deux arguments
arg1 = input("📝 Entrez le premier argument : ")
arg2 = input("📝 Entrez le deuxième argument : ")

### Fonction pour nettoyer et convertir une chaîne en nombre si possible
def convertir_en_nombre(valeur):
    if type(valeur) == str:                                                             # Vérifier si l'argument est une chaîne
        valeur = valeur.strip('"\'').replace(',', '.')                                  # Supprime les guillemets et remplace les virgules par des points
    try:
        return float(valeur) if '.' in valeur else int(valeur)                          # Convertir en décimal si le point est présent, sinon en entier
    except ValueError:
        return valeur                                                                   # Si la conversion échoue, retourne l'argument originale

# Convertir les arguments d'entrée en nombres si possible
arg1_converti = convertir_en_nombre(arg1)
arg2_converti = convertir_en_nombre(arg2)

# Déterminer le type d'opération basé sur les types des arguments convertis
if type(arg1_converti) in (int, float) and type(arg2_converti) in (int, float):
    type_combinaison = "🔢 Addition de deux nombres"
elif type(arg1_converti) == str and type(arg2_converti) == str:
    type_combinaison = "🔡 Concaténation de deux chaînes"
elif type(arg1_converti) in (int, float) and type(arg2_converti) == str:
    type_combinaison = "🔢 Concaténation d'un nombre et d'une chaîne"
elif type(arg1_converti) == str and type(arg2_converti) in (int, float):
    type_combinaison = "🔢 Concaténation d'une chaîne et d'un nombre"
else:
    type_combinaison = "⚠️ Type non pris en charge"

### Fonction somme pour ajouter deux arguments
# Si l'un des arguments est une chaîne, convertir les deux en chaînes
def somme(a=0, b=0):
    if type(a) == str or type(b) == str:                                                # Vérifier si a ou b est une chaîne
        a = str(a)
        b = str(b)
        resultat = a + " " + b                                                          # Concaténation avec espace
# Sinon, ajouter les deux valeurs numériques
    else:
        resultat = a + b                                                                # Addition numérique

# Afficher le résultat
    print(f"\n\033[95m {type_combinaison} :\033[0m")
    print(f"   ✅ Résultat : \033[92m{resultat}\033[0m ({type(resultat).__name__})")
    return resultat

# Appeler la fonction avec les arguments converties
somme(arg1_converti, arg2_converti)