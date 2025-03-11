# Exo 8. Calcul du sinus, cosinus et tangente d'un angle en radians
import math

print("\n\033[92mCalcul pour obtenir le sinus, le cosinus et la tangente d'un angle en radians.\033[0m")
print()
angle = float(input("Entrez un angle en radians \033[92m(Rappel : \033[93mradians = degrés * π/180) : \033[0m"))
sinus = math.sin(angle)
cosinus = math.cos(angle)
tangente = math.tan(angle)
print("\n\033[92mRésultats :\033[0m")
print("Sinus :", sinus)
print("Cosinus :", cosinus)
print("Tangente :", tangente)