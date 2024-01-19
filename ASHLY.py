
# Modification date: Fri Apr  1 16:07:22 2022

# Production date: Sun Sep  3 15:42:59 2023

import pygame
import os
path = os.getcwd()
pygame.init()
L=[]
# generer la fenetre de notre jeu
pygame.display.set_caption("ARMED")
#definir la longueur et la hauteur de la fenêtre
width, height = 1080, 720
#definir la fenêtre
win = pygame.display.set_mode((width, height))
image = pygame.image.load(path + "/Mon_projet.png")
image = pygame.transform.scale(image, (700, 500))

button = pygame.image.load(path + "/NSI-ARMED.png")
button = pygame.transform.scale(button, (250,250))

background = pygame.image.load(path + "/bg.png")
background = pygame.transform.scale(background, (width, height))

fps = 30
clock = pygame.time.Clock() 
running = True
# boucle tant que cette condition est vrai
while running:
	win.blit(background, (0, 0))
	win.blit(button, (400,400))
	win.blit(image, (150, 10))
	pygame.display.update()
    
    
