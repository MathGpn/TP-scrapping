# TP-scrapping

# Objectif : Créer un script exécutable permettant de scraper une liste de vidéos youtube et stockant les données récupérées dans un fichier au format json.

Pour ce TP, le scrapping est effectué à l'aide de BeautifulSoup et de Selenium.
Il est donc essentiel d'avoir un webdriver_manager.

-Le fichier "scrapper.py" contient une classe "Scrap" découpée en plusieurs méthodes permettant de retourner les informations demandées (titre vidéo, nom vidéaste...). A la fin de ce fichier se trouve un "main" permettant de respecter les consignes du TP comme l'utilisation du programme en CLI grâce à la librairie "argparse", aller piocher les vidéos Youtube à scrapper dans le "input.json" et retourner nos résultats du scrapping dans le "output.json". Vous remarquerez ainsi que sur le repo on a un exemple de output obtenu pour un l'input donné dans la consigne.

# Exécution du fichier "scrapper.py" avec la commande : python3 scrapper.py --input input.json --output output.json

-Le fichier "tests.py" nous permet de tester les différentes méthodes de la classe "Scrap" afin de s'assurer du bon fonctionnement de cette dernière sur un exemple concrêt (la vidéo d'Hugo Décrypte avec Pierre Niney). 

# Exécution des tests unitaires avec la commande : pytest tests.py
# Exécution du coverage des tests avec la commande : pytest --cov=. tests.py

Remarque 1 : Commencez par utiliser un "input.json" composé seulement de la vidéo d'Hugo Décrypte et de Pierre Niney :
({
    "videos_id": [
    "fmsoym8I-3o"
    ]
})
pour tester le programme en entier (temps d'exécution d'environ 10sec) ainsi que les tests unitaires.
Remarque 2 : Le coverage obtenu est de 54% mais toutes les méthodes sont testées.
