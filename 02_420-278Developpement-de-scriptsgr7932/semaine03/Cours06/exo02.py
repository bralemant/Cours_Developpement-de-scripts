print("\n\033[92mExo 2. Afficher tous les entiers compris entre deux nombres entiers.\033[0m")
print()

nb1 = input("Entrez le premier nombre entier: ")
nb2 = input("Entrez le deuxième nombre entier: ")

nombre1 = int(nb1)
nombre2 = int(nb2)

# Afficher les entiers compris entre nombre1 et nombre2
print(f"\nLes entiers compris entre {nombre1} et {nombre2} sont:")  
for i in range(nombre1, nombre2 + 1):       # +1 pour inclure nombre2
    print(i)                                # Afficher chaque nombre
