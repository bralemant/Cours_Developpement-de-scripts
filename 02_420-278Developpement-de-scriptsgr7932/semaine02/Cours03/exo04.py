print ("\n\033[32mExo 4. La plus grande des trois valeurs entières\033[0m")
print()
valeur1 = input("Tapez une première valeur entière : ")
valeur2 = input("Tapez une deuxième valeur entière : ")
valeur3 = input("Tapez une troisième valeur entière : ")

val1 = int(valeur1)
val2 = int(valeur2)
val3 = int(valeur3)

if val1 > val2 and val1 > val3:
  plus_grande = val1
elif val2 > val1 and val2 > val3:
  plus_grande = val2
else:
  plus_grande = val3
print("\n\033[32mLa plus grande valeur est :\033[0m", plus_grande)
