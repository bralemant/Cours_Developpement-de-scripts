import sys

def main():
    # Demander le nom d'utilisateur à l'utilisateur
    if len(sys.argv) != 2:
        username = input("Veuillez entrer le nom d'utilisateur à rechercher: ")
    else:
        username = sys.argv[1]

    try:
        with open('/etc/passwd', 'r') as passwd_file:
            for line in passwd_file:
                fields = line.strip().split(':')
                if fields[0] == username:
                    user_id = fields[2]
                    group_id = fields[3]
                    print(f"Utilisateur: {username}, ID utilisateur: {user_id}, ID de groupe: {group_id}")
                    return

            print(f"L'utilisateur '{username}' n'a pas été trouvé.")
    except FileNotFoundError:
        print("Le fichier /etc/passwd n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

if __name__ == "__main__":
    main()