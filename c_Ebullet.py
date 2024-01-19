
# Modification date: Sun Apr  3 12:38:38 2022

# Production date: Sun Sep  3 15:42:59 2023

import pygame
from math import sqrt
pygame.init()



class Ebullet:
    def __init__(self, x, y, vel, img):
        """
        C'est une fonction qui défini/crée la balle d'ennemi. Elle est crée quand l'ennemi qui tire de loin est assez proche.

        Les parametres: x coordonnée de la balle(x, int), y coordonnée de la balle(y, int), la vélocite de la balle(vel, int), image de la balle(img, pygame.image.load())
        """
        self.x = x
        self.y = y
        self.vel = vel
        self.img = img

    def deplacer(self, player, ebullets):
        """
        C'est une fonction qui déplace la balle d'ennemi, si elle est assez proche il subit de degat et s'éfface de la liste des balles d'ennemis.

        Les parametres: joueur(joueur, la classe Player), la liste des balles d'ennemis(ebullets, list)
        """
        self.x += self.vel
        if abs(player.x + 50 - self.x) < 32 or abs(player.x + 150 - self.x) < 8:
            if abs(player.y + 180 - self.y > 32) or player.y + 120 > self.y:
                player.hp -= 15
                ebullets.remove(self)

    # dessiner le joueur sur l'ecran
    def draw(self, win):
        """C'est une fonction qui affiche la balle sur l'ecran.

        Les parametres: la fenêtre du jeu(win, pygame.display.set_mode())
        """
        win.blit(self.img, (self.x, self.y))




