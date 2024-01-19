
# Modification date: Mon Apr 25 20:38:28 2022

# Production date: Sun Sep  3 15:43:01 2023

import pygame
import os
from c_Player import *
from c_Ennemi import *
from c_Ennemid import *
from c_Ennemiv import *
from c_Ebullet import *
from c_Button import *
from c_Bullet import *
from c_Pickup import *
from rayene import *
#from PIL import Image
from random import choice, randint

path = os.getcwd()
pygame.init()


L=[]
# generer la fenetre de notre jeu
pygame.display.set_caption("ARMED")
#definir la longueur et la hauteur de la fenêtre
width, height = 1080, 720
#definir la fenêtre
win = pygame.display.set_mode((width, height))




#
#LES IMAGES
#

# importation des images commeune liste 
p = pygame.image.load(path + "\\assets\\player.png")#200x200
mummy_left = [pygame.image.load(path + "\\assets\\mummy\\mummy1.png"),#1
	pygame.image.load(path + "\\assets\\mummy\\mummy2.png"),#2
	pygame.image.load(path + "\\assets\\mummy\\mummy3.png"),#3
	pygame.image.load(path + "\\assets\\mummy\\mummy4.png"),#4
	pygame.image.load(path + "\\assets\\mummy\\mummy5.png"),#5
	pygame.image.load(path + "\\assets\\mummy\\mummy6.png"),#6
	pygame.image.load(path + "\\assets\\mummy\\mummy7.png"),#7
	pygame.image.load(path + "\\assets\\mummy\\mummy8.png"),#8
	pygame.image.load(path + "\\assets\\mummy\\mummy9.png"),#9
	pygame.image.load(path + "\\assets\\mummy\\mummy10.png"),#10
	pygame.image.load(path + "\\assets\\mummy\\mummy11.png"),#11
	pygame.image.load(path + "\\assets\\mummy\\mummy12.png"),#12
	pygame.image.load(path + "\\assets\\mummy\\mummy13.png"),#13
	pygame.image.load(path + "\\assets\\mummy\\mummy14.png"),#14
	pygame.image.load(path + "\\assets\\mummy\\mummy15.png"),#15
	pygame.image.load(path + "\\assets\\mummy\\mummy16.png"),#16
	pygame.image.load(path + "\\assets\\mummy\\mummy17.png"),#17
	pygame.image.load(path + "\\assets\\mummy\\mummy18.png"),#18
	pygame.image.load(path + "\\assets\\mummy\\mummy19.png"),#19
	pygame.image.load(path + "\\assets\\mummy\\mummy20.png"),#20
	pygame.image.load(path + "\\assets\\mummy\\mummy21.png"),#21
	pygame.image.load(path + "\\assets\\mummy\\mummy22.png"),#22
	pygame.image.load(path + "\\assets\\mummy\\mummy23.png"),#23
	pygame.image.load(path + "\\assets\\mummy\\mummy24.png")]#128x128  24
mummy_right = [pygame.image.load(path + "\\assets\\mummy.invers\\mummy1.png"),#1
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy2.png"),#2
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy3.png"),#3
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy4.png"),#4
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy5.png"),#5
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy6.png"),#6
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy7.png"),#7
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy8.png"),#8
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy9.png"),#9
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy10.png"),#10
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy11.png"),#11
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy12.png"),#12
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy13.png"),#13
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy14.png"),#14
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy15.png"),#15
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy16.png"),#16
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy17.png"),#17
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy18.png"),#18
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy19.png"),#19
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy20.png"),#20
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy21.png"),#21
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy22.png"),#22
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy23.png"),#23
	pygame.image.load(path + "\\assets\\mummy.invers\\mummy24.png")]#128x128  24
