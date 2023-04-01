<div align="center">
  <h1>PROJET DIAMANT</h1>
  <a href="https://fr.wikipedia.org/wiki/Oracle_SQL_Developer"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/></a>
</div>

## À propos

Le but de ce projet était de réaliser un jeu de société nommé "Diamant". Ce jeu basé sur un principe de prise de risque amène les joueurs à explorer un temple où ils devront récupérer des diamants. Mais attention ! L'exploration n'est pas sans risque, et les joueurs peuvent rencontrer des dangers qui peuvent leur faire perdre la partie.

## Contenu
- Le fichier [Diamant.py](Diamant.py) contenant le programme qui permet de faire fonctionner le jeu, il contient la partie qui gère les calculs et la gestion des joueurs, et une autre partie qui permet de faire fonctionner l'interface graphique.
- Les répertoires images et images_original qui contiennent les images utilisées dans l'interface graphique.

## Règles du jeu

Le jeu se joue de 3 à 8 joueurs sur un seul et même appareil et se compose de 5 manches.

Le but du jeu est d'être le joueur avec le plus de diamants avant la fin de la partie. 
Chaque tour , une carte est piochée, celle-ci peut être une relique, un piège ou un trésor :
- La relique est laissée au sol et sera donnée au prochain joueur qui sortira du temple si il est seul.
- Le piège n'a pas de réel impact sauf si un piège identique a déjà été tiré lors de la manche actuelle. Dans ce cas, la manche prend fin et tous les joueurs encore présents dans le temple perdent tout le contenu de leur poche.
- Le trésor est une valeur en diamant qui est partagée équitablement entre tous les joueurs présents dans le temple.

A la fin de chaque tour les joueurs peuvent choisir de continuer d'explorer ou de rentrer au campement. Si il y a des diamant sur le sol lors de la sortie du temple, ceux-ci sont partagés entre tous les joueurs. Les joueurs ont pour but de terminer les 5 manches avec le plus de diamants au campement.

Pour plus d'informations, [cliquez ici](https://iello.fr/wp-content/uploads/2022/07/DIAMANT_regles.pdf).

## Comment utiliser ?

Exécutez le fichier Diamant.py puis une interface graphique s'ouvrira, vous pourrez ainsi jouer au jeu.

## Crédits

Projet réalisé par :
- [Ewen GILBERT](https://github.com/EwenDev)

Ce projet a été réalisé dans le cadre d'une SAÉ lors du premier semestre de BUT Informatique à l'IUT de Vélizy.


