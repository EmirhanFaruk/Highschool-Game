
# Modification date: Sun Apr  3 18:06:08 2022

# Production date: Sun Sep  3 15:42:59 2023

import pygame
import os
pygame.init()
path = os.getcwd()




class Player:
    def __init__(self, x, y, image, maxhp, degat):
        """
        C'est une fonction qui définit le joueuret ses attributs.

        Les parametres: x coordonnée de joueur(x, int), y coordonnée de joueur(y, int), image de joueur(image, pygame.image.load()), maximum point de vie de joueur(maxhp, int), degat d'un balle(bullet) de joueur(degat, int)
        """
        self.x = x
        self.y = y
        self.image = image
        self.moving_right = False
        self.moving_left= False
        self.vel = 5
        self.up = False
        self.left = False
        self.right = True
        self.maxhp, self.hp = maxhp, maxhp
        self.degat = degat
        self.tire = False
        self.tire_count = 0
        self.bulvel = 10
        #self.jump_count = 7
        self.y_vel = 0
        self.is_jumping = False


    def deplacer(self):
        """
        C'est une fonction qui déplace et limite le mouvement du joueur dans l'écran.
        """
        if self.moving_right and self.x < 1080-200:
            self.x=self.x + self.vel
            self.right = True
            self.left = False

        if self.moving_left and self.x > 0:
            self.x=self.x -self.vel
            self.left = True
            self.right = False
        if self.up:
            self.y += 5
        return
    # dessiner le joueur sur l'ecran
    def draw(self, win):
        """
        Cette fonction sert à afficher le joueur, la barre de vie du joueur et à changer la couleur de la barre en fonction de ses points de vie.
        """
        #pour modifier la couleur de la barre de vie au fur et à mesure lorsqu'il perd de la vie
        couleur = (0,255,0) 
        if self.hp < 50: #quand la vie du joueur est à moins de 50, la couleur de la barre de vie devient orange
            couleur = (255,125,0)
        if self.hp< 30:#quand la vie du joueur est à moins de 20, la couleur de la barre de vie deveint rouge
            couleur = (255,0,0)
        blanc = (255,255,255) 
      #emplacement, taille et couleur de la barre de vie 
        pygame.draw.rect(win, blanc, pygame.Rect(self.x + 49, self.y - 1, 102, 12)) 
        pygame.draw.rect(win, couleur, pygame.Rect(self.x + 50, self.y, self.hp, 10))
        
        
        
        win.blit(self.image, (self.x, self.y))
        
      