soinimg = pygame.image.load(path + "\\assets\\soinb.png")#64x64
pdimg = pygame.image.load(path + "\\assets\\plusdegatsb.png")#64x64
vbimg = pygame.image.load(path + "\\assets\\vitebulletsb.png")#64x64
vdimg = pygame.image.load(path + "\\assets\\vitedeplacementb.png")#64x64
background = pygame.image.load(path + "\\assets\\bg.jpg")
background = pygame.transform.scale(background, (width, height))
mr = pygame.image.load(path + "\\assets\\mummy.png")
"""
# pour changer les grandeur de les images de aliens
for c in range(1, 25):
    bltsimg = Image.open(path + "/assets/alien/alien" + str(c) +".png")
    bltsimg = bltsimg.resize((128, 128))
    bltsimg.save(path + "/assets/alienb/alien" + str(c) +".png")
"""
# pour les images de cartuches
bullet_img = [pygame.image.load(path + "\\assets\\bullet\\bullet01.png"), 
             pygame.image.load(path + "\\assets\\bullet\\bullet02.png"), 
             pygame.image.load(path + "\\assets\\bullet\\bullet03.png"), 
             pygame.image.load(path + "\\assets\\bullet\\bullet04.png"), 
             pygame.image.load(path + "\\assets\\bullet\\bullet05.png"), 
             pygame.image.load(path + "\\assets\\bullet\\bullet06.png"), 
             pygame.image.load(path + "\\assets\\bullet\\bullet07.png"), 
             pygame.image.load(path + "\\assets\\bullet\\bullet08.png")]
# les alien que tire de loin
alien_img = [pygame.image.load(path + "\\assets\\alienb\\alien1.png"),#1
	pygame.image.load(path + "\\assets\\alienb\\alien2.png"),#2
	pygame.image.load(path + "\\assets\\alienb\\alien3.png"),#3
	pygame.image.load(path + "\\assets\\alienb\\alien4.png"),#4
	pygame.image.load(path + "\\assets\\alienb\\alien5.png"),#5
	pygame.image.load(path + "\\assets\\alienb\\alien6.png"),#6
	pygame.image.load(path + "\\assets\\alienb\\alien7.png"),#7
	pygame.image.load(path + "\\assets\\alienb\\alien8.png"),#8
	pygame.image.load(path + "\\assets\\alienb\\alien9.png"),#9
	pygame.image.load(path + "\\assets\\alienb\\alien10.png"),#10
	pygame.image.load(path + "\\assets\\alienb\\alien11.png"),#11
	pygame.image.load(path + "\\assets\\alienb\\alien12.png"),#12
	pygame.image.load(path + "\\assets\\alienb\\alien13.png"),#13
	pygame.image.load(path + "\\assets\\alienb\\alien14.png"),#14
	pygame.image.load(path + "\\assets\\alienb\\alien15.png"),#15
	pygame.image.load(path + "\\assets\\alienb\\alien16.png"),#16
	pygame.image.load(path + "\\assets\\alienb\\alien17.png"),#17
	pygame.image.load(path + "\\assets\\alienb\\alien18.png"),#18
	pygame.image.load(path + "\\assets\\alienb\\alien19.png"),#19
	pygame.image.load(path + "\\assets\\alienb\\alien20.png"),#20
	pygame.image.load(path + "\\assets\\alienb\\alien21.png"),#21
	pygame.image.load(path + "\\assets\\alienb\\alien22.png"),#22
	pygame.image.load(path + "\\assets\\alienb\\alien23.png"),#23
	pygame.image.load(path + "\\assets\\alienb\\alien24.png")]
aimg = pygame.image.load(path + "\\assets\\alienb.png")

# l'ennemi qui explose
ennemivd = [pygame.image.load(path + "\\assets\\ennemivd\\ennemiv1.png"),#1
	pygame.image.load(path + "\\assets\\ennemivd\\ennemiv2.png"),#2
	pygame.image.load(path + "\\assets\\ennemivd\\ennemiv3.png"),#3
	pygame.image.load(path + "\\assets\\ennemivd\\ennemiv4.png")]

ennemivg = [pygame.image.load(path + "\\assets\\ennemivg\\ennemiv1.png"),#1
	pygame.image.load(path + "\\assets\\ennemivg\\ennemiv2.png"),#2
	pygame.image.load(path + "\\assets\\ennemivg\\ennemiv3.png"),#3
	pygame.image.load(path + "\\assets\\ennemivg\\ennemiv4.png")]

ennemiv = pygame.image.load(path + "\\assets\\EXP2b.png")


#
#LES SONS
#

son_tir1 = pygame.mixer.Sound('assets\\son\\fireball.wav')
son_tir1.set_volume(1.2)
#son_tir2 = pygame.mixer.Sound('assets\\son\\tir.ogg')





playbtnimg = pygame.image.load(path + "\\assets\\dhn2.png")
playbtnimg = pygame.transform.scale(playbtnimg, (250, 250))
button = pygame.image.load(path + "\\dhn4.png")
button = pygame.transform.scale(button, (250,250))
#button def __init__(self, x, y, w, h, texte, couleurtexte, grandeurtexte, couleur1, couleur2, task, image = "")
#picture = pygame.transform.scale(picture, (1280, 720))
play_button = Button(540-125, 400, 250, 250, "", "", "", "", "", "jouer", playbtnimg)

