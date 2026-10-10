#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Asset/menu.png').convert()
        self.rect = self.surf.get_rect(left=0, top=0)

        pygame.mixer_music.load('./Asset/Menu.mp3')
        pygame.mixer_music.play(-1)

    def run(self):
        roda_menu = True
        while roda_menu:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

