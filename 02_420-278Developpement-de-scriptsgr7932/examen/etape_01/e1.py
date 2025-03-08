# Demander à l'utilisateur de saisir son nom, son âge et la valeur de PI
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))
pi = float(input("Entrez la valeur de PI : "))

# Afficher les informations avec une f-string
print(f"Nom : {nom}, Âge : {age}, Valeur de PI : {pi:.8f}")