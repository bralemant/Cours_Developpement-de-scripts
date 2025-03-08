def somme(a=0, b=0):
    # Convertir les arguments en nombres si possible
    try:
        a = int(a) if isinstance(a, str) and a.isdigit() else float(a) if isinstance(a, str) else a
        b = int(b) if isinstance(b, str) and b.isdigit() else float(b) if isinstance(b, str) else b
    except (ValueError, TypeError):
        return "Erreur : Les arguments doivent être des nombres ou des chaînes représentant des nombres."

    # Retourner la somme
    return a + b

# Tester la fonction avec différents types d'arguments
print(somme(3, 5))          # Deux nombres
print(somme("4", "6"))      # Deux chaînes de caractères
print(somme("2", 3))        # Une chaîne et un nombre
print(somme(1.5, 2.5))      # Deux nombres à virgule flottante
print(somme("abc", 3))      # Test d'erreur