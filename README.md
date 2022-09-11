# Projet RedLine
***

## Context

Il s'agit d'une application web permettant aux joueur de roleplay sur GTAV d'avoir un catalogue des véhicules disponible en dehors des heures d'ouverture de la concession en ligne.
Cette application se veut être paramétrable pour tous les serveurs avec un minimum de modification.

Cette application propose un catalogue des véhicules disponibles, la possibilité aux utilisateurs de rechercher et commander un véhicule en informant les concessionaires de la commande.

L'application propose également la possibilité aux concessionaire d'enregistrer leurs ventes.

***

## Comment installer et utiliser l'applciation?
1. Clone ce repo;
2. Créer une base de donnée avec PostgreSQL ```redline``` avec un utilisateur ```concessionaire```. En cas de changement, il faut penser à modifier le fichier ```settings.py```;
3. Créer et utiliser un environnement virtuel avec ```python3 -m venv env``` puis ```source env/bin/activate```;
4. Installer les dépendances du projet avec ```pip install -r requirements.txt```;
5. Réaliser les migrations du projet avec ```python3 manage.py makemigrations``` et ```python3 manage.py migrate```;
6. Lancer les commandes pour remplir la base de données avec ```python3 manage.py category``` et ```python3 manage.py vehicule```;
7. Entrer l'url du channel discord en variable d'environnement ```DISCORDURL```; 
8. Puis vous pouvez lancer l'application avec ```python3 manage.py runserver```;

Pour tout déploiement sur serveur privé, il va falloir installer et paramétrer Nginx, ajouter les adresses autorisé dans le fichier ```settings.py```.

Pour utiliser flake8, il faut tout simplement entrer la commande ```flake8```\
Pour exécuter les tests, il faut utiliser ```coverage run --source='.' manage.py test``` et ```coverage report``` pour vérifier la taux de couverture des tests.
leano.pablo@gmail.com