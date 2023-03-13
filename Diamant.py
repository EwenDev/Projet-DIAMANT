
import random
import os
import tkinter as tk
from tkinter import messagebox

"""
DIAMANTS - INTERFACE GRAPHIQUE/LIGNES DE COMMANDES (autre fichier)

REALISÉ DANS LE CADRE DE LA SAÉ IMPLEMENTATION PAR EWEN GILBERT.
"""

class Partie:
  def __init__(self):
    """
    Initialisation de la classe Partie

    Entrée : /

    Sortie : /
    """
    #Initialisation des variables locales
    self.title = '\n _____   _                              \n(____ \ (_)                        _    \n _   \ \ _  ____ ____   ____ ____ | |_  \n| |   | | |/ _  |    \ / _  |  _ \|  _) \n| |__/ /| ( ( | | | | ( ( | | | | | |__ \n|_____/ |_|\_||_|_|_|_|\_||_|_| |_|\___)\n \n' #Titre diamant ASCII
    self.liste_tresor = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17] #Liste des valeurs de tresor
    self.liste_danger = ['araignée','araignée','araignée','serpent','serpent','serpent','lave','lave','lave','boulet','boulet','boulet','bélier','bélier','bélier'] #Liste des dangers
    self.liste_relique = ['Le Totem de Wennawenna (5)',"Le Masque de l'Arojam (5)",'La Statue du Deiporg (5)',"Le Pot d'Or de Toukapatou (10)","Le Talisman du Treblig (10)"] #Liste des reliques
    self.valeur_reliques = [5,5,5,10,10] #Liste des valeurs des reliques
    self.carte = None #Variable qui va contenir la carte piochée par la fonction pioche_carte
    self.pioche = [] #Liste répertoriant la pioche du jeu définie par les fonctions melange et add_relique 
    self.cartes_jeu = [] #Liste répertoriant l'historique des cartes piochées par la fonction pioche_carte
    self.diamants_sol = 0 #Variable représentant le nombre de diamants laissés au sol par les joueurs
    self.reliques_sol = [] #Variable représentant le nombre de reliques laissées au sol par les joueurs
    self.decouvert = [] #Liste qui répertorie les reliques qui ont été découvertes par les joueurs
    self.nbdecouvert = 0 #Variable qui donne le nombre de reliques découverte par les joueurs
    self.tresor_partage = 0 #Variable qui définit la part de diamants donnée à tous les joueurs une fois partagée
    self.statut = True #Booléen représentant le statut d'une manche changé par la fonction finmanche
    self.caption = '.'
    self.caption2 = '.'
    self.caption3 = '.'
    #self.partie() #Appel de la fonction qui va gérer la partie


  def settings_joueurs(self,joueurs):
    """
    Fonction regrouppant toutes les mises en place de joueurs dans la partie (création des objets, initialisation des variables, etc.)

    Entrée : joueurs (liste d'objets de la classe Joueur)

    Sortie : /
    """
    self.joueurs = [] #Création d'une liste d'objets 'joueurs' à partir de la classe Joueur()
    for i in joueurs:
      self.joueurs.append(Joueur(i.get()))
    self.joueurs_plateau = [] #Liste contenant les objets des joueurs présents dans le temple
    for i in range(len(self.joueurs)): #Boucle permettant de mettre les objets joueurs de la liste joueurs dans la liste joueurs_plateau (self.joueurs = self.joueurs_plateau va lier les listes, on utilise donc une boucle)
      self.joueurs_plateau.append(self.joueurs[i])
    self.joueurs_out = [] #Liste contenant la liste des joueurs qui ont quitté le plateau
    self.joueurs_sortir = [] #indice des joueurs qui sortent du temple

  def verif_victoire(self):
    """
    Vérifie quel joueur a le plus de diamants en fin de partie et si deux joueurs en haut du podium ont le même nombre de diamants .
    
    Entrée : /

    Sortie : indice_max (indice du joueur avec le plus de diamants)/'egalite' (si deux joueurs ont le même nombre de diamants)
    """
    max = self.joueurs[0].diamants_total #Variable qui va contenir le nombre de diamants du joueur avec le plus de diamants
    indice_max = 0 #Variable qui va contenir l'indice du joueur avec le plus de diamants
    for i in range(len(self.joueurs)): #Boucle qui va parcourir la liste des joueurs et qui va définir le joueur avec le plus de diamants
      if self.joueurs[i].diamants_total >= max:
        max = self.joueurs[i].diamants_total
        self.indice_max = i

    occu = 0
    for i in range(len(self.joueurs)): #Boucle qui va parcourir la liste des joueurs et qui va définir si deux joueurs ont le même nombre de diamants
      if self.joueurs[indice_max].diamants_total == self.joueurs[i].diamants_total == max:
        occu += 1
      if occu >= 2:
        return 'egalite' 
    return self.indice_max

  def test(self):
    """
    Fonction qui va tester les fonctions de la classe Partie()
    """
    self.test_verif_victoire()
    self.test_reset_manche()
    self.test_verifcarte()
    self.test_melange()
    self.test_danger()
    self.test_relique()
    self.test_tresor()

  def test_verif_victoire(self):
    self.joueurs = [Joueur('Test1'),Joueur('Test2'),Joueur('Test3'),Joueur('Test4')]
    self.joueurs[0].diamants_total = 10
    self.joueurs[1].diamants_total = 10
    self.joueurs[2].diamants_total = 10
    self.joueurs[3].diamants_total = 10
    assert self.verif_victoire() == 'egalite'
    self.joueurs[0].diamants_total = 15
    assert self.verif_victoire() == 0
    self.joueurs[1].diamants_total = 20
    assert self.verif_victoire() == 1
    self.joueurs[2].diamants_total = 25
    assert self.verif_victoire() == 2

  def test_reset_manche(self):
    self.joueurs = [Joueur('Test1'),Joueur('Test2'),Joueur('Test3'),Joueur('Test4')]
    self.decouvert = ['Le Totem de Wennawenna (5)']
    self.joueurs[0].ingame = False
    self.joueurs[0].diamants_manche = 10
    self.reset_manche()
    assert self.carte == None
    assert self.pioche == []
    assert self.liste_relique == ["Le Masque de l'Arojam (5)",'La Statue du Deiporg (5)',"Le Pot d'Or de Toukapatou (10)","Le Talisman du Treblig (10)"]
    assert self.decouvert == []
    assert self.joueurs[0].ingame == True
    assert self.joueurs[0].diamants_manche == 0
    assert self.joueurs_plateau == self.joueurs

  def test_melange(self):
    self.melange(5)
    assert len(self.pioche) == len(self.liste_tresor) + len(self.liste_danger)
    assert self.liste_tresor + self.liste_danger != self.pioche

  def test_verifcarte(self):
    self.carte = 'serpent'
    assert self.verifcarte() == 'danger'
    self.carte = 1
    assert self.verifcarte() == 'tresor'
    self.carte = 'Le Totem de Wennawenna (5)'
    assert self.verifcarte() == 'relique'

  def test_relique(self):
    self.carte = 'Le Totem de Wennawenna (5)'
    self.reliques_sol = []
    self.relique()
    assert self.reliques_sol == ['Le Totem de Wennawenna (5)']
    assert self.liste_relique == ["Le Masque de l'Arojam (5)",'La Statue du Deiporg (5)',"Le Pot d'Or de Toukapatou (10)","Le Talisman du Treblig (10)"]
  
  def test_tresor(self):
    self.carte = 1
    self.diamants_sol = 0
    self.joueurs_plateau = [Joueur('Test1'),Joueur('Test2'),Joueur('Test3'),Joueur('Test4')]
    self.tresor(1)
    assert self.diamants_sol == 1
    self.carte = 4
    assert self.tresor(4) == 1

  def test_danger(self):
    self.carte = 'serpent'
    self.cartes_jeu = ['serpent',1,2]
    assert self.danger('serpent') == self.finmanche()
    self.cartes_jeu = [1,2]
    assert self.danger('serpent') == None

  def reset_manche(self):
    """
    Fonction permettant de redéfinir les variable de fonctionnement d'une manche. Essentielle au bon fonctionnement du programme

    Entrée : /

    Sortie : Redéfinit les variables de la classe
    """
    self.carte = None
    self.pioche = []
    self.liste_relique = ['Le Totem de Wennawenna (5)',"Le Masque de l'Arojam (5)",'La Statue du Deiporg (5)',"Le Pot d'Or de Toukapatou (10)","Le Talisman du Treblig (10)"]
    self.nbdecouvert = len(self.decouvert)
    self.cartes_jeu = []
    self.diamants_sol = 0
    self.reliques_sol = []
    self.tresor_partage = 0
    self.statut = True
    self.joueurs_plateau = []
    for i in range(len(self.decouvert)): #Boucle qui permet de retirer les reliques découvertes de la liste des reliques à trouver
      self.liste_relique.remove(self.decouvert.pop(0))
    for i in range(len(self.joueurs)): #Boucle qui permet de remettre aux joueurs leur statut de joueur en jeu et leur nombre de diamants ramassés à 0
      self.joueurs[i].ingame = True
      self.joueurs[i].diamants_manche = 0
    for i in range(len(self.joueurs)): #Boucle qui permet de remettre les joueurs dans le temple
      self.joueurs_plateau.append(self.joueurs[i]) 
    self.joueurs_out = []

  def melange(self,i):
    """
    Crée une pioche aléatoire à partir des trésors et des dangers des listes self.liste_tresor et self.liste_danger avec le module random

    Entrée : i (permet d'importer i de la classe Diamant_Frame dans Partie)

    Sortie : self.pioche (liste des cartes dans la pioche sans compter les reliques ajoutées plus tard)
    """
    self.i = i
    self.pioche = self.liste_tresor + self.liste_danger
    random.shuffle(self.pioche) #Mélange la pioche
    return self.pioche

  def add_relique(self,nbreliques):
    """ 
    Ajoute la ou les reliques à la pioche en fonction de nbreliques

    Entrée : nbreliques (nombre de reliques à ajouter dans la pioche)

    Sortie : self.pioche (liste des cartes dans la pioche avec la ou les relique(s) ajoutée(s))
    """
    for i in range(nbreliques):
      if not len(self.liste_relique) <= 0: 
        self.pioche.insert(random.randrange(0,len(self.pioche)),self.liste_relique.pop(0))
    return self.pioche

  def pioche_carte(self):
    """
    Assigne la carte à l'emplacement 0 dans la liste pioche et la place dans une variable self.carte

    Entrée : /

    Sortie : self.carte (contient la carte tirée dans la pioche et est utilisée dans verif_carte principalement)
    """
    
    if len(self.pioche) <= 0 :
      return self.fintour()
    self.carte = self.pioche.pop(0) 
    return self.carte

  def affiche_joueurs(self):
    """
    Affiche les joueurs et leur statut ainsi que leurs diamants stockés sur eux et au campemant. (pas utilisé en mode graphique)

    Entrée : /

    Sortie : /
    """
    #nom joueur | statut | diamants temple | diamants total
    
    for i in range(len(self.joueurs)): #Boucle qui permet d'afficher les joueurs et leurs statuts
      print(self.joueurs[i].name,end =' ')
      if self.joueurs[i].ingame == True :
        print(f'(Dans le temple) |',end =' ')
      elif self.joueurs[i].ingame == False:
        print(f'(Au campement) |',end =' ')
      print(self.joueurs[i].diamants_manche,'diamants dans la poche |',end =' ')
      print(self.joueurs[i].diamants_total,'diamants stockés')
    print()
    return

  def affiche_cartes_jeu(self):
    """
    Affiche l'historique des cartes de la manche ainsi que le compte de diamants/reliques au sol (pas utilisé en mode graphique)

    Entrée : /

    Sortie : /
    """
    print(' ')
    for i in range(len(self.cartes_jeu)): #Boucle qui permet d'afficher les cartes tirées dans la manche
      if self.cartes_jeu[i] == "araignée" or self.cartes_jeu[i] =="serpent" or self.cartes_jeu[i] =="lave" or self.cartes_jeu[i] =="boulet" or self.cartes_jeu[i] =="bélier":
        print(f'          Danger : {self.cartes_jeu[i]}')
      elif type(self.cartes_jeu[i]) == int:
        print(f'          Trésor : {self.cartes_jeu[i]} diamants')
      else:
        print(f'          Relique : {self.cartes_jeu[i]}')

    print(' ')
    print(f'Diamants au sol : {self.diamants_sol}')
    if len(self.reliques_sol) > 0 :
      print('Reliques au sol :',end =' ')
      for i in range(len(self.reliques_sol)): #Boucle qui permet d'afficher les reliques au sol
        if i == len(self.reliques_sol) - 1:
          print(f'{self.reliques_sol[i]}',end =' ')
        else:
          print(f'{self.reliques_sol[i]}',end =', ')
      print(' ')
    print(' ')

  def verifcarte(self):
    """
    Vertifie la carte piochée pour exécuter les fonctions pour chaque type de carte (self.danger(), self.tresor(), self.relique()) 
    et dans le cas des diamants partage la valeur entre les joueurs avec la valeur renvoyée par self.tresor(), et ajoute la carte tirée dans la liste self.carte_jeu

    Entrée : /

    Sortie : /
    """
    if self.carte == "araignée" or self.carte =="serpent" or self.carte =="lave" or self.carte =="boulet" or self.carte =="bélier":
      self.danger(self.carte)
      carte = 'danger'
    elif type(self.carte) == int:
      self.tresor_partage = self.tresor(self.carte)
      for i in range(len(self.joueurs)): #Boucle qui permet de partager le trésor entre les joueurs en jeu
        if self.joueurs[i].ingame == True:
          self.joueurs[i].ajouter_diamants(self.tresor_partage,1)
      carte = 'tresor'
    else:
      self.decouvert.append(self.carte)
      self.relique()
      carte = 'relique'
    self.cartes_jeu.append(self.carte)
    return carte

  def tresor(self,tresor):
    """
    Partage le trésor parmis tous les joueurs présents dans le temple et l'affiche en changeant la variable self.caption utilisée dans la classe Diamant_Frame

    Entrée : tresor (valeur à partager (carte tirée dans self.verif_carte étant un int))

    Sortie : tresor divisé par le nombre de joueurs sur le plateau (self.joueurs_plateau)
    """
    self.caption = f'Il y a un trésor de {tresor} diamants !'
    self.diamants_sol += tresor % len(self.joueurs_plateau) #Ajoute les diamants restants au sol
    self.caption2 = f'Le trésor a été divisé en {len(self.joueurs_plateau)} parts de {tresor // len(self.joueurs_plateau)} diamants !'
    return tresor // len(self.joueurs_plateau) #Renvoie la valeur des diamants à partager
   
  def danger(self,danger):
    """
    Vérifie si il y a déjà un danger identique tiré dans la manche pour arrêter ou non la partie et l'affiche en modifiant self.caption utilisée dans la classe Diamant_Frame

    Entrée : danger (danger tiré dans pioche_carte() et vérifié dans verifcarte())

    Sortie : self.finmanche (fonction permettant de terminer la manche)
    """
    self.caption = f'Oh non ! Un danger de type {danger} arrive sur le plateau ! Attention !'
    for i in range(len(self.cartes_jeu)): #Boucle qui vérifie si il y a déjà un danger identique tiré dans la manche
      if self.cartes_jeu[i] == self.carte:
        return self.finmanche()
    return None
        
  def relique(self):
    """
    Ajoute la carte à la liste self.relique_sol pour que les joueurs puissent la ramasser en sortant du temps grâce à la fonction self.fintour() et l'écrit
    en modifiant la variable self.caption utilisée dans la classe Diamant_Frame

    Entrée : /

    Sortie : / (ajoute la relique dans la liste self.relique_sol)
    """
    self.caption = "Mais c'est une relique ! Incroyable ! Si vous décidez de sortir, vous repartez avec, mais attention, on ne peut pas la partager !"
    self.reliques_sol.append(self.carte)

  def choix_joueurs(self,joueur,choix):
    """
    Utilisée dans la fonction self.tour de la classe Diamant_Frame, cette fonction permet d'ajouter, si le paramètre choix est 'n', le joueur stocké dans dans le
    paramètre joueur est stocké dans une liste self.joueurs_sortir qui contient les joueurs ayant décidé de sortir du temple lors de la manche en cours.

    Entrée: joueur (joueur concerné par le choix), choix (choix entre 'y' et 'n' définit dans une messagebox dans une fonction de la classe Diamant_Frame)

    Sortie: / (Ajoute le joueur concerné dans la liste self.joueurs.sortir si son choix est 'n')
    
    """
    if choix == "n":
      self.joueurs_sortir.append(joueur)

  def choix_joueurs_exe(self):
    for i in range(len(self.joueurs)): #Boucle qui permet de retirer les joueurs sortant du plateau et de les mettre dans la liste self.joueurs_out
      if self.joueurs[i] in self.joueurs_plateau:
        if self.joueurs[i] in self.joueurs_sortir:
          self.joueurs[i].ingame = False
          self.joueurs[i].ajouter_diamants(self.joueurs[i].diamants_manche,2)
          self.joueurs[i].diamants_manche = 0
          self.joueurs_plateau.remove(self.joueurs[i])
          self.joueurs_out.append(self.joueurs[i])
          
  def fintour(self):
    """
    Fonction permettant d'amorcer la fin du tour et d'afficher les messages correspondants en modifiant les variables caption utilisées dans la fonction caption() de la classe Diamant_Frame. 
    Permet aussi de partager les diamants au sol entre les joueurs sortants et de donner la/les relique(s) au joueur sortant si celui-ci est seul.

    Entrée : /

    Sortie : / (modifie les variables caption, les données des objets des listes self.joueurs_out et modifie diamants_sol et reliques_sol)
    """
    if len(self.joueurs_out) == 1: #Si il n'y a qu'un joueur sortant, il récupère les diamants et la/les reliques au sol
      
      if len(self.reliques_sol) >= 1:
        self.caption = (f"{self.joueurs_out[0].name} sort seul et garde la relique pour lui seul ! Il gagne donc {self.valeur_reliques[self.i]} diamants !")
        
        for i in range(len(self.reliques_sol)):
          self.joueurs_out[0].ajouter_relique(self.reliques_sol[i], self.valeur_reliques[self.i])
          
        self.reliques_sol = []
        
      if self.diamants_sol >= 1:
        self.caption2 = (f"{self.joueurs_out[0].name} ramasse {self.diamants_sol} diamants sur son passage et les range dans son coffre au campement !")
        self.joueurs_out[0].ajouter_diamants(self.diamants_sol,2)
        self.diamants_sol = 0

      self.caption3 = f"{self.joueurs_out[0].name} sort du temple, il dépose ses diamants au campement."
        
    elif len(self.joueurs_out) > 1: #Si plusieurs joueurs sortent en même temps
      if len(self.reliques_sol) == 1:
        self.caption = ("Plusieurs joueurs ont quitté en même temps et n'ont pas pu se décider sur le partage de la relique, impossible de la couper en morceaux !")
        
      elif len(self.reliques_sol) > 1:
        self.caption = ("Plusieurs joueurs ont quitté en même temps et n'ont pas pu se décider sur le partage des reliques, ils ont donc décidé de les laisser dans le temple !")
        
      if self.diamants_sol >= 1:
        self.caption2 = (f"Le butin au sol a été divisé en {len(self.joueurs_out)} parts équitables de {self.diamants_sol // len(self.joueurs_out)} diamants.")
        
        for i in range(len(self.joueurs_out)): #Boucle qui permet de partager les diamants au sol entre les joueurs sortants
          self.joueurs_out[i].ajouter_diamants(self.diamants_sol // len(self.joueurs_out),2)
        self.diamants_sol = 0

      self.caption3 = "Les joueurs qui ont décidé de partir sortent du temple, ils déposent leurs diamants au campement."
    
  def finmanche(self):
    """
    Modifie le booléen self.statut en False pour signifier la fin de la manche à la fonction self.manche() qui va y mettre fin à l'aide d'une condition.

    Entrée : /

    Sortie : self.statut (booléan symbolisant le statut de la manche, True si celle-ci est en cours et False si elle doit être terminée)
    """
    self.statut = False
    return self.statut

class Joueur:

  def __init__(self,name):
    """
    Initialisation de la classe Joueur en définissant ses variables de base

    Entrée : name (nom du joueurs entré dans la fonction ecran_choix_noms() de la classe Diamant_Frame)

    Sortie : /
    """
    self.name = name #nom du joueur
    self.diamants_manche = 0 #diamants ramassés pendant la manche
    self.diamants_total = 0 #diamants ramassés pendant la partie stockés au campement
    self.reliques = [] #reliques ramassées pendant la partie stockées au campement
    self.ingame = True #booléen indiquant si le joueur est encore en jeu ou non
  
  def ajouter_diamants(self,diamants,where):
    """
    Ajoute des diamants au nombre de diamants des joueurs à la position demandée

    Entrée : diamants (nombre de diamants à ajouter), where (où les ajouter) -> options : 1 (dans la poche), 2 (au campement)

    Sortie : diamants_manche/diamants_total
    """
    if where == 1: #Si where = 1, on ajoute les diamants dans la poche du joueur
      self.diamants_manche += diamants
      return self.diamants_manche
    elif where == 2: #Si where = 2, on ajoute les diamants dans le coffre du campement du joueur
      self.diamants_total += diamants
      return self.diamants_total


  def ajouter_relique(self,relique,valeur):
    """
    Ajoute une relique et sa valeur en diamants dans le coffre du campement du joueur.

    Entrée : relique, valeur (valeur de la relique en diamants)

    Sortie : diamants_total (nouvelle valeur), reliques (liste des reliques possédées par le joueur)
    """
    self.diamants_total += valeur #On ajoute la valeur de la relique au nombre de diamants du joueur
    self.reliques.append(relique) #On ajoute la relique à la liste des reliques du joueur
    return self.diamants_total,self.reliques #On retourne les nouvelles valeurs


class Diamant_Frame:

  def __init__(self):
    """
    Initialisation de la classe Diamant_Frame en définissant ses variables de base et en créant la fenetre self.fenetre grâce au module Tkinter

    Entrée : /

    Sortie : /
    """
    self.fenetre = tk.Tk() #Création de la fenetre
    self.fenetre.geometry('1080x720') #Taille de la fenetre
    self.fenetre.title('Diamant') #Titre de la fenetre
    self.fenetre['bg'] = '#EEEEEE' #Couleur de fond de la fenetre
    self.fenetre.resizable(height=False,width=False) #On empêche la fenetre de se redimensionner
    
    self.p = Partie() #Création d'une instance de la classe Partie
    self.images = {1:'images/diam_1.png',2:'images/diam_2.png',3:'images/diam_3.png', 4:'images/diam_4.png', 5:'images/diam_5.png',7:'images/diam_7.png',9:'images/diam_9.png',11:'images/diam_11.png',13:'images/diam_13.png',14:'images/diam_14.png',15:'images/diam_15.png',17:'images/diam_17.png','araignée':'images/araignee','serpent':'images/serpent.png','lave':'images/lave.png','boulet':'images/boulet.png','bélier':'images/belier.png','Le Totem de Wennawenna (5)':'images/rel_1.png',"Le Masque de l'Arojam (5)":'images/rel_2.png','La Statue du Deiporg (5)':'images/rel_3.png',"Le Pot d'Or de Toukapatou (10)":'images/rel_4.png',"Le Talisman du Treblig (10)":'images/rel_5.png'}
    #Création d'un dictionnaire contenant les images des diamants et des dangers, ainsi que les images des reliques
    for i in range(1,18): #On parcourt les images des diamants
      if i != 6 and i != 8 and i != 10 and i != 12 and i != 16:
        self.images[i] = tk.PhotoImage(file=f'images/diam_{i}.png') #On ajoute les images des diamants au dictionnaire
    for i in self.p.liste_danger: #On parcourt les images des dangers
      self.images[i] = tk.PhotoImage(file=f'images/{i}.png') #On ajoute les images des dangers au dictionnaire
    for i in range(len(self.p.liste_relique)): #On parcourt les images des reliques
      self.images[self.p.liste_relique[i]] = tk.PhotoImage(file=f'images/rel_{i+1}.png') #On ajoute les images des reliques au dictionnaire
    self.ecran_choix_nombre()
    
    
    self.fenetre.mainloop() #boucle de fonctionnement
    
  def partie(self):
    """
    Fonction principale permettant de faire fonctionner une partie de Diamant en créant une boucle éxecutant les 5 manches du jeu. 
    Et exécutant les fonctions de fin de partie une fois la boucle terminée
    
    Entrée : /
    
    Sortie : /
    """
    for self.i in range(5):
      #Initialisation de toutes les parties graphiques de la manche
      self.update_num_manche() 
      self.init_liste_cartes()
      self.update_liste_joueurs()
      self.update_nb_diams_sol()
      self.update_liste_reliques_sol()
      self.caption()

      self.manche()
      self.p.reset_manche()
    self.remove_all() #On supprime toutes les parties graphiques de la manche
    self.ecran_fin() #On affiche l'écran de fin de partie

  def manche(self):
    """
    Fonction pricipale gérant chaque manche de la partie et gérée par la boucle de la fonction partie()

    Entrée : /

    Sortie : /
    """
    self.p.melange(self.i) #On mélange la pioche
    self.p.add_relique(self.i +1 - self.p.nbdecouvert) #On ajoute la relique de la manche à la liste des reliques possibles
    while True:
      self.remove_all() #On supprime toutes les parties graphiques pour les recréer correctement
      self.update_num_manche()
      self.update_liste_joueurs()
      self.p.pioche_carte() #On pioche une carte
      self.reset_caption_var() #On réinitialise les variables de la légende
      self.p.verifcarte() #On vérifie si la carte piochée est un danger, un trésor ou une relique
      if self.ecran_deux_pieges() == True: #Si la carte piochée est un danger, on vérifie si il a déjà été tiré
        return #Si oui, on arrête la manche
      self.update_liste_cartes() 
      self.caption()
      if self.p.statut == False :
        return #Si le statut a été changé en False, on arrête la manche
      #self.p.affiche_cartes_jeu() 
      self.update_liste_joueurs()
      self.update_nb_diams_sol()
      self.update_liste_reliques_sol()
      self.continuer()
      self.reset_caption_var()
      self.question_joueur() #On demande à chaque joueur s'il veut continuer ou non
      self.caption()
      self.reset_caption_var()
      self.p.fintour()
      self.caption()
      self.p.joueurs_out = [] #On réinitialise la liste des joueurs en dehors du temple avant de terminer la manche
      if len(self.p.joueurs_plateau) == 0: #Si il n'y a plus de joueurs sur le plateau, on arrête la manche (le statut est changé en False dans la fonction finmanche())
        self.p.finmanche()
      if self.p.statut == False : #Si le statut a été changé en False, on arrête la manche
        return

  def ecran_choix_nombre(self):
    """
    Demande le nombre de joueurs à l'utilisateur à l'aide de boutons et execute la fonction ecran_choix_noms en conséquence

    Entrée : /

    Sortie : /
    """
    self.choix_nombre = tk.Frame(self.fenetre) 
    self.choix_nombre.pack(expand='YES')
    texte_boutons = tk.Label(self.choix_nombre, text='Choisissez le nombre de joueurs...',font=("Calibri",20))
    texte_boutons.pack()
    boutons = tk.Frame(self.choix_nombre) #On crée un frame pour les boutons
    boutons.pack(pady=15)
    self.texte_choix_nom = tk.Label(self.fenetre, text='Entrez le nombre de joueurs...', font=("Calibri", 20))
    #On crée un bouton pour chaque nombre de joueurs possible
    bouton_3 = tk.Button(boutons, text=" 3 ", command=lambda :self.ecran_choix_noms(3),font=("Calibri",20)) 
    bouton_3.pack(side='left',padx=10)
    bouton_4 = tk.Button(boutons, text=" 4 ", command=lambda :self.ecran_choix_noms(4),font=("Calibri",20))
    bouton_4.pack(side='left',padx=10)
    bouton_5 = tk.Button(boutons, text=" 5 ", command=lambda :self.ecran_choix_noms(5),font=("Calibri",20))
    bouton_5.pack(side='left',padx=10)
    bouton_6 = tk.Button(boutons, text=" 6 ", command=lambda :self.ecran_choix_noms(6),font=("Calibri",20))
    bouton_6.pack(side='left',padx=10)
    bouton_7 = tk.Button(boutons, text=" 7 ", command=lambda :self.ecran_choix_noms(7),font=("Calibri",20))
    bouton_7.pack(side='left',padx=10)
    bouton_8 = tk.Button(boutons, text=" 8 ", command=lambda :self.ecran_choix_noms(8),font=("Calibri",20))
    bouton_8.pack(side='left',padx=10)
    
  def ecran_choix_noms(self,nb):
    """
    Interface permettant à chaque joueur d'entrer son nom à partir du nombre demandé dans la fonction précédente (ecran_choix_nombre()) et d'afficher les règles une fois fait

    Entrée : nb (int) : nombre de joueurs

    Sortie : /
    """
    self.nbjoueurs = nb #On stocke le nombre de joueurs dans une variable de la classe
    self.choix_nombre.destroy()
    self.choix_noms= tk.Frame(self.fenetre) #On crée un frame pour les entrées de texte
    self.choix_noms.pack(expand='YES')
    joueurs = [] #On crée une liste pour stocker les entrées de texte
    for i in range(nb): #On crée une entrée de texte pour chaque joueur
      tk.Label(self.choix_noms,text="Nom du joueur "+ str(i+1) + " : ",font=('Calibri', 18)).pack()
      joueurs.append(tk.Entry(self.choix_noms,font=('Calibri', 15)))
      joueurs[i].insert(0,"Joueur " + str(i+1))
      joueurs[i].pack(pady=5)
    bouton_joueurs = tk.Button(self.choix_noms, text="Confirmer", font=("Calibri",20), command=lambda: [self.p.settings_joueurs(joueurs),self.choix_noms.destroy(),self.ecran_affiche_regles()]).pack(pady=15) #On crée un bouton pour valider les noms et lancer la fonction ecran_affiche_regles()

  def ecran_affiche_regles(self):
    """
    Affiche les règles du jeu à l'utilisateur et lui permet de lancer la partie une fois qu'il a lu les règles en appuyant sur le bouton

    Entrée : /

    Sortie : /
    """
    self.affiche_regles= tk.Frame(self.fenetre) #On crée un frame pour les règles
    self.affiche_regles.pack(expand='YES')
    tk.Label(self.affiche_regles, text='Bonjour, je suis M.Hayes, je serais votre guide tout au long de votre aventure des les temples de Wenawena !',font=("Calibri",15)).grid(row=0,sticky='W')
    tk.Label(self.affiche_regles, text=' ', font=('Calibri',10)).grid(row=1,sticky='W')
    tk.Label(self.affiche_regles, text='Voici le déroulement de votre aventure :',font=("Calibri",15)).grid(row=2,sticky='W')
    tk.Label(self.affiche_regles, text=' ', font=('Calibri',10)).grid(row=3,sticky='W')
    tk.Label(self.affiche_regles, text="L'aventure se joue en 5 manches.",font=("Calibri",15)).grid(row=4,sticky='W')
    tk.Label(self.affiche_regles, text="Chaque tour , une carte est piochée, celle-ci peut être une relique, un piège ou un trésor.",font=("Calibri",15)).grid(row=5,sticky='W',padx=5)
    tk.Label(self.affiche_regles, text="- La relique est laissée au sol et sera donnée au prochain joueur qui sortira du temple si il est seul.",font=("Calibri",15)).grid(row=6,sticky='W',padx=10)
    tk.Label(self.affiche_regles, text="- Le piège n'a pas de réel impact sauf si un piège identique a déjà été tiré lors de la manche actuelle.",font=("Calibri",15)).grid(row=7,sticky='W',padx=10)
    tk.Label(self.affiche_regles, text="Dans ce cas, la manche prend fin et tous les joueurs encore présents dans le temple perdent tout le contenu de leur poche.",font=("Calibri",15)).grid(row=8,sticky='W',padx=15)
    tk.Label(self.affiche_regles, text="- Le trésor est une valeur en diamant qui est partagée équitablement entre tous les joueurs présents dans le temple.",font=("Calibri",15)).grid(row=9,sticky='W',padx=10)
    tk.Label(self.affiche_regles, text=' ', font=('Calibri',10)).grid(row=10,sticky='W')
    tk.Label(self.affiche_regles, text="A la fin de chaque tour les joueurs peuvent choisir de continuer d'explorer ou de rentrer au campement.",font=("Calibri",15)).grid(row=11,sticky='W')
    tk.Label(self.affiche_regles, text="Si il y a des diamant sur le sol lors de la sortie du temple, ceux-ci sont partagés entre tous les joueurs.",font=("Calibri",15)).grid(row=12,sticky='W')
    tk.Label(self.affiche_regles, text="Les aventuriers ont pour but de terminer les 5 manches avec le plus de diamants au campement.",font=("Calibri",15)).grid(row=13,sticky='W')
    tk.Label(self.affiche_regles, text=' ', font=('Calibri',10)).grid(row=14,sticky='W')
    tk.Label(self.affiche_regles, text="Vous avez tout compris ? Alors bonne chance aventuriers !",font=("Calibri",15)).grid(row=15,sticky='W')
    tk.Button(self.affiche_regles, text='Commencer la partie !', font=('Calibri',20),command=lambda: [self.affiche_regles.destroy(),self.ecran_main_jeu()]).grid(row=16,pady=20) #On crée un bouton pour lancer la partie

  def ecran_main_jeu(self):
    """
    Exécute la fonction self.partie() qui permet de lancer la partie

    Entrée : /
    
    Sortie : /
    """
    self.partie() #On lance la partie	

  def ecran_fin(self):
    """
    Affiche l'écran de fin de partie et affiche le vainqueur de la partie ou une égalité si il y en a une entre plusieurs joueurs et permet de relancer une partie 

    Entrée : /

    Sortie : / (peut relancer une partie)
    """
    self.texte_fin = tk.Frame(self.fenetre) #On crée un frame pour afficher le texte de fin de partie
    self.texte_fin.pack(expand='YES')
    tk.Label(self.texte_fin, text="PARTIE TERMINÉE !",font=("Calibri",25,"bold")).pack()
    tk.Label(self.texte_fin, text="Félicitations aventuriers ! Vous avez tous réuni un maximum de diamants au péril de votre vie !",font=("Calibri",15)).pack()
    tk.Label(self.texte_fin, text="Mais l'aventurier qui possède le plus de diamants est...",font=("Calibri",15)).pack()
    if self.p.verif_victoire() == 'egalite': #On vérifie si il y a une égalité entre plusieurs joueurs
      tk.Label(self.texte_fin, text="Et c'est une égalité entre deux aventuriers. Malheureusement, il n'y a pas de gagants !",font=("Calibri",15)).pack()
    else: #Sinon on affiche le vainqueur
      tk.Label(self.texte_fin, text=f"{self.p.joueurs[self.p.indice_max].name} avec {self.p.joueurs[self.p.indice_max].diamants_total} diamants ! Félicitations à lui !",font=("Calibri",15, 'bold')).pack()
    tk.Label(self.texte_fin, text="Résumé :",font=("Calibri",15)).pack()
    for i in range(len(self.p.joueurs)): #On affiche le résumé de la partie pour chaque joueur
      tk.Label(self.texte_fin, text=f"{self.p.joueurs[i].name} : ",font=("Calibri",15)).pack()
      tk.Label(self.texte_fin, text=f"{self.p.joueurs[i].diamants_total} diamants au total",font=("Calibri",10)).pack(pady=5)
    
    tk.Button(self.texte_fin, text='Rejouer', font=('Calibri',20),command=lambda: [self.texte_fin.destroy(),self.ecran_main_jeu()]).pack(pady=20) #On crée un bouton pour relancer une partie
    
  def ecran_deux_pieges(self):
    """
    S'affiche si deux pièges sont tirés lors d'une manche (avec la variavle self.p.statut modifiée dans self.p.danger) et permet de passer à la manche suivante

    Entrée : /

    Sortie : True (si deux pièges sont tirés et donc que self.p.statut == False) ou rien (si deux pièges ne sont pas tirés et donc que self.p.statu == True)
    """
    if self.p.statut == False: #Si deux pièges sont tirés
      self.remove_all() 
      self.texte_deux_pieges = tk.Frame(self.fenetre) #On crée un frame pour afficher le texte de fin de manche
      self.texte_deux_pieges.pack(pady=200)
      tk.Label(self.texte_deux_pieges, text="DEUX PIÈGES IDENTIQUES !",font=("Calibri",25,"bold")).pack()
      tk.Label(self.texte_deux_pieges, text="Malheureusement, deux pièges identiques ont été tirés lors de cette manche.",font=("Calibri",15)).pack()
      tk.Label(self.texte_deux_pieges, text="La manche prend fin et tous les joueurs encore présents dans le temple perdent tout le contenu de leur poche.",font=("Calibri",15)).pack()
      tk.Label(self.texte_deux_pieges, text="Cliquez sur le bouton pour passer à la manche suivante....",font=("Calibri",15)).pack()
      tk.Label(self.fenetre, image=self.images[self.p.carte]).place(x=425,y=350) #On affiche le piège tiré
      tk.Label(self.fenetre, image=self.images[self.p.carte]).place(x=575,y=350) #On affiche la piège tiré
      self.continuer() #On crée un bouton pour passer à la manche suivante
      return True #On retourne True pour indiquer que deux pièges ont été tirés

  def liste_joueurs(self):
    """
    Affiche la liste des joueurs, leur statut, leur nombre de diamants dans la poche et au campement.

    Entrée : /
    
    Sortie : /
    """
    self.frame_liste_joueurs = tk.Frame(self.fenetre,borderwidth=1, relief="solid",padx=5) #On crée un frame pour afficher la liste des joueurs
    self.frame_liste_joueurs.place(x=875,y=25,width=200)
    list_frames_joueurs = [] #On crée une liste de frames pour afficher les informations de chaque joueur
    for i in range(self.nbjoueurs): #On parcourt la liste des joueurs
      list_frames_joueurs.append(tk.Frame(self.frame_liste_joueurs,borderwidth=1, relief="solid",padx=5)) #On crée un frame pour chaque joueur
      list_frames_joueurs[i].pack(pady=5,fill='both')
      tk.Label(list_frames_joueurs[i],text=f"{self.p.joueurs[i].name}",font=('Calibri', 10)).pack() #On affiche le nom du joueur
      if self.p.joueurs[i].ingame == True: #On affiche le statut du joueur
        tk.Label(list_frames_joueurs[i],text="Dans le temple",font=('Calibri', 10), fg='green').pack()
      else:
        tk.Label(list_frames_joueurs[i],text="Au campement",font=('Calibri', 10), fg='red').pack()
      tk.Label(list_frames_joueurs[i],text=f"Poche : {self.p.joueurs[i].diamants_manche}",font=('Calibri', 10)).pack(side='left') #On affiche le nombre de diamants de la poche joueur
      tk.Label(list_frames_joueurs[i],text=f"Campement : {self.p.joueurs[i].diamants_total}",font=('Calibri', 10)).pack(side='right') #On affiche le nombre de diamants au campement du joueur

  def update_liste_joueurs(self):
    """
    Met a jour la liste des joueurs en détruisant la liste actuelle et en en créant une nouvelle

    Entrée : /

    Sortie : /
    """
    try: #On essaie de détruire la liste des joueurs
      self.frame_liste_joueurs.destroy()
      self.liste_joueurs()
    except: #Si la liste des joueurs n'existe pas, on la crée
      self.liste_joueurs()


  def init_liste_cartes(self):
    """
    Initialise la liste des cartes tirées lors de la manche et les coordonnées de base des cartes pour leur affichage

    Entrée : /

    Sortie : /
    """
    self.liste_cartes_graph = [] #On crée une liste pour stocker les images des cartes tirées
    self.carte_y = 50 #On initialise les coordonnées de base des cartes

  def update_liste_cartes(self):
    """
    Met à jour la liste des cartes tirées lors de la manche en détruisant les cartes actuelles et en en créant de nouvelles

    Entrée : /

    Sortie : /
    """
    for i in range(len(self.liste_cartes_graph)): #On parcourt la liste des cartes tirées
      self.liste_cartes_graph[i].destroy() #On détruit les cartes
    self.liste_cartes() #On crée de nouvelles cartes

  def liste_cartes(self):
    """
    Affiche la liste des cartes sous forme d'images

    Entrée : /

    Sortie : /
    """
    x = 10 #On initialise les coordonnées de base des cartes
    self.carte_y = 50
    for i in range(len(self.p.cartes_jeu)): #On parcourt la liste des cartes tirées
      if i%8 == 0 and i != 0: #On change les coordonnées de base des cartes pour les afficher sur une deuxième ligne si on a plus de 8 cartes
        x = 10
        self.carte_y = 210
      elif i != 0: #On change les coordonnées de base des cartes pour les afficher en ligne si on a moins de 8 cartes
        x = x + 100
        
      self.liste_cartes_graph.append(tk.Label(self.fenetre, image=self.images[self.p.cartes_jeu[i]])) #On crée une image pour chaque carte tirée
      self.liste_cartes_graph[len(self.liste_cartes_graph)-1].place(x=x,y=self.carte_y) #On affiche l'image de la carte aux coordonnées correspondantes

  def continuer(self):
    """
    Affiche le bouton continuer et met en pause de programme tant que celui-ci n'est pas affiché

    Entrée : /

    Sortie : /
    """
    var = tk.IntVar() #On crée une variable pour le bouton continuer qui sera modifiée lorsqu'on appuiera sur le bouton
    continuer_bouton = tk.Button(self.fenetre, text='   Continuer   ', font=('Calibri',20),command=lambda: var.set(1)) #On crée le bouton continuer
    continuer_bouton.place(x=150,y=575)
    continuer_bouton.wait_variable(var) #On met en pause le programme tant que le bouton continuer n'est pas cliqué 
    continuer_bouton.destroy() #On détruit le bouton une fois cliqué

  def remove_all(self):
    """
    Vide la fenêtre de tous les objets tkinter

    Entrée : /

    Sortie : /
    """
    for widget in self.fenetre.winfo_children(): #On parcourt tous les objets tkinter de la fenêtre
      widget.destroy() #On détruit tous les objets

  def num_manche(self):
    """
    Affiche le numéro de la manche

    Entrée : /

    Sortie : /
    """
    self.num_manche_label = tk.Label(self.fenetre,text=f"Manche n°{self.i+1}",font=('Calibri', 15)) #On affiche le numéro de la manche
    self.num_manche_label.pack(side='top')

  def update_num_manche(self):
    """
    Met à jour le numéro de manche en détruisant l'ancien pour en créer un nouveau

    Entrée : /

    Sortie ; /
    """
    try: #On essaie de détruire le numéro de manche
      self.num_manche_label.destroy()
      self.num_manche()
    except: #Si le numéro de manche n'existe pas, on le crée
      self.num_manche()

  def caption(self):
    """
    Affiche la légende à partir des variables de la classe Partie self.caption_1, self.caption_2 et self.caption_3

    Entrée : /

    Sortie : /
    """
    try: #On essaie de détruire la légende
      self.caption_frame_frame.destroy()
    except: #Si la légende n'existe pas, on la crée
      pass
    #On répète la même opération pour chaque varible caption
    try: 
      self.caption_1.destroy()
    except:
      pass
    try:
      self.caption_2.destroy()
    except:
      pass
    try:
      self.caption_3.destroy()
    except:
      pass
    self.caption_frame_frame = tk.Frame(self.fenetre,borderwidth=1, relief="solid",padx=5) #On crée une frame pour la légende
    self.caption_frame_frame.place(x=850,y=450,width=800,anchor='e')
    if len(self.p.caption) > 1: #Si la variable caption n'est pas vide, on l'affiche
      self.caption_1 = tk.Label(self.caption_frame_frame,text=self.p.caption)
      self.caption_1.pack()
    if len(self.p.caption2) > 1: #Si la variable caption2 n'est pas vide, on l'affiche
      self.caption_2 = tk.Label(self.caption_frame_frame,text=self.p.caption2)
      self.caption_2.pack()
    if len(self.p.caption3) > 1: #Si la variable caption3 n'est pas vide, on l'affiche
      self.caption_3 = tk.Label(self.caption_frame_frame,text=self.p.caption3)
      self.caption_3.pack()
  
  def reset_caption_var(self):
    """
    Réininitialise les variables de la classe Partie self.caption_1, self.caption_2 et self.caption_3çjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj

    Entrée : /

    Sortie : /
    """
    self.p.caption = '.'
    self.p.caption2 = '.'
    self.p.caption3 = '.'

  def nb_diams_sol(self):
    """
    Affiche le nombre de diamants au sol

    Entrée : /

    Sortie : /
    """
    self.diamants_sol = tk.Label(self.fenetre,text=f"Diamants au sol : {self.p.diamants_sol}",font=('Calibri', 15)).place(x=150,y=500) #On affiche le nombre de diamants au sol

  def update_nb_diams_sol(self):
    """
    Met à jour le nombre de diamants au sol en détruisant l'ancien pour en créer un nouveau

    Entrée : /

    Sortie : /
    """
    try:  #On essaie de détruire le nombre de diamants au sol
      self.diamants_sol.destroy()
      self.nb_diams_sol()
    except: #Si le nombre de diamants au sol n'existe pas, on le crée
      self.nb_diams_sol()

  def question_joueur(self):
    """
    Affiche des messagebox qui demandent à chaque joueur si il veut continuer d'explorer ou non

    Entrée : /

    Sortie : /
    """
    self.p.joueurs_sortir = [] #indice des joueurs qui sortent du temple
    for i in range(len(self.p.joueurs)): #On parcourt la liste des joueurs
      if self.p.joueurs[i] in self.p.joueurs_plateau: #Si le joueur est sur le plateau
        rep = messagebox.askquestion(f"{self.p.joueurs[i].name}", f"{self.p.joueurs[i].name} voulez-vous continuer d'explorer ?") #On demande au joueur s'il veut continuer d'explorer
        if rep == 'yes':
          self.p.choix_joueurs(self.p.joueurs[i],'o')
        elif rep == 'no':
          self.p.choix_joueurs(self.p.joueurs[i],'n')
    self.p.choix_joueurs_exe() #On exécute les choix des joueurs

  def liste_reliques_sol(self):
    """
    Affiche la liste des reliques au sol

    Entrée : /

    Sortie : /
    """
    self.reliques_sol = tk.Frame(self.fenetre,bg='#EEEEEE') #On crée une frame pour la liste des reliques au sol
    self.reliques_sol.place(x=400,y=500)
    tk.Label(self.reliques_sol, text='Reliques au sol :',font=('Calibri', 15)).pack()
    for i in range(len(self.p.reliques_sol)): #On parcourt la liste des reliques au sol
      tk.Label(self.reliques_sol,text=f'- {self.p.reliques_sol[i]}',font=('Calibri', 14)).pack() 
    for i in range(5 - len(self.p.reliques_sol)): #On ajoute des lignes vides pour que la liste soit toujours de la même taille
      tk.Label(self.reliques_sol,text='-                           ',font=('Calibri', 14),bg='#EEEEEE').pack()
  
  def update_liste_reliques_sol(self):
    """
    Met à jour la liste des reliques au sol en détruisant l'ancienne pour en créer une nouvelle.

    Entrée : /

    Sortie : /
    """
    try: #On essaie de détruire la liste des reliques au sol
      self.reliques_sol.destroy()
      self.liste_reliques_sol()
    except: #Si la liste des reliques au sol n'existe pas, on la crée
      self.liste_reliques_sol()


df = Diamant_Frame() #On crée une instance de la classe Diamant_Frame

"""
Fonction pour dire à Mehmet de faire un kebab
"""

