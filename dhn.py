
# Modification date: Fri Apr  1 16:07:22 2022

# Production date: Sun Sep  3 15:42:59 2023


couleur = (255,0,0) 
pygame.draw.rect(win, couleur, pygame.Rect(self.x + 50, self.y, self.hp, 10)) #déterminer l'emplacement et la taille du rectangle 
 blanc = (255,255,255) 
pygame.draw.rect(win, blanc, pygame.Rect(self.x + 49, self.y - 1, 102, 10))  #emplacement, taille et couleur(blanche) du contour du rectangle

 #pour faire baisser la vie du joueur
def frappe(self, joueur):
  if self.distance(joueur) < 100:
    joueur.hp=joueur.hp-1


if self.hp < 50:#quand la vie du joueur est à moins de 50, la couleur de la barre de vie devient orange
  couleur = (255,125,0)
if self.hp < 20:#quand la vie du joueur est à moins de 20, la couleur de la barre de vie deveint rouge
  couleur = (255,0,0)

button = pygame.image.load(path + "/dhn4.png")
button = pygame.transform.scale(button, (250,250))