# Exo 7. Élever un nombre à la puissance d'un autre nombre
print("\n\033[92mTapez deux nombres pour calculer le premier nombre élevé à la puissance du deuxième nombre.\033[0m")
print()
nombre1 = float(input("Entrez le premier nombre (base) : "))
nombre2 = float(input("Entrez le deuxième nombre (exposant) : "))
puissance = pow(nombre1, nombre2)
print()
print(nombre1, "élevé à la puissance de", nombre2, "est :", puissance)