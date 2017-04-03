#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1920, 1080), HWSURFACE | DOUBLEBUF | RESIZABLE)

# Chargement et collage du fond
fond = pygame.image.load("Img/Fond.png").convert()
fond = pygame.transform.scale(fond, (1920, 1080))
fenetre.blit(pygame.transform.scale(fond, (1920, 1080)), (0, 0))

# Rafraîchissement de l'écran
pygame.display.flip()

# BOUCLE INFINIE
continuer = 1
while continuer:

    # boucle detection evenement
    for event in pygame.event.get():
        # evenement croix fenetre
        if event.type == QUIT:
            continuer = 0
        # evenement resize
        elif event.type == VIDEORESIZE:
        fenetre = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        fenetre.blit(pygame.transform.scale(fond, event.dict['size']), (0, 0))

    # rafraichissement final
    pygame.display.flip()
