print("\n\033[92mExo 3. Générateur de nombres entiers pairs dans une plage spécifique.\033[0m\n")

# 1. Demander à l'utilisateur de saisir deux nombres entiers
nombre1 = input("Saisissez le premier nombre entier pair : ")
nombre2 = input("Saisissez le deuxième nombre entier pair : ")

nb1 = nombre1.strip()
nb2 = nombre2.strip()

# Vérifier que les entrées ne sont pas vides
if not nb1 or not nb2:
    print("❌ Les deux nombres sont obligatoires.")
    exit()

# Vérifier que les entrées sont bien des entiers
if (nb1[0] == '-' and nb1[1:].isdigit()) or nb1.isdigit():
    entier1 = int(nb1)
else:
    print("❌ Veuillez entrer un premier nombre entier pair valide.")
    exit()

if (nb2[0] == '-' and nb2[1:].isdigit()) or nb2.isdigit():
    entier2 = int(nb2)
else:
    print("❌ Veuillez entrer un deuxième nombre entier pair valide.")
    exit()

# 2. Vérifier si les deux entiers sont pairs
if entier1 % 2 != 0 or entier2 % 2 != 0:
    print("❌ Les deux nombres doivent être pairs.")
    exit()

# 3. Vérifier que le deuxième nombre est plus grand que le premier
if entier2 <= entier1:
    print("❌ Le deuxième nombre doit être plus grand que le premier.")
    exit()

# 4. Afficher tous les nombres pairs entre entier1 et entier2 inclus
print("\n✅ Nombres pairs dans la plage spécifiée :")
for i in range(entier1, entier2 + 1, 2):
    print(i)

