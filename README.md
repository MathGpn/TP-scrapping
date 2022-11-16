# TP-scrapping

# Objectif : Créer un script exécutable permettant de scraper une liste de vidéos youtube et stockant les données récupérées dans un fichier au format json.

Pour ce TP, le scrapping est effectué à l'aide de BeautifulSoup et de Selenium.
Il est donc essentiel d'avoir un webdriver_manager.

-Le fichier "scrapper.py" contient une classe "Scrap" découpée en plusieurs méthodes permettant de retourner les informations demandées (titre vidéo, nom vidéaste...). A la fin de ce fichier se trouve un "main" permettant de respecter les consignes du TP comme l'utilisation du programme en CLI grâce à la librairie "argparse", aller piocher les vidéos Youtube à scrapper dans le "input.json" et retourner nos résultats du scrapping dans le "output.json". Vous remarquerez ainsi que sur le repo on a un exemple de output obtenu pour un l'input donné dans la consigne.

# Exécution du fichier "scrapper.py" avec la commande : python3 scrapper.py --input input.json --output output.json

-Le fichier "tests.py" nous permet de tester les différentes méthodes de la classe "Scrap" afin de s'assurer du bon fonctionnement de cette dernière sur un exemple concrêt (la vidéo d'Hugo Décrypte avec Pierre Niney). 

# Exécution des tests unitaires avec la commande : python3 -m unittest tests.py
# Exécution du coverage des tests avec la commande : pytest --cov=. tests.py

Remarque 1 : L'exécution du scrapping est déjà assez coûteuse pour 2 vidéos (50sec)
Remarque 2 : Il arrive rarement que les données n'aient pas le temps d'être scrappées 
