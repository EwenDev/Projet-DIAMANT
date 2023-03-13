# Le jeu

## Mais c'est quoi "Diamant" ?

Le but de ce projet était de réaliser un jeu de société nommé "Diamant". Ce jeu basé sur un principe de prise de risque amène les joueurs à explorer un temple où ils devront récupérer des diamants. Mais attention ! L'exploration n'est pas sans risque, et les joueurs peuvent rencontrer des dangers qui peuvent leur faire perdre la partie.

## Les besoins du jeu

Le jeu a d'abord besoin d'une liste de joueurs, qui vont être modifiables avec plusieurs critères, tels que leur nombre de diamants, ou encore leur statut.

Celui-ci a également besoin d'une pioche créée à partir des cartes du jeu qui incarnent les trésors, les dangers, et les reliques.

Ensuite, on a besoin également d'un moyen d'analyser les cartes pour agir en conséquence. Si c'est un trésor, il doit être partagé entre les joueurs sur le plateau, si c'est un danger, on doit vérifier si il y en a déjà un identique qui a été tiré. Si c'est une relique, on l'ajoute au sol et on annexe sa valeur.

Il faut aussi interpréter le choix des joueurs et faire en sorte que la partie se déroule normalement avec 5 manches.

# Les outils utilisés

## Côté logiciel

Au départ, pour éditer et tester mon code, j'ai utilisé une site nommé "Replit" qui permet de programmer sur un site internet, permettant de programmer depuis n'importe quel appareil. Dans mon cas, il permet de faire un pont entre mon ordinateur portable et mon ordinateur fixe.

Ensuite, plus tard lorsque j'ai dû développer l'interface graphique, j'ai utilisé le logiciel "Visual Studio Code", qui est très pratique pour des projets de cette envergure.

Pour enregistrer et récupérer mon travail entre les appareils, j'ai utilisé la plateforme GitHub, permettant de sauvegarder les versions du programme en ligne et d'y accèder depuis n'importe où.

Pour m'organiser, j'ai utilisé un outil nommé "Trello", permettant de s'organiser et de planifier ses tâches.

## Côté programme

Pour réaliser l'interface graphique, j'ai utilisé un module nommé "tkinter" proposant diverses fonctions permettant de créer des interfaces graphiques interractives

Pour tout ce qui touche à l'aléatoire, j'ai utilisé un module nommé "random" intégrant plusieurs fonctions permettant de générer des nombres aléatoires ou encore mélanger des listes.

# Les stratégies utilisées

## Le processus

Il a fallu tout d'abord créer les joueurs à l'aide d'une classe, permettant alors de créer une liste d'objets "joueurs". Celle-ci sera par la suite parcourue par des boucles pour modifier les différentes données comme le nom des joueurs ou leur nombre de diamants.

Ensuite, j'ai créé une pioche à partir des cartes existantes dans le jeu diamant en utilisant des boucles qui vont ensuite mélanger le tas pour faire une pioche aléatoire.

La programmation orientée objet m'a beaucoup aidé dans la réalisation du jeu. Surtout dans la gestion des joueurs où elle était primordiale. Elle est utile dans son fonctionnement, permettant de séparer les fonctions, comme avec la fonction moteur, et la fonction d'interface graphique.

Pour la gestion des diamants entre les joueurs, ceux-ci sont d'abors archivés dans une variable qui va représenter les diamants à partager. Le reste va être stocké dans une variable qui va être utilisée lorsqu'un ou plusieurs joueurs voudront sortir du temple.

Pour vérifier la si la manche doit être terminée, une boucle vérifie, entre chaque tour si jamais deux pièges identiques ont étés piochés ou si tous les joueurs ont décidé de sortir du temple.

# Les difficultés rencontrées

J'ai tout d'abord rencontré des difficultés lors du début de la création du jeu, où la gestion des joueurs, des cartes, des fonctions principales et de la gestion du classement étaient difficiles. Le seul moyen de gérer les joueurs convenablement était l'utilisation d'un dictionnaire, mais cette solution n'est pas viable si on veut faire de notre jeu un jeu plus complexe.

Un autre problème était lors de l'implémentation de la partie graphique, car mon code était alors adapté pour un affichage et une gestion dans la console. J'ai dû alors modifier en grande partie mon code pour que son fonctionnement convienne à une version avec une interface graphique.

Une autre difficulté était également l'utilisation de tkinter, qui est un module de python assez complexe à comprendre quand on débute. La création de la partie graphique était alors la partie la plus longue à faire dans la réalisation du projet.

Pour terminer, la dernière difficulté était la complexité du jeu, qui demande beaucoup de tests unitaires et de changements de dernière minute, qui ont finalement pu faire fonctionner le code correctement.

# Comment passer au dessus de celles-ci ?

Pour la création du jeu, j'ai finalement opté pour une programmation orientée objet à l'aide de classes. Beaucoup plus pratique dans son fonctionnement, elle permet d'interpréter séparement les joueurs, en leurs donnant leurs propres données, comme leur nombre de diamants dans le temple et au campement, leur statut dans la partie ou encore leur nom.

Pour l'implémentation de l'interface graphique, j'ai pu migrer des fonctions de la classe qui gère la partie vers la classe de l'interface graphique, ce qui m'a permis une execution plus fluide et plus logique.

Pour les difficultés avec tkinter, j'ai pu y arriver grâce à la documentation variée disponible pour tkinter mais également grâce à mes camarades qui ont pu me guider sur la compréhension du module.

Pour ce qui est de la complexité du jeu, j'ai utilisé des fonctions de test unitaire pour essayer toute éventualité qui pourrait poser problème dans le jeu.

# Mon experience

Ce projet m'a permis d'en apprendre plus sur python et sur tkinter, et m'a permis de pratiquer énormément et de comprendre un peu plus le fonctionnement du langage. Malheureusement, celui-ci n'a pas vraiment été fait en équipe, mais il m'a apris à me gérer seul et à m'imposer un rythme de travail et des tâches précises. J'ai pu créer un vrai projet ambicieux à partir de zéro, et ça me rend réellement fier d'avoir réussi à réaliser autant tout en étant seul et en si peu de temps.

Surtout, le dernier avantage et que maintenant, je suis imbattable contre n'importe qui voulant jouer au jeu "Diamant" !

