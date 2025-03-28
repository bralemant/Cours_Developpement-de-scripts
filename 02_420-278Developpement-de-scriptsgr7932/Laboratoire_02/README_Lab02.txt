LABORATOIRE 2

### Partie 1 : Surveiller les processus de votre système
La première partie du laboratoire se concentre sur la création d’un script Python pour surveiller les processus en cours sur un système. Elle évolue en trois étapes distinctes.

# Étape 1 : Faire fonctionner le script de base
Dans cette étape, le script utilise le module psutil pour surveiller un processus spécifique, comme htop. Toutes les 5 secondes, il vérifie si ce processus est actif. S’il l’est, le script affiche un message avec son PID; sinon, il indique que le processus n’est pas trouvé. Pour commencer, on identifie le nom exact du processus avec la commande ps aux, on le configure dans le script, puis on l’exécute pour observer les messages de surveillance.

# Étape 2 : Convertir le script en exécutable et ajouter un paramètre
Ici, le script devient un exécutable qu’on peut lancer directement dans le terminal avec un argument, comme ./monWatchdog.py htop. On ajoute le shebang #!/usr/bin/env python3, on rend le fichier exécutable avec chmod +x, et on modifie le code pour utiliser sys.argv afin de récupérer le nom du processus à surveiller. Une fois prêt, on teste le script en passant le nom d’un processus en paramètre.

# Étape 3 : Surveiller plusieurs processus depuis un fichier
À cette étape, le script lit une liste de processus à surveiller dans un fichier texte (ex. : processus_a_surveiller.txt). Il vérifie l’état de chaque processus toutes les 5 secondes et affiche les résultats. On crée d’abord le fichier avec les noms des processus, puis on adapte le script pour le lire et boucler sur chaque entrée. Le code gère aussi les erreurs, comme un fichier introuvable ou vide, pour assurer une exécution robuste.



### Partie 2 : Introduction aux stratégies de sauvegarde
La deuxième partie automatise des sauvegardes (complètes et différentielles) en Python, en remplaçant des scripts bash par un script unique. Elle progresse en cinq étapes.

# Étape 0 : Familiarisation avec les commandes de sauvegarde
Cette étape préparatoire consiste à explorer les scripts bash existants pour les sauvegardes. On teste les commandes tar dans un terminal pour créer des sauvegardes complètes et différentielles sur un dossier de test, afin de comprendre leur fonctionnement avant de les adapter en Python.

# Étape 1 : Transformer la sauvegarde complète en Python
Le script Python reproduit une sauvegarde complète en utilisant subprocess.run() pour exécuter la commande tar -cvf comp.tar /chemin/du/dossier. On importe le module subprocess, on définit le chemin du dossier à sauvegarder, puis on lance la commande pour générer une archive complète.

# Étape 2 : Transformer la sauvegarde différentielle en Python
Ici, le script gère une sauvegarde différentielle en archivant uniquement les fichiers modifiés récemment. Avec subprocess.run(), on combine find et tar pour créer une archive (ex. : diff.tar). On ajuste le nom de l’archive et on utilise shell=True pour exécuter la commande adaptée.

# Étape 3 : Automatiser la sauvegarde selon le jour
Le script devient intelligent : il choisit automatiquement entre une sauvegarde complète (le vendredi) ou différentielle (les autres jours) selon la date, détectée avec datetime.weekday(). Le nom de l’archive est généré dynamiquement avec strftime(), et des messages informent l’utilisateur du type de sauvegarde effectué.

# Étape 4 : Passer les chemins en paramètres
Enfin, le script accepte le dossier source et la destination comme arguments via sys.argv (ex. : ./sauvegarde.py /source /dest). On modifie le code pour intégrer ces chemins dans les commandes tar, permettant une personnalisation facile lors de l’exécution.

