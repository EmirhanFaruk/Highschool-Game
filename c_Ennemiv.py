
# Modification date: Sun Apr  3 16:05:30 2022

# Production date: Sun Sep  3 15:42:59 2023

import pygame
from math import sqrt
pygame.init()

son_explosion = pygame.mixer.Sound('assets/son/explosion.ogg')
#son_explosion.set_volume(0.4)


class Ennemiv:
    def __init__(self, x, y, image, vel, imgmarchergauche, imgmarcherdroite, imgexplosion, exdgt, hp):
        """
        C'est une fonction qui définit/crée un ennemi qui explose quand le joueur est assez proche.
        
        Les parametres: x coordonnée de l'ennemi(x, int), y coordonnée de l'ennemi(y, int), image de l'ennemi(image, pygame.image.load()), la vélocite(vitesse de marche) de l'ennemi(vel, int), les images de l'animation pour marcher vers gauche(imgmarcher, list), les images de l'animation pour marcher vers droite(imgmarcherdroite, list), le point de vie d'ennemi(hp, int)
        """
        self.x = x
        self.y = y
        self.image = image
        self.imgexplosion = imgexplosion
        self.exdgt = exdgt
        self.vel = vel
        self.maxhp, self.hp = hp, hp
        self.width = 128
        self.height = 128
        self.droite = False
        self.gauche = True
        self.bg = False
        self.bd = False
        self.imgmarcherdroite = imgmarcherdroite
        self.imgmarchergauche = imgmarchergauche
        self.compteur = 0
        self.ecompteur = 0

    def deplacer(self, player):
        """
        C'est une fonction qui déplace l'ennemi vers le joueur.
        
        Elle prend la parametre joueur(joueur, la classe Player)
        """
        if self.hp > 0 and self.ecompteur == 0:
            if player.x + 100 > self.x + 64:
                self.x = self.x + self.vel
                self.droite = True
                self.gauche = False
                self.bg = False
                self.bd = True
                
            if player.x + 100 < self.x + 64:
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
        if self.bg and not self.ecompteur > 0:
            if self.compteur==24:
                self.compteur=0
            win.blit(self.imgmarchergauche[self.compteur//6], (self.x, self.y))
            self.compteur=self.compteur +1

			
        elif self.bd and not self.ecompteur > 0:
            if self.compteur==24:
                self.compteur=0
            win.blit(self.imgmarcherdroite[self.compteur//7], (self.x, self.y))
            self.compteur=self.compteur +1

        elif self.ecompteur > 0:
            #pygame.draw.circle(win, (255, 255, 255), (self.x + self.width//2, self.y + self.height//2), 164)
            win.blit(self.imgexplosion, (self.x - 61, self.y - 61))
        else:
            win.blit(self.image, (self.x, self.y))
        
        

    #pour faire baisser la vie du joueur
    def frappe(self, joueur, ebullets, ennemis):
        #si la distance entre le joueur et l'ennemi est inférireur à 200, l'ennemi explose en subissant de dégats
        if abs(joueur.x - self.x) < 150 or self.ecompteur > 0 or self.hp <= 0:
            if abs(joueur.x - self.x) < 200:
                joueur.hp = joueur.hp - self.exdgt
            for ennemi in ennemis:
                if ennemi != self:
                    if abs(ennemi.x - self.x) < 200:
                        ennemi.hp -= self.exdgt
            self.ecompteur += 1
            if self.ecompteur == 1:
                son_explosion.play()
        if self.ecompteur > 10:
            try:
                ennemis.remove(self)
            except:
                pass
            
  