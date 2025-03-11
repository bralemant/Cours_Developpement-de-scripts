print("\n\033[92mExo Program. Rechercher un utilisateur et ses ID dans le fichier /etc/passwd \033[0m")
print()

import sys

# Fonction principale pour rechercher un utilisateur dans le fichier /etc/passwd
def main():
    if len(sys.argv) != 2:                                              # Vérifier si un argument est fourni
        username = input("Veuillez entrer le nom d'utilisateur à rechercher: ")
    else:
        username = sys.argv[1]                                          # Récupérer le nom d'utilisateur depuis les arguments
# Ouvrir et lire le fichier /etc/passwd
    try:
        passwd_file = open('/etc/passwd', 'r')                          # Ouvrir le fichier en mode lecture
        for line in passwd_file:                                        # Parcourir les lignes du fichier
            fields = line.strip().split(':')                            # Séparer les champs par ':'
            if fields[0] == username:                                   # Vérifier si le nom d'utilisateur correspond
                user_id = fields[2]                                     # Récupérer l'ID utilisateur et ID de groupe
                group_id = fields[3]                                    # Récupérer l'ID de groupe                                  
                print(f"\n\033[92mUtilisateur\033[0m: {username}, \033[92mID utilisateur\033[0m: {user_id}, \033[92mID de groupe\033[0m: {group_id}")
                return
        print(f"\n\033[91mL'utilisateur '{username}' n'a pas été trouvé.\033[0m")
    except FileNotFoundError:                                           
        print("Le fichier /etc/passwd n'a pas été trouvé.")
    except Exception as e:                                              
        print(f"Une erreur est survenue: {e}")

# Exécuter la fonction principale
if __name__ == "__main__":
    main()