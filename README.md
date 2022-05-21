# 02 - Manipuler git

## Introduction

**git** est un outil de versionnage (de code) permettant à un l'utilisateur de créér un historique navigable de ses fichiers.

Pour les développeurs, cet outil facilite la gestion du code au sein d'un projet, personnel et surtout en équipe. **git** est capable de détecter des conflits et offre la possibilité de les résoudres automatiquemet, si cela est possible, ou manuellement dans le cas contraire.

**git** est un outil complet et offre des fonctionnalités avancées qui ne seront pas vu dans cet atelier. Toutefois, pour les plus curieux, je vous invite à consulter les ressources suivantes :
- [Git official docs](https://git-scm.com/docs)
- [Git pro](https://git-scm.com/book/en/v2)

À contrario, cet atelier vise à vous enseigner les notions de bases de git et son fonctionnement principal au sein d'un projet *standalone* et dans un projet *d'équipe simple* :
- [Git basic cheatsheet](https://wac-cdn.atlassian.com/dam/jcr:e7e22f25-bba2-4ef1-a197-53f46b6df4a5/SWTM-2088_Atlassian-Git-Cheatsheet.pdf?cdnVersion=357)
- [GitEveryday minimum commands](https://git-scm.com/docs/giteveryday)

Voir les vidéos suivantes :
- [Git dans la vraie vie en 5min](https://www.youtube.com/watch?v=1SXpE08hvGs)

## Vocabulaire de git

*NB: Les termes utilisés sont les termes anglais de git*

*NB 2: On parle de "projet" un dossier contenant des fichiers et un "projet git" un dossier contenant des fichiers que git gère/versionne.*

- **remote (remote server)**:  serveur distant hébergeant vos repositories git. Les plus connus sont *GitHub* et *GitLab*.
- **repository (repo)**: pour qu'un projet soit suivi par git, ce dernier doit être qualifié de *repository git* (abrégé *repo git*). On distingue 2 types de repository :
    - **local repository**: repository hébergé sur votre machine locale. C'est ce repo qui vous sert d'environnement de travail. Toutes les modifications se feront sur ce repo qui par la suite sera synchroniser avec votre repo distant.
    - **remote repository**: repository distant hébergé sur un serveur SCM git. Les serveurs les plus connus sont *GitHub* et *GitLab*. Ce repo est à utilité multiple. Il sert de :
        - **Sauvegarde** : vous pouvez récupérer un repo depuis un serveur git vers votre PC et inversement.
        - **Référence** : les autres développeurs ne peuvent pas consulter un repository local. Par contre, un repository distant est consultable sur internet (si les authorisations nécessaires sont attribuées). Ainsi, les autres développeurs peuvent récuperer votre projet, y contribuer et proposer des changements que vous décidez ou non d'appliquer.
        - **Point de synchronisation** : lorsqu'un repository est utilisé par plusieurs collaborateurs, les changements sont déposés et récupérés sur le *remote repository*. Effectivement, il n'est pas possible de faire du *peer to peer* pour se synchroniser. Tout est centralisé sur le serveur git.
Par défaut, lorsqu'un repository est créé, une *branche git* par défaut est obligatoirement créé (souvent appelé `master` ou `main`). Elle sert de point de départ dans votre historique de versionnage.
- **commit**: une sauvegarde de votre projet à un instant t. Un commit est caractérisé par :
    - son **auteur**
    - son **identifiant (SHA)** unique.
    - son **message** décrivant l'intérêt de la sauvegarde.
    - ses **fichiers** que l'on souhaite versionner. Cela implique qu'une séléction de fichiers est nécessaire. Ce n'est pas parce que des fichiers se trouve dans votre projet git qu'il sera suivit par git. D'où l'intéret des commandes `git add` et `git rm`.
- **branch**: une succession de commit qui forme un historique. C'est une bifurquation d'historique à partir d'un commit. Avoir plusieurs branches permet d'obtenir plusieurs historiques différents. Par défaut, la branche principale est appelé *master* et de cette branche peut produire d'autres branches. Elles peuvent être fusionnées pour converger 2 historiques différents (fusion de branche). Chaque branche doit disposer d'un nom unique. 
- **remote branch**: même principe mais sur le serveur distant. Elle sert de sauvegarde ou de point de synchronisation.
- **merge**: fusion appliquée entre 2 branches (2 historiques différents). Une fusion permet l'aggregation des changements produits dans les 2 branches créant ainsi un nouveau commit. Ce nouveau commit contiendra les changements detenus par la branche #1 ou par la branche #2 ou par les 2 branches.
- **conflict**: on parle de conflit lorsqu'un problème est survenu soit entre le repo local et distant, soit entre deux branches. Il est commun de rencontrer des conflits au moment d'un *merge* car des changements trop radicaux sont détectés par git qui est incapable de les gérer automatiquement. Il est donc du ressort du développeur de résoudre ces conflits avant de finaliser la fusion.
- **fork (on repository)**: permet de cloner un repository distant contenu sur un serveur distant (souvent qui ne vous appartient pas) vers votre espace personnel du serveur distant. Entre autre, *forker* effectue un clone distant d'un projet.

## Atelier

Les ateliers suivants vont vous permettre de manipuler git afin d'assimiler les notions vu au-dessus. 

### Choix d'atelier

Pour commencer un atelier, il est nécessaire de forker le projet. Cliquer sur **Fork** (en haut à droite) et choisissez votre compte. Cela permet de cloner mon repo GitHub sur votre compte personnel.

Cloner votre repository forké sur votre compte GitHub vers votre machine locale en cliquant sur **Code**. Copier-coller l'URL qui est apparue et lancer sur votre machine la commande suivante : 

```bash
git clone <url-copiée>
```

Pour séléctionner et débuter un atelier, veuillez lancer une des commandes indiquées ci-dessous.

1. Manipuler git individuellement

```shell
git checkout -b atl1_actif origin/atl1
```

2. Manipuler git en équipe

```shell
git checkout -b atl2_actif origin/atl2
```
