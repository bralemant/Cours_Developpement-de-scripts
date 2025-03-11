#!/home/codespace/.python/current/bin/python3
import sys

print("Exo 3. Rappels salutations personnalisées")
print()

# Vérifier si deux arguments sont fournis
if len(sys.argv) != 3:
    print("Usage: ./salut.py <salutation> <nom>")
    sys.exit(1)

salutation = sys.argv[1]
nom = sys.argv[2]

# Afficher le message
print(f"Pour votre rappel: {salutation} {nom}.")
