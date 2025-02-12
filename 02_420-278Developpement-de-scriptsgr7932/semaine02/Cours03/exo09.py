print("\n\033[32mExo 9. Selon l'âge, affichez un message indiquant que vous êtes majeur ou mineur.\033[0m")
print()
ans = input("Entrez votre âge: ")

age = int(ans)

if age >= 18:
    print(f"\nVous avez {age}; vous êtes donc majeur.")  
else:
    print(f"\nVous avez {age}; vous êtes donc mineur.") 