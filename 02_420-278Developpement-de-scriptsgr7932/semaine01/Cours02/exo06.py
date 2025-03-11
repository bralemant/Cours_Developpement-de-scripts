# Exo 6. Calcul de la racine carrée d'un nombre
import math

print("\n\033[92mEntrez un nombre pour calculer sa racine carrée.\033[0m")
print()
nombre = float(input("Entrez un nombre : "))
racine_carrée = math.sqrt(nombre)
print("\nLa racine carrée de", nombre, "est :", racine_carrée)