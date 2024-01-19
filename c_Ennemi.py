
# Modification date: Sun Apr  3 12:45:10 2022

# Production date: Sun Sep  3 15:42:59 2023

import pygame
from math import sqrt
pygame.init()




class Ennemi:
    def __init__(self,x,y,image, vel, imgmarchergauche, imgmarcherdroite, hp):
        """
        C'est une fonction qui définit/crée un ennemi qui frappe de proche.
        
        Les parametres: x coordonnée de l'ennemi(x, int), y coordonnée de l'ennemi(y, int), image de l'ennemi(image, pygame.image.load()), la vélocite(vitesse de marche) de l'ennemi(vel, int), les images de l'animation pour marcher vers gauche(imgmarcher, list), les images de l'animation pour marcher vers droite(imgmarcherdroite, list), le point de vie d'ennemi(hp, int)
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
        self.imgmarcherdroite = imgmarcherdroite
        self.imgmarchergauche = imgmarchergauche
        self.compteur = 0

    def distance(self, joueur):
        """
        C'est une fonction qui retour la calcule la distance entre l'ennemi et le joueur.
        Elle prend la parametre joueur(joueur, la classe Player)
        """
        return sqrt(((self.x + self.width//2) - (joueur.x + 100))**2 + ((self.y + self.height//2) - (joueur.y + 100))**2)


    def deplacer(self, player):
        """
        C'est une fonction qui déplace l'ennemi vers le joueur.
        
        Elle prend la parametre joueur(joueur, la classe Player)
        """
        if player.x + 100 > self.x + 64 :#la momie décide s'il va vers la droite 
            self.x = self.x + self.vel
            self.droite = True
            self.gauche = False
            self.bg = False
            self.bd = True
            
        else:#la momie décide s'il va vers la gauche
            self.x = self.x - self.vel
            self.droite = False
            self.gauche = True
            self.bg = True
            self.bd = False
			
        return
    # dessiner l'ennemi sur l'ecran
    def draw(self, win, joueur):
        """
        C'est une fonction qui affiche l'ennemi sur l'ecran, fait une animation s'il est en train de marcher.

        Les parametres: la fenêtre du jeu(win, pygame.display.set_mode()), joueur-il n'est pas utilisé, mais c'est important pour le boucle dans main.py-(joueur, la classe Player)
        """
        if self.bg:
            if self.compteur==24:
                self.compteur=0
            win.blit(self.imgmarchergauche[self.compteur], (self.x, self.y))
            self.compteur=self.compteur +1

			
        elif self.bd:
            if self.compteur==24:
                self.compteur=0
            win.blit(self.imgmarcherdroite[self.compteur], (self.x, self.y))
            self.compteur=self.compteur +1
            
        else:
            win.blit(self.image, (self.x, self.y))

    #pour faire baisser la vie du joueur
    def frappe(self, joueur, ebullets, ennemis):
        #si la distance entre le joueur et le méchant est inférireur à 100, la vie du joueur baisse
        if self.distance(joueur) < 100:
            joueur.hp=joueur.hp-1
  