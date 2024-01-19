
# Modification date: Fri Apr  1 16:07:22 2022

# Production date: Sun Sep  3 15:42:59 2023

import pygame
from math import sqrt
pygame.init()



class Bullet:
    def __init__(self, x, y, vel, imgdroite):
        """
        C'est une fonction qui défini/crée la balle de joueur. Elle est crée quand le joueur appuie sur le bouton 'espace'.

        Les parametres: x coordonnée de la balle(x, int), y coordonnée de la balle(y, int), la vélocite de la balle(vel, int), image de la balle(img, pygame.image.load()), l'animation de la balle(imgdroite, list)
        """
        self.x = x
        self.y = y
        self.vel = vel
        self.imgdroite = imgdroite
        self.imggauche = imgdroite[::-1]
        self.compteur = 0
        

    def distance(self, ennemi):
        """
        C'est une fonction qui retour la calcule la distance entre l'ennemi et la balle.
        
        Elle prend la parametre ennemi(ennemi, la classe Ennemi)
        """
        return sqrt(((self.x + 8) - (ennemi.x + 64))**2 + ((self.y + 8) - (ennemi.y + 64))**2)

    def deplacer(self, ennemis, bullets):
        """
        C'est une fonction qui déplace la balle du joueur, si elle est assez proche à un ennemi il subit de degat et s'éfface de la liste des balles.

        Les parametres: la liste d'ennemis(ennemis, list), la liste des balles(bullets, list)
        """
        self.x += self.vel
        if self.x < -32 or self.x > 1112 and self:
            bullets.remove(self)
        for ennemi in ennemis:
            if self.distance(ennemi) < 32:
                ennemi.hp -= 75
                try:
                    bullets.remove(self)
                except:
                    pass
                return
        return
    # dessiner le joueur sur l'ecran
    def draw(self, win):
        """
        C'est une fonction qui affiche et fait l'animation de la balle sur l'ecran.

        Les parametres: la fenêtre du jeu(win, pygame.display.set_mode())
        """
        if self.vel > 0:
            if self.compteur==len(self.imgdroite):
                self.compteur=0
            win.blit(self.imgdroite[self.compteur], (self.x, self.y))
            self.compteur=self.compteur +1
        elif self.vel < 0:
            if self.compteur==len(self.imggauche):
                self.compteur=0
            win.blit(self.imggauche[self.compteur], (self.x, self.y))
            self.compteur=self.compteur +1


