# 02 - Manipuler git

## Atelier 2 : manipuler git en équipe

## Pré-requis

- `git`
- `Python 3.9`
- `VS Code` en option avec l'extension [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) d'installée.

Lancer la commande `python -m pip install -r atelier/requirements.txt` pour installer les dépendances pythons.

### Introduction

Lorsqu'on utilise git en équipe, il faut un point de synchronisation centrale permettant à chaque membre de déposer des changements et/ou récupérer les dernières mise-à-jour du projet.

Pour se faire, on utilise un dépôt SCM git tels que GitHub ou encore GitLab. Lors de la session 01-Introduction_CI/CD, vous avez eu l'occassion de manipuler quelques commandes avec GitHub Actions. Lors de cet atelier #2, nous allons revoir certaines d'entre elles et les détailer.

Aidez-vous de ceci :
- [Git basic cheatsheet](https://wac-cdn.atlassian.com/dam/jcr:e7e22f25-bba2-4ef1-a197-53f46b6df4a5/SWTM-2088_Atlassian-Git-Cheatsheet.pdf?cdnVersion=357)
- [GitEveryday minimum commands](https://git-scm.com/docs/giteveryday)


### Exercice

Tout d'abord, constituer une équipe de 2 personnes dont une des personnes est l'**owner du repository**. Il est chargé d'invité son camarade sur le repo GitHub : Aller sur `Settings > Collaborators and teams > Add People`

La personne invitée par le owner doit cloner le repos de son camarade en local en faisant `git clone <url owner's repo>`.

À ce stade, vous possedez en local un repository commun. Vous pouvez maintenant travailler en équipe sur les fonctionnalités du projet.
Au sein de cet exercice, le terme **owner** qualifie l'individu propriétaire du repository GitHub et le terme **guest** le collaborateur invité.

Le projet consiste à créer sous Python une nouvelle structure de données (comme `Array`, `List`, `Dict`...). Cette structure se nomme `Circular` et est caractérisée comme suit :

- `Circular` est initialisée à une taille fixe `n` avec pour valeur `None`.
- `Circular` est considérée vide lorsque les `n` valeurs sont égales à `None`.
- `Circular` est considérée pleine lorsque les `n` valeurs sont différentes de `None`.
- `Circular` peut ajouter des éléments de tout type en commencant par l'indice `0` jusqu'à `n-1` (indexation classique sous Python)
- `Circular` peut supprimer un élément. Cela sera toujours l'élément d'indice `0`. Lorsqu'un élément est supprimé, les autres éléments sont décalés vers la gauche.
- `Circular` peut décaler tous les éléments vers la gauche.
- `Circular` peut supprimer tous les éléments en une seule fois (méthode `clean`)
- `Circular` n'a pas d'effet de bord, c'est-à-dire que si la structure de données est pleine et qu'on souhaite ajouter un nouvel élémet, alors on ne fait rien. De même pour la suppression, si tous les éléments sont à None, alors on ne fait rien.

La branche par défaut de cet exercice est `atl2_actif`

En binome, suivez ce scénario à la lettre. Il permettra de créer des situations git qui faut absolument voir et comprendre. Ainsi, certains **TODO** seront soit à faire par le **owner**, soit à faire par le **guest**, soit par les deux. **Sauf mention contraire, ne passer pas à l'étape suivante avant que l'étape courante soit terminée**, c'est très important !!

#### Partie 1 : travail en équipe en synchrone

Faire `cd atelier/` pour travailler sur le code.

0. **TODO:owner:**: En local, exécuter la commande `git checkout -b atl2_actif origin/atl2`, qui permet de créér une branche `atl2_actif` (qui sera pour cette exercice la branche par défaut) à partir de la branche serveur (`origin`) nommée `atl2`. Ensuite, faire un `git push origin HEAD` pour déposer sa nouvelle branche `atl2_actif` sur le serveur git (qui s'appellera `origin/atl2_actif`). Enfin, faire un `git branch -u origin/atl2_actif` pour que la branche local `atl2_actif` se synchronise avec la branche distante `origin/atl2_actif`. En effet, sans cette commande, elle resterait en synchronisation avec la branche `atl2`.

1. **TODO:owner:**: Compléter la méthode `is_empty` dans le fichier `atelier/circular/__init__.py`. Tester en lancant la commande `pytest -s circular/test_circular.py::TestCircular::test_is_empty`. Si le test est OK, alors créer un commit avec un message explicit en veillant à ce que les bons fichiers sont dans l'état **staged**, puis pousser vos modifications sur le serveur GitHub avec la bonne commande `git push`. 

2. **TODO:guest:**: L'owner a déposé des changements au sein du projet, il faut les récupérer avant de continuer. Exécuter la commande `git checkout -b atl2_actif origin/atl2_actif` pour récupérer la nouvelle branche. Faire un `git pull` pour mettre à jour le repository en local (ta machine) par rapport au repository distant (GitHub). Pour vérifier que les modifications sont bien récupérées, faire un `git log`. Le commit le plus récent doit porter le message écrit par le **owner** ou bien être rédigé par le owner. Si ce n'est pas le cas, un problème est survenu à l'étape 1.

3. **TODO:guest:** Compléter la méthode `is_full` dans le fichier `atelier/circular/__init__.py`. Tester en lancant la commande `pytest -s circular/test_circular.py::TestCircular::test_is_full`. Si le test est OK, alors créer un commit avec un message explicit en veillant à ce que les bons fichiers sont dans l'état **staged**, puis pousser vos modifications sur le serveur GitHub avec la bonne commande `git push`. 

4. **TODO:owner:**: Le guest a à son tour déposé des changements au sein du projet, il faut les récupérer avant de continuer. Faire un `git pull`. Pour vérifier que les modifications sont bien récupérées, faire un `git log`. Le commit le plus récent doit porter le message écrit par le **guest** ou bien être rédigé par ce dernier. Si ce n'est pas le cas, un problème est survenu à l'étape 3.

Observer l'évolution de l'historique à l'aide de l'extension VScode **Git Graph**.

Dans cette facon de travailler, chaque membre de l'équipe a participé à tour de rôle au sein du projet.

Avantages:
- Jamais de conflit car chacun travail sur le projet à jour et sur des *features* distinctes.
- Utilisation très basique de git limitée aux commandes `git pull`, `git push` et `git add/commit`.

Inconvénients:
- Impose un rythme de travail différent qui impacte l'avancement du projet souvent lent.
- Viable uniquement sur une taille d'équipe très petite (~2 personnes)

#### Partie 2 : travail en équipe en asynchrone

5. **TODO**: Après que s'être synchronisé au repository distant par un `git pull`, un membre du binôme implémentera la méthode `add` tandis que l'autre membre fera la méthode `clean`, cette fois-ci de manière asynchrone.

- Celui qui fera `add` testera son code en faisant `pytest -s circular/test_circular.py::TestCircular::test_add`. Si le test est OK, alors créé un commit avec message explicit. **PAS DE `git push` A FAIRE**
- Celui qui fera `clean` testera son code en faisant `pytest -s circular/test_circular.py::TestCircular::test_clean`. Si le test est OK, alors créé un commit avec message explicit. **PAS DE `git push` A FAIRE**

6. **TODO**: Lorsque les 2 binômes valident leur test, et uniquement à ce moment, chacun fera un `git push`. Qu'observez-vous ?

Observer l'évolution de l'historique à l'aide de l'extension VScode **Git Graph**.

7. **TODO**: Pour résoudre le problème, le binôme confronté à l'erreur doit se mettre à jour au repository distant avant de pousser ses changements. En effet, pour le serveur git, il observe une anomalie sur le dernier commit. Une fois à jour, faire un `git push`.

Si aucun conflit est observé, alors tout est bon.

L'autre binôme peut se re-synchroniser au moyen d'un `git pull`.

Observer tous les deux l'évolution de l'historique à l'aide de l'extension VScode **Git Graph**.

Dans cette manière de travailler, chaque membre de l'équipe avance au même moment avec potentiellement une version différente du repository (càd, avec des commits en retard ou en avance). 

Avantages:
- Chaque membre peut travailler quand bon lui semble. Permet une plus grande flexibilité sur l'organisation du travail.
- Si les *features* réalisées sont totalement indépendantes, alors la productivité augmentera.

Inconvénients:
- Risque fréquent de conflit s'il y a une dépendance fonctionnelle ou lorsque 2 collaborateurs travaillent sur la même chose.
- Si le différentiel des changements est trop important entre les commits d'un collaborateur et un autre, alors le conflit prendra beaucoup de temps à être résolu
- Très difficile à gérer lorsque la taille de l'équipe est grande (> 4 personnes)

#### Partie 3 : travail en équipe sur des branches personnelles

8. **TODO**: Après que s'être synchronisé au repository distant par un `git pull`, un membre du binôme créer une nouvelle branche nommée `atl2_actif_shift_left` tandis que l'autre membre va créer une nouvelle branche nommée `atl2_actif_pop`. 

9. **TODO**: Faites un `git push` de votre nouvelle branche afin de la répercuter sur le serveur GitHub. Quand les deux binômes ont terminé de pousser leur branche respective, faites un `git pull` pour récupérer la branche de votre binôme.

Observer l'évolution de l'historique à l'aide de l'extension VScode **Git Graph**.

10.  **TODO**: Le binôme en charge de la branche `atl2_actif_shift_left` implémente la méthode `shift_left` tandis que l'autre, en charge de `atl2_actif_pop`, implémente la méthode `pop`. Tester en faisant `pytest -s circular/test_circular.py::TestCircular::test_shift_left` ou `pytest -s circular/test_circular.py::TestCircular::test_pop`.

En toute rigueur, le test `test_pop` a du échouer. En effet, la méthode `pop()` utilise la méthode `shift_left()` qui doit être implémenté par le binôme. La personne responsable de la méthode `pop()` est donc coincé (autrement, cela veut dire que la méthode `pop()` a réécrit la méthode `shift_left` en son sein). Suivre les instructions suivantes :

11.  **TODO**: Si le test `test_shift_left` est OK, alors créér un nouveau commit avec un message explicit puis pousser vos modifications sur le serveur git.

À ce niveau, 2 scénarios (à minima) peut se créér :
- Soit l'un des binômes finalise sa branche très rapidement avant son collègue. Il est alors éligible à fusionner sa branche avec la branche par défaut de cet exercice `atl2_actif`. Une fois la fusion réalisée, son collègue sera bloqué par le serveur git s'il tente de fusionner sa branche avec celle par défaut. En effet, l'historique divergera et git lui demandera de se mettre à jour avant de procéder. La mise à jour lui provoquera potentiellement des conflits.
- Soit les deux binômes finalisent aux même moment, car l'un a besoin du travail de l'autre pour avancé. C'est ce scénario qu'on va privilégier pour la démonstration. 

12.  **TODO**: Lorsque les deux binômes ont finalisé puis poussé leur branche respective sur le serveur git, il faudra fusionner l'une des deux branches sur l'autre, puis résoudre les conflits (si existant). Lorsque les conflits sont résolus, il faudra se remettre à jour en local. Pour fusionner 2 branches, il existe plusieurs méthodes dont :
- Les *pull request* GitHub (~ *merge request* sur GitLab)
- La commande `git merge` (utilisé en fast-forward)
- La commande `git rebase` (plus technique et très pratique)

Pour cette étape, veuillez utiliser les *pull request* à l'aide de l'interface web de GitHub. Aller sur votre branche, puis cliquer sur `Create new pull request`. **ATTENTION: par défaut, la pull request pointe sur le repository qui a servi de fork (donc le repo de @Rxinui), veuillez à séléctionner votre repository dans la base-branch**. Vous verrez `<base branch> <-- <current branch>` sur l'interface web où `<base branch>` doit correspondre à la branche qui recevra les changements, ici `atl2_actif_pop` et `<current branch>` la branche où les nouvelles modifications ont été traités donc `atl2_actif_shift_left`.

Grâce aux pull request, GitHub vous affiche de manière ergonomique les différences entre chaques fichiers comportant des modifications et vous permets d'intéragir avec l'auteur de la *pull request*. Vous êtes ainsi invité à commenter les changements afin de participer à l'audit du code.

Après la validation de la *pull request*, la branche distante `origin/atl2_actif_pop` obtiendra la méthode `shift_left` implémentée, et pourra ainsi continuer l'implémentation de la méthode `pop`.

Observer l'évolution de l'historique à l'aide de l'extension VScode **Git Graph**.

13.  **TODO**: le binôme en charge de la méthode `pop` doit terminer l'implémentation de cette méthode. Tester en faisant `pytest -s circular/test_circular.py::TestCircular::test_pop`. Si le test `test_pop` est OK, alors créér un nouveau commit avec un message explicit puis pousser vos modifications sur le serveur git.
    
14.   **TODO**: À présent, il faut fusionné la branche précédente - celle qui a recu les modifications `atl2_actif_pop` - sur la branche par défaut de cet exercice `atl2_actif`. Résoudre les conflits (si existant) et mettre à jour en local.

15.  **TODO**: Placer vous sur la branche `atl2_actif`, et lancer la commande `pytest -s` puis le programme principal `python main.py`. Tout devrait fonctionner.

Observer l'évolution de l'historique à l'aide de l'extension VScode **Git Graph**.


Dans cette manière de travailler, chaque membre travail à un rythme/moment différent mais surtout sur une branche différente. Cette méthode offre la possibilité d'avoir son espace personnel (sa branche). De facto, les changements apportés sur sa branche n'impacte et ne concerne aucunement les autres collaborateurs. Une fois que la branche est terminée (càd, la *feature* réalisée), on met à jour la branche personnelle par rapport à la branche principale (ie. `master`), git se chargera de faire correspondre les changements entre ces deux branches, et affichera les conflits à résoudre.

Avantages:
- Avoir sa propre branche offre une liberté totale. On peut la casser, la reconstruire, la modifier à souhait. Cela ne va gêner ni le projet, ni les autres équipiers.
- La productivité est largement augmentée.
- Indépendance de travail entre les collaborateurs.
- Remplit son rôle dans une grande équipe. **Attention**: cela requiert quand même un bon management.

Inconvénients:
- Demande plus de connaissances sur `git` et sur le serveur git utilisé (ie. GitHub).
- Si une *guideline* n'est pas définit en amont par l'équipe, notamment sur comment et quand créer des branches personnelles, alors le management du serveur git peut rapidement devenir délicat.
