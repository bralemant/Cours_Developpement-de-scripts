def convertir_en_nombre(valeur):
    # Essaie de convertir une chaîne en nombre (int ou float).
    # Si la conversion échoue, retourne la chaîne originale.
    if isinstance(valeur, str):                                 # Vérifier si c'est une chaîne
        valeur = valeur.strip('"\'').replace(',', '.')          # Nettoyage
    try:
        return float(valeur) if '.' in valeur else int(valeur)
    except ValueError:
        return valeur                                           # Retourner la chaîne si la conversion échoue

def somme(a=0, b=0):
    # Effectue l'addition si les deux arguments sont numériques.
    # Concatène sous forme de chaînes sinon.
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b                                            # Addition
    return str(a) + " " + str(b)                                # Concaténation avec espace

if __name__ == "__main__":
    print("\n\033[94mÉtape 4. Fonctions. Création et test de la fonction somme (addition ou concaténation).\033[0m\n")

    # Saisie utilisateur
    valeur1 = input("📝 Entrez le premier argument : ")
    valeur2 = input("📝 Entrez le deuxième argument : ")

    # Conversion
    valeur1_converti = convertir_en_nombre(valeur1)
    valeur2_converti = convertir_en_nombre(valeur2)

    # Détermination du type d'opération
    if isinstance(valeur1_converti, (int, float)) and isinstance(valeur2_converti, (int, float)):
        type_combinaison = "🔢 Addition de deux nombres"
    elif isinstance(valeur1_converti, str) and isinstance(valeur2_converti, str):
        type_combinaison = "🔡 Concaténation de deux chaînes"
    else:
        type_combinaison = "🔢 Concaténation d'un nombre et d'une chaîne"

    # Calcul et affichage
    resultat = somme(valeur1_converti, valeur2_converti)
    print(f"\n\033[95m {type_combinaison} :\033[0m")
    print(f"   ✅ Résultat : \033[92m{resultat}\033[0m ({type(resultat).__name__})")
