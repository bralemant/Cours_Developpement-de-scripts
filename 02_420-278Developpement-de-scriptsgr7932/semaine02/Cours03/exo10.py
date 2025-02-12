print ("\n\033[32mExo 10. Afficher un message de catégorisation selon l'âge.\033[0m")
print()
ans = input("Entrez votre âge: ")
age = int(ans)
if age < 20:
    print("Vous avez moins de 20 ans.")
elif 20 <= age < 30:
    print("Vous avez dans la vingtaine.")
elif 30 <= age < 40:
    print("Vous avez dans la trentaine.")
elif 40 <= age <= 60:
    print("Vous avez entre 40 et 60 ans.")
else:
    print("Vous avez plus de 60 ans.")  
