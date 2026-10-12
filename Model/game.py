#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from Model.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from Model.level import Level
from Model.menu import Menu
from Model.Score import Score

#runs the game based on the width and height of the const.py
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                player_score = [0, 0]#Player1, Player2
                player_health = [300, 300]

                level1 = Level(self.window, 'Level1', menu_return, player_score, player_health)
                level1_return = level1.run()
                if level1_return:
                    level2 = Level(self.window, 'Level2', menu_return, player_score, player_health)
                    level2_return = level2.run()
                    if level2_return:
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[2]:
                score = Score(self.window)
                score.show()

            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                exit()
            else:
                pass