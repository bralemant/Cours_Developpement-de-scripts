print("\n\033[92mExo 4. Génération des carrés et des cubes des nombres de 20 à 40. Utilisation d'une boucle while.\033[0m")

n = 20
print("Nombre | Carré | Cube")
print("----------------------")

while n <= 40:
    print(f"{n} | {n**2} | {n**3}")
    n += 1
