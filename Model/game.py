#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from Model.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from Model.level import Level
from Model.menu import Menu

#runs the game based on the width and height of the const.py
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                level = Level(self.window, 'Level-1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                exit()
            else:
                pass