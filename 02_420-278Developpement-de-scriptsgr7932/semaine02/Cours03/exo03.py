print("\n\033[32mExo 3. Calcul de note sur 20 en pourcentage et mention pour un étudiant\033[0m")
print()
note20 = input("Entrez la note de l'étudiant (sur 20) : ")
note = float(note20)

note_pct = (note / 20) * 100

print("La note est :", note_pct, "%")

if note_pct > 60:
  print("\033[32mBravo!\033[0m")