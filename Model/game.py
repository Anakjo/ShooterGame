#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from Model.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from Model.level import Level
from Model.menu import Menu
from Model.Score import Score

#Main game controller class that manages application state flow, screens, and window execution
class Game:
    def __init__(self):
        pygame.init()
        #Initialize the main game display window using dimensions from constants
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        #Main game loop handling screen transitions and states
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            #Handle game start options (1 Player or 2 Players)
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                player_score = [0, 0] #Score tracking for Player 1 and Player 2
                player_health = [300, 300] #Initial health pool for players

                pygame.mixer_music.load('./Asset/Level.ogg')
                pygame.mixer_music.play(-1)

                #Run Level 1
                level1 = Level(self.window, 'Level1', menu_return, player_score, player_health)
                level1_return = level1.run()

                #If Level 1 is cleared, proceed to Level 2
                if level1_return:
                    level2 = Level(self.window, 'Level2', menu_return, player_score, player_health)
                    level2_return = level2.run()

                    #If Level 2 is completed, save the final score to the database
                    if level2_return:
                        score.save(menu_return, player_score)

            #Open the high score leaderboard screen
            elif menu_return == MENU_OPTION[2]:
                score = Score(self.window)
                score.show()

            #Exit and terminate the game application
            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                exit()
            else:
                pass