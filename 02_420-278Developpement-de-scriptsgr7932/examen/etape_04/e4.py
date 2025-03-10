print("\n\033[94mÉtape 4. Fonctions. Création et test de la fonction somme.\033[0m\n")
print()

# Demander à l'utilisateur d'entrer les deux valeurs
valeur1 = input("📝 Entrez le premier argument : ")
valeur2 = input("📝 Entrez le deuxième argument : ")

### Fonction pour nettoyer et convertir une chaîne en nombre si possible
def convertir_en_nombre(valeur):
    if type(valeur) == str:                                     # Vérifier si la valeur est une chaîne
        valeur = valeur.strip('"\'')                            # Supprime les guillemets doubles ou simples
    try:
        return float(valeur) if '.' in valeur else int(valeur)  # Convertir en décimal si le point est présent, sinon en entier
    except ValueError:
        return valeur                                           # Si la conversion échoue, retourne la valeur originale

# Convertir les valeurs d'entrée en nombres si possible
valeur1_converti = convertir_en_nombre(valeur1)
valeur2_converti = convertir_en_nombre(valeur2)

# Déterminer le type d'opération basé sur les types convertis
if type(valeur1_converti) in (int, float) and type(valeur2_converti) in (int, float):
    type_combinaison = "🔢 Addition de deux nombres"
elif type(valeur1_converti) == str and type(valeur2_converti) == str:
    type_combinaison = "🔡 Concaténation de deux chaînes"
elif type(valeur1_converti) in (int, float) and type(valeur2_converti) == str:
    type_combinaison = "🔢 Concaténation d'un nombre et d'une chaîne"
elif type(valeur1_converti) == str and type(valeur2_converti) in (int, float):
    type_combinaison = "🔢 Concaténation d'une chaîne et d'un nombre"
else:
    type_combinaison = "⚠️ Type non pris en charge"

### Fonction somme pour ajouter deux valeurs
# Si l'un des valeurs est une chaîne, convertir les deux en chaînes
def somme(a=0, b=0):
    if type(a) == str or type(b) == str:                # Vérifier si a ou b est une chaîne
        a = str(a)
        b = str(b)
        resultat = a + " " + b                          # Concaténation avec espace
# Sinon, ajouter les deux valeurs numériques
    else:
        resultat = a + b                                # Addition numérique

# Afficher le résultat
    print(f"\n\033[95m {type_combinaison} :\033[0m")
    print(f"   ✅ Résultat : \033[92m{resultat}\033[0m ({type(resultat).__name__})")
    return resultat

# Appeler la fonction avec les valeurs converties
somme(valeur1_converti, valeur2_converti)