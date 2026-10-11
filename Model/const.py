import pygame

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg1': 0,
    'Level1Bg2': 1,
    'Level1Bg3': 3,
    'PlayerS': 5,
    'PlayerS2': 5,
    'Enemy1': 3,
    'Enemy2': 3
}


#M
MENU_OPTION = ('NEW GAME--1 PLAYER',
               'NEW GAME--2 PLAYERS',
               'SCORE',
               'EXIT')


#P
PLAYER_KEY_UP = {'PlayerS': pygame.K_UP,
                 'PlayerS2': pygame.K_w}
PLAYER_KEY_DOWN = {'PlayerS': pygame.K_DOWN,
                 'PlayerS2': pygame.K_s}
PLAYER_KEY_LEFT = {'PlayerS': pygame.K_LEFT,
                 'PlayerS2': pygame.K_a}
PLAYER_KEY_RIGHT = {'PlayerS': pygame.K_RIGHT,
                 'PlayerS2': pygame.K_d}
PLAYER_KEY_SHOOT = {'PlayerS': pygame.K_RCTRL,
                 'PlayerS2': pygame.K_LCTRL}

#S
SPAWN_TIME = 4000

#W
WIN_WIDTH = 1024
WIN_HEIGHT = 600