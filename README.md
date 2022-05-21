# 02 - Manipuler git

## Atelier 1 : Manipuler git individuellement

### Pré-requis

On se basera sur un simple script python.

Installation de :
- `git v2.32.0`
- `python v3.9`

### Introduction

Dans cet atelier, on va utiliser les commandes basiques de git au sein d'un projet individuel. Ces commandes vous permettront de versionner votre code (et vos fichiers de manière générale), de lire votre historique et d'y naviguer, c'est-à-dire se déplacer d'une version ultérieure vers une version antérieure et vice-versa.

Pour cet atelier, les ressources suivantes peuvent vous être utile:
- https://git-scm.com/docs/giteveryday#STANDALONE

Pour rappel, le cheminement d'un commit

![Git staged commit](./img/1-git-staged-commit.png)

### Commandes git


### Exercice

Un script python est mis à votre disposition `atelier/main.py`. Ce fichier sera versionné à chaque ajout de fonctionnalité jusqu'à sa version finale.

**État initial** : `atelier/main.py` afficher un message hello.
**État final** : `atelier/main.py` analyse l'ensemble des fichiers contenu dans `atelier/rsc/`.

#### [Draft] plan
[Partie 1]
1. `get_files_path` : lire les fichiers du dossier `atelier/rsc/`
2. `get_file_content` : afficher tous les fichiers 
3. `analyze_files` : analyse les fichiers (nom, extensions, nombre de mots, nombre de lignes)

[Partie 2]
4. Checkout sur commit `get_file_content` et créer une nouvelle branche `atl1_filter_files`
5. Modifier `get_files_path` pour ne lire que les fichiers de type `.txt`
6. Faire une merge `atl1_filter_files` -> `atl1`. Conflit attendu. Résoudre le conflit de sorte à inclure le changement.

7. **TODO**: Lancer la commande `git status`.

À ce stade, tout est *clean*. On va rajouter une fonctionnalité à notre programme afin de faire réagir git.

2. **TODO**: Copier-coller la fonction ci-dessous dans le fichier `atelier/main.py` (dans la section *Functions*)

```Python
def get_files_path(folder: str) -> List[Path[str]]:
    """Renvoie la liste des noms de fichier contenu dans {folder}
    
    Args:
        folder (str): chemin du dossier à parcourir
    Return:
        List[Path[str]]: liste contenant les chemins des fichiers de {folder}
    """
    return list(Path(folder).iterdir())
```

2. **TODO**: Lancer de nouveau la commande `git status`. Des changements ont du être opérés. 

Effectivement, le contenu du fichier `atelier/main.py` a changé, c'est ce que vous indique le résultat de la commande. Pour prendre en compte les changement, il faut les ajouter dans votre commit.

3. **TODO**: Ajouter les modifications dans l'état "staged" à l'aide de la commande `git add .` (`.` signifit "Tous les fichiers modifiées")
4. **TODO**: Lancer à nouveau `git status` et observer. Créer une sauvegarder (commit) avec la commande `git commit -m "<mon message expliquant les changements>"`. Exécuter de nouveau `git status`.

Pour consulter l'historique git de votre projet, c'est à dire tous les commits de votre branche actuelle (`atl1`), on utilise la commande `git log`

5. **TODO**: Créer le dossier `atelier/rsc/` et rajouter à l'intérieur au moins 1 fichier au format `.txt` et au moins 1 fichier au format `.csv`. Mettre du contenu random dans les fichiers rajoutés (ie. https://loremipsum.io/generator/).

6. **TODO**: Lancer `git status`. Quels changements remarquez-vous ? Les fichiers de `atelier/rsc/` seront-ils pris en compte si vous faîtes un `git commit -m "rajout des fichier"` ? Faites-en sorte d'inclure les nouveaux fichiers et créer un nouveau commit.

À ce stade, si vous faîtes un `git status`, tout doit être *clean*.

7. **TODO**: Rajouter la fonctionnalité suivante et répéter les commandes (utiles) git précédentes afin de créer un nouveau commit pour cette fonctionnalité :

```python
def get_file_content(path: Path[str]) -> str:
    """Renvoie le contenu d'un fichier
    
    Args:
        path (Path(str)): chemin du fichier à lire
    Return:
        (str): contenu du fichier
    """
    return open(path).read()
```

Consulter de nouveau votre historique git et vous devriez voir 4 commits au total (dont le plus ancien a pour auteur 'Rxinui').

8. **TODO**: Rajouter et completer la fonction suivante à l'aide des fonctions pythons, `get_files_path` et `get_file_content`.

```python
def analyze_files(folder: str) -> None:
    """Analyse les fichier contenu dans {folder}

    Args:
        folder (str): chemin du dossier à analyser
    """
    data = dict.fromkeys(["file","extension","chars","lines"])
    paths = # TODO
    for path in paths:
        content = # TODO
        data["file"], data["extension"] = #  TODO see https://docs.python.org/3.9/library/pathlib.html#methods-and-properties
        data["chars"], data["lines"] = # TODO see https://docs.python.org/3.9/library/stdtypes.html#string-methods
        print(content,"-"*10,data,sep="\n",end="\n\n")
```

9. **TODO**: Créer un nouveau commit pour inclure la nouvelle fonctionnalité.

10. **TODO**: Mettre à jour le main program du fichier `atelier/main.py` de sorte à utiliser la fonction `analyze_files` sur le dossier `rsc/`. Exécuter le fichier python. Si le programme fonctionne sans problème, créer un nouveau commit avec comme message `"Version finale de main.py"`. Sinon, corriger les erreurs et re-tester.
