# Projet DevOps - Python, Docker, GitHub Actions

## Présentation

Ce projet est une introduction au DevOps à travers un exemple simple en Python.
L'objectif est de comprendre comment le code, les tests, et le déploiement
peuvent être automatisés et fiabilisés grâce à des outils modernes.

## Ce que contient ce projet

```
DevOps/
├── app.py                        # Le code Python
├── test_app.py                   # Les tests automatisés
├── Dockerfile                    # La définition du conteneur Docker
├── .gitignore                    # Les fichiers à ignorer dans Git
├── README.md                     # Ce fichier
└── .github/
    └── workflows/
        └── ci.yml                # Le pipeline CI/CD GitHub Actions
```

## Explication de chaque fichier

### app.py

C'est le coeur du projet. Il contient une fonction Python simple qui
retourne un message de bienvenue.

A chaque fois qu'on lance le programme, il affiche :

```
Bonjour, Monsieur Mohamed Bellahcene ! Bienvenue chez Kyndyl !
```

C'est volontairement simple. En entreprise, ce serait une vraie application
(une API, un service web, un traitement de données), mais le principe
DevOps reste exactement le même.

### test_app.py

Ce fichier contient les tests automatisés, écrits avec pytest.

Un test, c'est une vérification automatique que le code fait bien ce qu'on
attend de lui. On appelle la fonction, et on vérifie que le résultat contient
les bons mots.

Pourquoi c'est important : si quelqu'un modifie app.py par erreur et casse
le message, le test va échouer et alerter immédiatement. Sans tests,
l'erreur passerait inapercue jusqu'en production.

Pour lancer les tests manuellement :

```bash
python -m pytest test_app.py -v
```

### Dockerfile

Docker permet d'empaqueter une application avec tout ce dont elle a besoin
pour fonctionner (Python, les librairies, le code) dans une boite isolée
appelée conteneur.

L'avantage : le conteneur fonctionne de la meme facon sur n'importe quelle
machine, que ce soit votre ordinateur Windows, un serveur Linux, ou le
cloud. On elimine le probleme classique "ca marche sur ma machine mais pas
en production".

Notre Dockerfile dit en 4 lignes :
1. Partir d'une image Python officielle
2. Créer un dossier de travail
3. Copier notre code dedans
4. Lancer le programme au démarrage

Pour construire et lancer le conteneur :

```bash
docker build -t mon-app .
docker run mon-app
```

### .gitignore

Git est l'outil qui suit les modifications du code et les envoie sur GitHub.
Le fichier .gitignore lui dit quels fichiers ignorer, comme les fichiers
de cache Python (__pycache__) qui sont générés automatiquement et n'ont
pas besoin d'etre versionnés.

### ci.yml - Le pipeline GitHub Actions

C'est la piece centrale du DevOps. Ce fichier décrit une suite d'actions
automatiques qui se déclenchent a chaque fois qu'on pousse du code sur GitHub.

Notre pipeline fait trois choses dans l'ordre :
1. Récupérer le code
2. Installer Python et pytest
3. Lancer les tests
4. Construire l'image Docker

Si une étape échoue, les suivantes ne s'executent pas et GitHub affiche
une alerte rouge. Le code "cassé" n'ira jamais plus loin.

---

## Le cycle complet

Voici ce qui se passe a chaque modification du code :

```
1. On modifie le code sur son ordinateur
2. On lance les tests en local pour vérifier
3. On envoie le code sur GitHub (git push)
4. GitHub Actions déclenche automatiquement le pipeline
5. Les tests sont relancés sur les serveurs de GitHub
6. L'image Docker est construite
7. Si tout est vert, le code est validé
8. Si quelque chose echoue, on est alerté immédiatement
```

Ce cycle s'appelle CI/CD :
- CI (Intégration Continue) : tester automatiquement a chaque modification
- CD (Déploiement Continu) : déployer automatiquement si les tests passent

---

## Commandes utiles

Lancer les tests :
```bash
python -m pytest test_app.py -v
```

Construire l'image Docker :
```bash
docker build -t mon-app .
```

Lancer le conteneur :
```bash
docker run mon-app
```

Envoyer le code sur GitHub :
```bash
git add .
git commit -m "description"
git push
```
