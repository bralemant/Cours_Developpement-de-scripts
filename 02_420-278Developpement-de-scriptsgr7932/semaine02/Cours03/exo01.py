print ("\033[32mExo 1. Évaluation des expressions logiques\033[0m")
#a.
a = not ((12>8) and (14<12))
print("Resultat a :" , a)
#b.
b = (12>8) and not (14<12) or (3<=3)
print("Resultat b :" , b)
#c.
c = (12>8) and (14<12) or not (3<=3)
print("Resultat c :" , c)
#d.
d = (12>8) and not (14<12) or not (3<=3)
print("Resultat d :" , d)

