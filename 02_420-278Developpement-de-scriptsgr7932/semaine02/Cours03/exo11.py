print ("\n\033[32mExo 11. Calcul du nombre de semaines de vacances auquel l'employé a droit selon son ancienneté.\033[0m")
print()
ans = input("Entrez les années d'ancienneté de l'employé: ")
anciennete = float(ans)
if 1 <= anciennete < 6:
    print("L'employé a droit à 3 semaines de vacances.")
elif 6 <= anciennete < 11:
    print("L'employé a droit à 4 semaines de vacances.")    
elif anciennete >= 11:
    print("L'employé a droit à 5 semaines de vacances.") 
else:
    print("L'employé n'a pas droit à des vacances.")   

