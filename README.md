Objectifs
=========

Depuis l'ENT, offrir un accès personnel à       

JupyterHub à tous les enseignants intéressés par la 
rédaction de notebooks.                             
                                                    
2\. Permettre le partage de notebooks avec les      
élèves.                                             
                                                    
3\. Permettre aux élèves de modifier une copie      
personnalisée du notebook partagé que l'enseignant  
peut ensuite afficher depuis son interface          
Capytale.                                           

![](media/image3.png)

Le contexte
===========

**JupyterHub** est un outil en ligne, donc accessible avec un simple
navigateur web permettant de construire des notebooks, qu'on peut
considérer au choix

- comme des programmes Python enrichis de commentaires à la mise en
forme très évoluée
- comme des cours enrichis de code Python exécutable

C'est un excellent outil pour apprendre à programmer ou pour préparer
des activités mettant en œuvre le codage. Le défaut de JupyterHub est
actuellement le manque de fonctionnalités de partage de notebooks via
une interface simple d'utilisation.

**NBHosting** est un projet développé par l'INRIA qui permet à un
enseignant de proposer à des étudiants d'accéder à une copie personnelle
d'un notebook accessible par une URL partagée. L'étudiant peut modifier
sa copie du notebook et les changements sont automatiquement enregistrés
: il les retrouvera lors de l'accès suivant.

L'origine du projet 
===================

En Juin 2019

1.  L'académie dispose déjà d'un JupyterHub fonctionnel.
2.  La Dane a déjà l'expérience de la mise en place de briques dans les
    > ENT pour permettre d'accéder à un service tiers avec
    > authentification SSO. L'intégration de Jupyterhub dans un ENT
    > semble donc envisageable à relativement court terme.
3.  Thierry Parmentelat qui a développé à l'INRIA le projet NBHosting a
    > rencontré le 27 juin 2019 la DANE et la DSI qui se dit prête à
    > tenter une installation NBHosting sur un serveur académique pour
    > la rentrée prochaine.

Tous les éléments sont donc réunis pour une mise en place d'un service
(inédit dans l'éducation nationale après l'expérience intégrée dans
m@gistère) qui permettrait d'offrir dans les ENT une alternative à ce
que proposent dans leurs environnements Google (Colaboratory) et
Microsoft (Azure Notebooks).

Le calendrier
=============

- Courant Juillet/Août - La DSI de l'académie de Paris a commencé
  l'installation des différents outils nécessaire à la mise en lace
  du sevice complet.
- 10 septembre - La DSI a terminé la mise en place de l'outil
  NBHosting permettant le partage de notebooks. Le service est
  rebaptisé pour l'occasion : Capytale.
- Courant septembre, lancement des développements des l'interfaçages
  entre l'ENT et les services Jupyterhub d'une part et Capytale
  d'autre part.
- Mardi 8 octobre - Ajout d\'une brique dans l'ENT et d'un menu pour
  les enseignants
- Lundi 14 octobre - Possibilité de voir la liste des URL des notebook
  des élèves dans l'interface Capytale des enseignants
- Mardi 15 octobre - Phase Pilote : Ouverture des droits pour une
  douzaine de Beta-testeurs enseignant les mathématiques, les
  sciences physiques, les sciences des l'ingénieur ou NSI.
- Mercredi 16 octobre - Montage de 4 serveurs avec système de
  répartition de charge.
- 20-21-22 novembre - Présentations pédagogiques lors du salon
  Édicatec-Éducatice.
- 05 Décembre : Mise en route d'une machine de test.
- 17 décembre : problèmes réglés sur les caractères spéciaux dans les
  noms de fichier.
- 15 janvier : réunion sur l'installation de modules :
    -   Diaporama https://github.com/damianavila/RISE
    -   Exécution pas à pas https://github.com/lgpage/nbtutor
- 17 janvier : installation de rice, nbtutor (jupyterhub et nbhosting)
  et nbgrader (jupyterhub uniquement).
- 20 janvier : ajout de fichiers annexes possible

> Projets :

- Évaluation et tests unitaires
  https://github.com/parmentelat/nbautoeval
- Installer des noyaux supplémentaires
  (https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)
- Ocaml
  http://pascal.ortiz.free.fr/contents/autres/jupyter\_ocaml/jupyter\_ocaml.html
- Modifier l\'image Jupyter pour nbhosting afin de
  - permettre la modification des cellules de texte par les élèves
  - proposer une interface en français

Le schéma fonctionnel
=====================

1. **Travailler ses notebooks dans JupyterHub**\
  La brique ENT «JupyterHub» permet à chaque professeur d'accéder à son
  espace personnel sur le serveur jupyterHub académique (sans reconnexion
  grâce à une authentification SSO).\
  L'enseignant peut construire un notebook et en télécharger une copie au
  format .ipynb.
2. **Partager un notebook avec des élèves**\
  La brique ENT «Déposer un notebook partagé» donne accès à un formulaire
  de dépôt de notebook au format .ipynb (2.1). En retour, on obtient une
  URL à proposer aux destinataires du partage (2.2). L'ENT dispose déjà
  d'outils pour partager une URL avec la classe.

  ![](media/image1.jpg)

3. **Accéder à un notebook partagé**

En cliquant sur une URL de partage de notebook, l'élève transite de
manière invisible par un service (3.1) qui le redirige vers une URL
personnalisée lui donnant accès à une copie personnelle et modifiable du
notebook partagé par l'enseignant (3.2).

![](media/image2.jpg)
