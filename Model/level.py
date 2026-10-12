#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random

from Model.entity import Entity
from Model.entityFactory import EntityFactory
from Model.const import WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from pygame import Surface, Rect
from pygame.font import Font
from Model.EntityMediator import EntityMediator
from Model.player import Player
from Model.enemy import Enemy

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('PlayerS'))
        if game_mode == MENU_OPTION[1]:
            self.entity_list.append(EntityFactory.get_entity('PlayerS2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)


        self.timeout = 20000

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
    
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

            # printed text
            self.level_text(30, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', (240, 248, 255), (10, 5))
            # fps print 
            self.level_text(30, f'fps: {clock.get_fps():.0f}', (240, 248, 255), (10, WIN_HEIGHT - 70))
                
            self.level_text(30, f'entidades: {len(self.entity_list)}', (240, 248, 255), (10, WIN_HEIGHT - 35))
            pygame.display.flip()

            #collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            clock.tick(60)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Agency FB", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)