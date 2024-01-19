
# Modification date: Sun Apr  3 15:52:54 2022

# Production date: Sun Sep  3 15:42:59 2023

import pygame
from random import randint
from math import sqrt
pygame.init()




class Pickup:
    def __init__(self, image, mw, mh, width, height, vel, abilité):
        """
        C'est une fonction qui crée un pickup(qui aide le joueur).
        Les parametres: image de pickup(image - pygame.image.load()), la longueur(mw - int) et la hauteur de la carte(mh - int), la longueur(width - int) et la hauteur de la pickup(height - int), la vitesse de la pickup pendant il tombe du ciel(vel - int/float), abilité(abilité - str)
        """
        self.image = image
        self.width, self.height = width, height
        self.x = randint(0, mw - width)
        self.y = -height
        self.limite = mh - 184#le pickup va s'arreter à cet y.
        self.vel = vel
        self.abilité = abilité
        #self.les_abilités = ["soinger", "plus dégats"]


    def distance(self, joueur):
        """
        C'est une fonction qui retour la calcule de la distance entre le pickup et le joueur.

        Elle prend la parametre joueur(joueur, la classe Player)
        """
        return sqrt(((self.x + self.width//2) - (joueur.x + 100))**2 + ((self.y + self.height//2) - (joueur.y + 100))**2)
        
    def touché(self, joueur):
        """
        C'est une fonction qui donne 'l'abilité' au joueur s'il est assez proche, et qui retour True, pour qu'il soit effacé.

        Elle prend la parametre joueur(joueur, la classe Player)
        """
        if (abs(joueur.x + 150 - self.x) < 128 or abs(joueur.x - self.x + self.width) < 128) and (abs(joueur.y - self.y + self.height) < 128):
            #print(abs(joueur.x + 150 - self.x), abs(joueur.x - self.x + self.width))
            if self.abilité == "soigner":
                joueur.hp = joueur.maxhp
                #print("je l'ai eu!")
            elif self.abilité == "plus dégats":
                joueur.degat += 25
            elif self.abilité == "vite bullets":
                joueur.bulvel += 10
            elif self.abilité == "vite deplacement":
                joueur.vel += 5
            return True
    
    def deplacer(self, pickups):
        #print(self.x, self.y)
        """
        C'est une fonction qui déplace le pickup vers le bas jusqu'à la terre.
        """
        #print(self.y, self.limite)
        if self.y < 720:
            self.y += self.vel
            #print("je tombe!")
        else:
            #print("self removing protocole activated")
            pickups.remove(self)
    # dessiner le pickup sur l'ecran
    def draw(self, win):
        """
        C'est une fonction qui affiche le pickupdans l'écran.

        Elle prend le parametre la fenêtre du jeu(win, pygame.display.set_mode())
        """
        win.blit(self.image, (self.x, self.y))