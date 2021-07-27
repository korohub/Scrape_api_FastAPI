# API scraping avec FastAPI


[<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png">](https://fastapi.tiangolo.com/)


Projet d'api rapide avec FastAPI pour scraper des données sur une page Web.
Permet soit d'alimenter une base de données où de redistribué le contenu sur une page Web.

**Attention au droit d'auteur.**


## Pour commencer

Git clone https://github.com/korohub/Scrape_api_FastAPI.git

### Pré-requis

Ce qu'il est requis pour commencer avec votre projet...

- Python > 3.5
- FastAPI
- Uvicorn
- requests_html

### Installation

Les étapes pour installer 

cd Scrape_api_FastAPI

Avec pipenv :
```
pipenv install -r requirements.txt
```

Avec pip:
```
pip install -r requirements.txt
```

## Démarrage

```sh
python ./main.py
```

Pour les quotes :

rendez-vous sur http://localhost:8000/v1/quotes/{cat}
{cat} est a remplacer par la catégorie, ex: life
ex : http://localhost:8000/v1/quotes/life

pour l'api ecommerce

http://localhost:8000/v1/ecommerce/laptops
ou 
http://localhost:8000/v1/ecommerce/tablets



## Versions
Listez les versions ici 
_exemple :_
**Dernière version stable :** 1.0
**Dernière version :** 1.0


## Auteurs
Listez le(s) auteur(s) du projet ici !
* _**Korohub**_

## Todo

- Ajout dockerfile pour build une image
- Ajout Stockage en BDD (MongoDB || postgresql)
- Déploiement sur Héroku ou Vercel
