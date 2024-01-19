
# Modification date: Sun Apr  3 13:52:22 2022

# Production date: Sun Sep  3 15:42:59 2023

import pygame
from math import sqrt
from c_Ebullet import *
import os
path = os.getcwd()
pygame.init()

#l'image de la balle d'ennemi
ebullet_img = pygame.image.load(path + "/assets/ebullet.png")
son_laser = pygame.mixer.Sound('assets/son/laser.wav')


class Ennemid:
    def __init__(self,x,y,image, vel, imgmarcher, hp):
        """
        C'est une fonction qui définit/crée un ennemi qui tire de loin.
        
        Les parametres: x coordonnée de l'ennemi(x, int), y coordonnée de l'ennemi(y, int), image de l'ennemi(image, pygame.image.load()), la vélocite(vitesse de marche) de l'ennemi(vel, int), les images de l'animation pour marcher(imgmarcher, list), le point de vie d'ennemi(hp, int)
        """
        self.x = x
        self.y = y
        self.image = image
        self.vel = vel
        self.maxhp, self.hp = hp, hp
        self.width=128
        self.height=128
        self.droite = False
        self.gauche = True
        self.bg = False
        self.bd = False
        self.imgmarcher = imgmarcher
        self.compteur = 0
        self.compteur_tire = 30


    def deplacer(self, player):
        """
        C'est une fonction qui déplace l'ennemi vers le joueur et qui fait l'arrêter quand il est assez proche(pour tirer)
        
        Elle prend la parametre joueur(joueur, la classe Player)
        """
        if abs(player.x - self.x) > 380:
            if player.x > self.x :#le mummy décide s'il va vers la droite 
                self.x = self.x + self.vel
                self.droite = True
                self.gauche = False
                self.bg = False
                self.bd = True
                
            if player.x < self.x:#le mummy décide s'il va vers la gauche
                self.x = self.x - self.vel
                self.droite = False
                self.gauche = True
                self.bg = True
                self.bd = False
        else:
            self.droite = False
            self.gauche = False
			
        return
    # dessiner l'ennemi sur l'ecran, fait une animation s'il est en train de marcher
    def draw(self, win, joueur):
        """
        C'est une fonction qui affiche l'ennemi sur l'ecran, fait une animation s'il est en train de marcher.

        Les parametres: la fenêtre du jeu(win, pygame.display.set_mode()), joueur(joueur, la classe Player)
        """
        if abs(joueur.x - self.x) > 380:
            if self.bg or self.bd:
                if self.compteur==24:
                    self.compteur=0
                win.blit(self.imgmarcher[self.compteur], (self.x, self.y))
                self.compteur=self.compteur +1
        else:
            win.blit(self.image, (self.x, self.y))

    #pour faire baisser la vie du joueur
    def frappe(self, joueur, ebullets, ennemis):
        """
        C'est une fonction qui fait tirer l'ennemi quand il est assez proche au joueur.

        Les parametres: joueur(joueur, la classe Player), la liste des balles d'ennemis(ebullets, list)
        """
        if abs(joueur.x - self.x) < 400 and self.compteur_tire >= 30 and self.x > -64 and self.x < 1080 - 64:
            if self.x + self.width < joueur.x + 100:
                ebulvel = 30
            else:
                ebulvel = -30
            ebullets.append(Ebullet(self.x + 64, self.y + 64, ebulvel, ebullet_img))
            self.compteur_tire = 0
            son_laser.play()
            self.bd, self.bg = False, False
            return
        else:
            self.compteur_tire += 1
  