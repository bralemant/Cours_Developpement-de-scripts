print ("\n\033[32mExo 5. La médiane de trois nombres entiers\033[0m")
print()
nombre1 = input("Tapez un premier nombre entier : ")
nombre2 = input("Tapez un deuxième nombre entier : ")
nombre3 = input("Tapez un troisième nombre entier : ")

nb1 = int(nombre1)
nb2 = int(nombre2)
nb3 = int(nombre3)

liste = [nb1, nb2, nb3]
liste.sort()
medn = liste[1]

print("\033[32mLa médiane est :\033[0m", medn)