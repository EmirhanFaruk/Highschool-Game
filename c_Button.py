
# Modification date: Sat Apr  2 14:24:58 2022

# Production date: Sun Sep  3 15:42:59 2023

import pygame
pygame.init()

class Button:
    def __init__(self, x, y, w, h, texte, couleurtexte, grandeurtexte, couleur1, couleur2, task, image = ""):
        self.x, self.y, self.w, self.h, self.texte, self.couleurtexte, self.couleur1, self.couleur2, self.task= x, y, w, h, texte, couleurtexte, couleur1, couleur2, task
        if image != "":
            self.image = image

    def appuié(self, position_souris):
        #print(f"{position_souris[0]} > {self.x} and {position_souris[0]} < {self.x + self.w}")
        #print(f"{position_souris[1]} > {self.y} and {position_souris[1]} < {self.y + self.h}")
        if position_souris[0] > self.x and position_souris[0] < self.x + self.w:
            if position_souris[1] > self.y and position_souris[1] < self.y + self.h:
                return True
        return False
    
    def draw(self, win):
        if self.image != "":
            win.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(win, self.couleur, pygame.Rect(self.x, self.y, self.w, self.y)) 
            #afficher le texte sur le button
            font= pygame.font.SysFont('arial', self.grandeurtexte) #Sysfont:créez un objet Font à partir des polices système SysFont(name, size, bold=False, italic=False)
            score_texte=font.render(f"{self.texte}", 1, self.couleurtexte)
            win.blit(score_texte,self.coordonnées)