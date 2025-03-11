print("\n\033[92mExo 2. Conversion de température.\033[0m")
print()

class Temperature:
    def __init__(self, valeur=0):
        self.valeur = valeur

    def C2f(self):
        # Convertir Celsius à Fahrenheit
        return (self.valeur * 9/5) + 32

    def F2c(self):
        # Convertir Fahrenheit à Celsius
        return (self.valeur - 32) * 5/9

# Entrée de l'utilisateur
valeur_temp = float(input("Entrez la valeur de la température : "))
unite = input("Entrez l'unité de la température (C pour Celsius, F pour Fahrenheit) : ").strip().upper()

# Créer un objet Temperature avec la valeur fournie
temp = Temperature(valeur_temp)

# Conversion et affichage des résultats
if unite == "C":
    print(f"\n{valeur_temp}°C équivaut à {temp.C2f():.2f}°F.")
elif unite == "F":
    print(f"\n{valeur_temp}°F équivaut à {temp.F2c():.2f}°C.")
else:
    print("\nUnité non reconnue. Veuillez entrer 'C' pour Celsius ou 'F' pour Fahrenheit.")