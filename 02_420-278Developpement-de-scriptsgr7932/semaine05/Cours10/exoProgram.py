print("\n\033[92mExo Program. Rechercher un utilisateur et ses ID dans le fichier /etc/passwd \033[0m")
print()

import sys
# Fonction principale pour rechercher un utilisateur dans le fichier /etc/passwd
def main():
    if len(sys.argv) != 2:
        username = input("Veuillez entrer le nom d'utilisateur à rechercher: ")
    else:
        username = sys.argv[1]
# Ouvrir et lire le fichier /etc/passwd
    try:
        passwd_file = open('/etc/passwd', 'r')
        for line in passwd_file:
            fields = line.strip().split(':')
            if fields[0] == username:
                user_id = fields[2]
                group_id = fields[3]
                print(f"\nUtilisateur: {username}, ID utilisateur: {user_id}, ID de groupe: {group_id}")
                return
        print(f"\n\033[91mL'utilisateur '{username}' n'a pas été trouvé.\033[0m")
    except FileNotFoundError:
        print("Le fichier /etc/passwd n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

# Réexécuter la fonction principale
if __name__ == "__main__":
    main()