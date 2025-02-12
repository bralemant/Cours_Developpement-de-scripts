print("\n\033[92mExo 1. Afficher tous les entiers impairs compris entre 11 et 31 inclusive.\033[0m")

# Utilisation d'une boucle for
print("\n\033[7mUtilisation d'une boucle for\033[0m")

for i in range(11, 32):     # Pour chaque nombre entre 11 et 31
    if i % 2 != 0:          # Verifier si le nombre est impair
        print(i)


# Utilisation d'une boucle while
print("\n\033[7mUtilisation d'une boucle while\033[0m")

i = 11                      # Initialiser i à 11
while i <= 31:              # Tant que i est inférieur ou égal à 31
    if i % 2 != 0:          # Vérifier si le nombre est impair
        print(i)            # Afficher le nombre
    i += 1                  # Incrémenter i de 1
