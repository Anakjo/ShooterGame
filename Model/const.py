import pygame

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg1': 0,
    'Level1Bg2': 1,
    'Level1Bg3': 3,
    'PlayerS': 5,
    'PlayerSShot': 4,
    'PlayerS2': 5,
    'PlayerS2Shot': 4,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 3
}

ENTITY_HEALTH = {
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'PlayerS': 300,
    'PlayerSShot': 1,
    'PlayerS2': 300,
    'PlayerS2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1
}

ENTITY_SHOT_DELAY = {
    'PlayerS': 20,
    'PlayerS2': 15,
    'Enemy1': 100,
    'Enemy2': 150
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
PLAYER_KEY_SHOOT = {'PlayerS': pygame.K_SPACE,
                 'PlayerS2': pygame.K_LCTRL}

#S
SPAWN_TIME = 4000

#W
WIN_WIDTH = 1024
WIN_HEIGHT = 600