print("\n\033[92mExo 4. Volume d'un parallélépipède.\033[0m")
print()
# Entrée utilisateur séparée de la conversion
x1 = input("Entrez la première dimension : ")
dim1 = float(x1)

x2 = input("Entrez la deuxième dimension : ")
dim2 = float(x2)

x3 = input("Entrez la troisième dimension : ")
dim3 = float(x3)

def volBoite(x1, x2, x3):
    return x1 * x2 * x3  # Volume du parallélépipède

# Appel de la fonction et affichage du résultat
print(f"\n\033[92mLe volume de la boîte est :\033[0m {volBoite(dim1, dim2, dim3):.2f}")
