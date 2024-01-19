
# Modification date: Fri Apr  1 16:07:22 2022

# Production date: Sun Sep  3 15:43:01 2023

import pygame
pygame.init()


#les coordonnées, la couleur, le texte, la grandeur de la texte, le score(si on va pas l'utiliser ça doit être 0 automatiquement)
class Texte:
  def __init__(self, coordonnées,couleur,texte,grandeur,score):
    #mettre le score a 0
    self.score=score
    self.coordonnées = coordonnées
    self.couleur =couleur
    self.texte=texte
    self.grandeur =grandeur
    
  def update(self, screen):
    #afficher le score dans l'écran
    font= pygame.font.SysFont('arial',self.grandeur) #Sysfont:créez un objet Font à partir des polices système SysFont(name, size, bold=False, italic=False)
    score_texte=font.render(f"{self.texte} {self.score}" ,1,self.couleur)
    screen.blit(score_texte,self.coordonnées)



#https://www.freelogoservices.com/fr/diy-logo-upsells?lid=881321680




    
