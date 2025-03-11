print ("\n\033[32mExo 2. Comparez deux nombres et afficher le plus petit\033[0m")
print()
nombre1 = input("Tapez un premier nombre : ")
nombre2 = input("Tapez un deuxième nombre : ")

nb1 = float(nombre1)
nb2 = float(nombre2)

if nb1 < nb2:
  plus_petit = nb1
else:
  plus_petit = nb2
print("\nLe plus petit nombre est :", plus_petit)
