# Exo 5. Utilisation des opérateurs logiques
print("\n\033[92mÉvaluer plusieurs conditions avec des opérateurs logiques.\033[0m")
print("\n\033[93mAttention !!!\033[0m \nTapez l'argument exactement comme indiqué, sinon l'argument sera considéré comme 'False'.")
print()
a = input("Tapez en majuscules TRUE ou FALSE pour a : ") == "TRUE"
b = input("Tapez en majuscules TRUE ou FALSE pour b : ") == "TRUE"
print("\n\033[92mRésultats de la logique booléene :\033[0m")
print("a ET b :", a and b)
print("a OU b :", a or b)
print("NON a :", not a)
print("NON b :", not b)