# Exo 4. Vérification si un nombre est pair ou impair
print("\n\033[92mDéterminer si le nombre est pair ou impair.\033[0m")
print()
nombre = int(input("Entrez un nombre entier : "))
est_pair = (nombre % 2 == 0)
print("\nLe nombre est pair :", est_pair)