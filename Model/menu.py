#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from Model.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION

class Menu:
    #background png image and music
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Asset/menu.png').convert()
        self.rect = self.surf.get_rect(left=0, top=0)

        pygame.mixer_music.load('./Asset/Menu.mp3')
        pygame.mixer_music.play(-1)

    def run(self):
        #events
        #game runs and don't close by itself
        menu_option = 0
        run_menu = True
        while run_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #down key
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: #up key
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #enter
                        return MENU_OPTION[menu_option]

                
            self.window.blit(source=self.surf, dest=self.rect)

            #title
            self.menu_text(100, "Cosmic", (240, 248, 255), ((WIN_WIDTH / 2), 70))
            self.menu_text(100, "Void", (240, 248, 255), ((WIN_WIDTH / 2), 160))

            #colors of the menu selection options
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], (255, 230, 0), ((WIN_WIDTH / 2), 300 + 50 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i], (240, 248, 255), ((WIN_WIDTH / 2), 300 + 50 * i))

            pygame.display.flip()

    #function to create the title image
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Agency FB", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)