#ply_again_img = pygame.image.load(path + "/dhn4.png")
#ply_again_img = pygame.transform.scale(ply_again_img, (250, 250))
replay_button = Button(width//2 - 125, 250, 250, 250, "", "", "", "", "", "rejouer", button)
#banner

logo = pygame.image.load(path + "\\assets\\logo.png")
logo = pygame.transform.scale(logo, (700, 500))


#Player
player = Player(width//2 - 100,height - 275, p, 100, 50)
"""
#Ennemis
ennemi = Ennemi(-128, height - 235, mr, 2, mummy_left, mummy_right, 300)

alien = Ennemid(0, height - 235, aimg, 2, alien_img, 300)

#Pickup
#pickup = Pickup(pdimg, width, height, 150, 150, 10, "plus degats")
"""


#Les listes
ennemis = []
bullets = []
ebullets = []
pickups = []

#apparition des ennemis
def créer_des_ennemis(ennemis, compteur, vagues, pickups):
    can_spawn = int(vagues * 1.5)
    if compteur > 600 or len(ennemis) == 0:
        compteur= 0
        vagues += 1
        while can_spawn > 0:
            if randint(0, 1) == 1:#gauche
                if vagues > 4:
                    #1-50 = mummy, 51-80 = alien, 81-90 = ennemiv
                    da_ennemi = randint(1, 100)
                    if da_ennemi <= 50:
                        xde = randint(-300,-128)
                        ennemis.append(Ennemi(xde, height - 235, mr, 2, mummy_left, mummy_right, 300 + vagues * 20))
                    elif da_ennemi <= 80:
                        xde = randint(-256,-128)
                        ennemis.append(Ennemid(xde, height - 235, aimg, 1, alien_img, 200 + vagues * 10))
                    else:
                        xde = randint(-512,-196)
                        ennemis.append(Ennemiv(xde, height - 300, ennemiv, 6, ennemivg, ennemivd, ennemiv, 1 + vagues, 100 + vagues * 5))
                        #ennemis.append(choice([Ennemi(xde, height - 235, mr, 2, mummy_left, mummy_right, 300), Ennemid(xde, height - 235, aimg, 2, alien_img, 200), Ennemiv(xde, height - 300, ennemiv, 6, ennemivg, ennemivd, ennemiv, 100)]))
                elif vagues > 2:
                    da_ennemi = randint(1, 80)
                    if da_ennemi <= 50:
                        xde = randint(-300,-128)
                        ennemis.append(Ennemi(xde, height - 235, mr, 2, mummy_left, mummy_right, 300 + vagues * 20))
                    elif da_ennemi <= 80:
                        xde = randint(-256,-128)
                        ennemis.append(Ennemid(xde, height - 235, aimg, 1, alien_img, 200 + vagues * 10))
                else:
                    xde = randint(-300,-128)
                    ennemis.append(Ennemi(xde, height - 235, mr, 2, mummy_left, mummy_right, 300))
            else:
                if vagues > 4:
                    #1-50 = mummy, 51-80 = alien, 81-90 = ennemiv
                    da_ennemi = randint(1, 100)
                    if da_ennemi <= 50:
                        xde = randint(1080, 1252)
                        ennemis.append(Ennemi(xde, height - 235, mr, 2, mummy_left, mummy_right, 300 + vagues * 20))
                    elif da_ennemi <= 80:
                        xde = randint(1080, 1208)
                        ennemis.append(Ennemid(xde, height - 235, aimg, 1, alien_img, 200 + vagues * 10))
                    else:
                        xde = randint(1144, 1396)
                        ennemis.append(Ennemiv(xde, height - 300, ennemiv, 6, ennemivg, ennemivd, ennemiv , 1 + vagues, 100 + vagues * 5))
                        #ennemis.append(choice([Ennemi(xde, height - 235, mr, 2, mummy_left, mummy_right, 300), Ennemid(xde, height - 235, aimg, 2, alien_img, 200), Ennemiv(xde, height - 300, ennemiv, 6, ennemivg, ennemivd, ennemiv, 100)]))
                elif vagues > 2:
                    da_ennemi = randint(1, 80)
                    if da_ennemi <= 50:
                        xde = xde = randint(1080, 1252)
                        ennemis.append(Ennemi(xde, height - 235, mr, 2, mummy_left, mummy_right, 300 + vagues * 20))
                    elif da_ennemi <= 80:
                        xde = randint(1080, 1208)
                        ennemis.append(Ennemid(xde, height - 235, aimg, 1, alien_img, 200 + vagues * 10))
                else:
                    xde = xde = randint(1080, 1252)
                    ennemis.append(Ennemi(xde, height - 235, mr, 2, mummy_left, mummy_right, 300))
                #xde = randint(1080,1252)
                #ennemis.append(choice([Ennemi(xde, height - 235, mr, 2, mummy_left, mummy_right, 300), Ennemid(xde, height - 235, aimg, 2, alien_img, 200), Ennemiv(xde, height - 300, ennemiv, 6, ennemivg, ennemivd, ennemiv, 100)]))
            can_spawn -= 1
        pickups.append(choice([Pickup(soinimg, width, height, 64, 64, 5, "soigner"), Pickup(pdimg, width, height, 64, 64, 5, "plus dégats"), Pickup(vbimg, width, height, 64, 64, 5, "vite bullets"), Pickup(vdimg, width, height, 64, 64, 5, "vite deplacement")]))
    else:
        compteur=compteur+1
    
    return compteur, vagues, pickups

#Les Textes
texte_de_score = Texte((20, 20), (0, 0, 0), "Score:", 30, 0)
texte_de_temps = Texte((800, 20), (0, 0, 0), "temps:", 30, 0)
texte_game_over = Texte((190,50),(250,0,0),"GAME OVER",100, "")
texte_de_niveau = Texte((400, 20), (0, 0, 0), "niveau:", 30, 0 )
texte_de_meilleur_score = Texte((255, 160), (0, 0, 0), "BRAVO RECORD BATTU !", 30, "" )





font = pygame.font.SysFont("Arial", 18)




compteur_de_temps = 0
compteur, vagues = 0, 0
fps_set = 30
clock = pygame.time.Clock() 
running = True
# boucle tant que cette condition est vrai
menu_principale = True
en_jeu = False
while running:
    #if pickups:
        #print(pickups, pickups[0].x, pickups[0].y)
    if menu_principale:#menu principale
        #dessiner le plan arrière
        win.blit(background,(0,0))
        #win.fill((238, 130, 238))
        clock.tick(fps_set)
        # si le jouer ferme cette fenetre
        for event in pygame.event.get():
            # que l'evenement est fermeture de fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                #print("fermeture de jeu")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                clicked = play_button.appuié((mx, my))
                if clicked:
                    menu_principale = False
                    en_jeu = True
                    ennemis = []
                    pickups = []
                    bullets = []
                    ebullet = []
                    player = Player(width//2,height - 275, p, 100, 50)
                    compteur_de_temps = 0
                    compteur, vagues = 0, 0
                    texte_de_score.score = 0
                    
        
        play_button.draw(win)
        win.blit(logo, (150, 10))
        #pygame.display.update()
    elif en_jeu:#le jeu
        #dessiner le plan arrière
        win.blit(background,(0,0))
        #win.fill((238, 130, 238))
        clock.tick(fps_set)
        # si le jouer ferme cette fenetre
    
        for event in pygame.event.get():
            # que l'evenement est fermeture de fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
                #print("fermeture de jeu")
            if event.type == pygame.KEYUP and player.hp > 0:
                #print("Je n'appui plus sur un button!")
                if event.key == pygame.K_LEFT:
                    #print("Je n'appui plus sur la fleche gauche")
                    player.moving_left = False
                    continue
                if event.key == pygame.K_RIGHT:
                    #print("Je n'appui plus  sur la fleche droite")
                    player.moving_right= False
                    continue
                if event.key == pygame.K_SPACE:
                    player.tire = False
                
            if event.type == pygame.KEYDOWN and player.hp > 0:
                #print("J'appui sur un button!")
                if event.key == pygame.K_LEFT:
                    #print("J'appui sur la fleche gauche")
                    player.moving_left = True
                    continue
                if event.key == pygame.K_RIGHT:
                    #print("J'appui sur la fleche droite")
                    player.moving_right= True
                    continue
                if event.key == pygame.K_SPACE:
                    player.tire = True
                    #son_tir2.play()
                    continue
                if not(player.is_jumping):
                    if event.key == pygame.K_UP:
                        player.is_jumping = True
                        player.y_vel += 9

            if event.type == pygame.MOUSEBUTTONDOWN and player.hp <= 0:
                mx, my = event.pos
                clicked = replay_button.appuié((mx, my))
                if clicked:
                    menu_principale = True
                    en_jeu = False
                    ennemis = []
                    pickups = []
                    bullets = []
                    ebullet = []
                    player = Player(width//2,height - 275, p, 100, 50)
                    compteur_de_temps = 0
                    compteur, vagues = 0, 0
                    texte_de_score.score = 0
                    
                            
    
        #si les point de vie de joueur est 0 ou moins
        if player.hp <= 0:
            replay_button.draw(win)
            player.moving_right = False
            player.moving_left = False
            player.left = False
            player.right = False
            player.tire = False

            texte_game_over.update(win) #afichage de game over
            ms_l = open("meilleure_score.txt", "r") #ouverture du fichier
            ms = int(ms_l.readlines()[0])#recuperer le meilleure score
            ms_l.close() #fermiture le fichier
            #print(ms)
            if ms <= texte_de_score.score: #verifier si le score est > ai meilleure score 
                meil_s = texte_de_score.score #on définit le meilleure score
                texte_de_meilleur_score.texte = "Bravo! Nouveau record: "#modifier le texte car on a battu le record
                
            else:
                meil_s = ms #definir le record
                texte_de_meilleur_score.texte = "             record: "#modifier le texte car on a pas battu le record
            ms_l = open("meilleure_score.txt", "w") #ouvrir le fichier
            ms_l.write(str(meil_s)) #sauvgarder le score
            ms_l.close()
            texte_de_meilleur_score.score = meil_s #on medifier le texte de meilleur score
            texte_de_meilleur_score.update(win) #affichage
            



            
        try:
            compteur, vagues, pickups = créer_des_ennemis(ennemis, compteur, vagues, pickups)
        except:
            print("passing niveaux")
            pass
    
        # le saut
        #print(player.y, player.y_vel, player.is_jumping)
        if player.is_jumping:
            if player.y - player.y_vel > 445:
                player.is_jumping = False
                player.y_vel = 0
                player.y = 445
            elif player.y <=  445.0:
                player.y_vel -= 0.5
            else:
                player.is_jumping = False
                player.y_vel = 0
                player.y = 445

            """
            if player.jump_count >= -7:
                neg = 1
                if player.jump_count < 0:
                    neg = -1
                player.y -= (player.jump_count ** 2) * 0.5 * neg
                player.jump_count -= 1
            else:
                player.is_jumping = False
                player.jump_count = 7
            """
    
    
        
    
        if player:
            player.y -= player.y_vel
            if player.tire:
                if player.tire_count >= 2:
                    if player.left:
                        bulvel = -player.bulvel
                    else:
                        bulvel = player.bulvel
                    bullets.append(Bullet(player.x + 100, player.y + 84, bulvel, bullet_img))
                    son_tir1.play()
                    player.tire_count = 0
                else:
                    player.tire_count += 1
            player.deplacer()
            player.draw(win)
        #l'affichage et deplacement des bullets
        for bullet in bullets:
            bullet.deplacer(ennemis, bullets)
            bullet.draw(win)
        for ebullet in ebullets:
            ebullet.deplacer(player, ebullets)
            ebullet.draw(win)
        #print(player.hp)
        for ennemi in ennemis:
            if ennemi.hp <= 0:
                try:
                    ennemis.remove(ennemi)
                    texte_de_score.score += 1
                except:
                    pass
                
            ennemi.frappe(player, ebullets, ennemis)
            ennemi.deplacer(player)
            ennemi.draw(win, player)
        for pickup in pickups:
            try:
                est_touché = pickup.touché(player)
                pickup.deplacer(pickups)
                pickup.draw(win)
                if est_touché:
                    #print(f"picked up {pickup.abilité}")
                    pickups.remove(pickup)
            except:
                pass
            
    
            
        texte_de_score.update(win)  #affichage de score
        if player.hp>0:
            compteur_de_temps += 1
        
            
            
        
        texte_de_niveau.score = vagues
        texte_de_temps.score=compteur_de_temps//fps_set
        texte_de_temps.update(win) #affichage de temps

        texte_de_niveau.update(win)
        #meilleure_score.txt = open("data.txt", "w")
        
            
        #play_button.draw(win)
        #pygame.display.update()


    
    #fps
    fps = int(clock.get_fps())
    fps_text = font.render(str(fps), 1, pygame.Color("coral"))
    win.blit(fps_text, (10,10))
    pygame.display.update()
