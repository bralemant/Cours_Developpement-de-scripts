nb_req_curr = 100
nb_req_past = 1000

if nb_req_curr > nb_req_past :
  print("VRAI. La semaine passée était moins intense.")

if nb_req_past > nb_req_curr :
  print("FAUX. La semaine passée était plus intense.")



note = 5.5

if note < 5 :
  print("F")
elif note >= 6 :
  print("")


print(f"""oneliner challenge : Le plus petit nombre est {min(int(input("entrez un 1e nombre entier: ")), int(input("entrez un 2e nombre entier: ")))}""")