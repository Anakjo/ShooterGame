#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random

from Model.entity import Entity
from Model.entityFactory import EntityFactory
from Model.const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, EVENT_TIMEOUT, TIMEOUT_LEVEL
from pygame import Surface, Rect
from pygame.font import Font
from Model.EntityMediator import EntityMediator
from Model.player import Player
from Model.enemy import Enemy

#Manages active gameplay levels, rendering, events, scores, and game loop execution
class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int], player_health: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.player_score = player_score
        self.player_health = player_health

        #Initialize entity list with background layers
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))

        #Instantiate Player 1 and load carried score/health states
        player = (EntityFactory.get_entity('PlayerS'))
        player.score = player_score[0]
        player.health = self.player_health[0]
        self.entity_list.append(player)

        #Instantiate Player 2 if game mode is cooperative (2 Players)
        if game_mode == MENU_OPTION[1]:
            player = (EntityFactory.get_entity('PlayerS2'))
            player.score = player_score[1]
            player.health = self.player_health[1]
            self.entity_list.append(player)

        #Set custom timers for enemy spawning and level countdown
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, 1000)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.window.fill((0, 0, 0))

            #Handle pygame events (window closure, enemy spawning, and level timeout)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 1000
                    #If level timer expires successfully, update scores/health and clear level
                    if self.timeout <= 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'PlayerS':
                                self.player_score[0] = ent.score
                                self.player_health[0] = ent.health
                            if isinstance(ent, Player) and ent.name == 'PlayerS2':
                                self.player_score[1] = ent.score
                                self.player_health[1] = ent.health
                        return True

            #Check if any player is still alive on screen
            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True

            #If all players are eliminated, end the level/game
            if not found_player:
                return False

            #Update and draw all active entities
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'PlayerS':
                    self.level_text(27, f'Player1 - Health: {ent.health} | Score: {ent.score}', (240, 248, 255), (10, 40))
                if ent.name == 'PlayerS2':
                    self.level_text(27, f'Player2 - Health: {ent.health} | Score: {ent.score}', (240, 248, 255), (10, 70))

            #Render UI overlays (Level  info, timer, FPS counter, entity count)
            self.level_text(30, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', (240, 248, 255), (10, 5))

            # Display special 'WAVE 2' banner at the top center during Level 2 for continuous gameplay feel
            if self.name == 'Level2':
                self.level_text(40, "WAVE 2", (255, 230, 0), (WIN_WIDTH / 2, 10))


            self.level_text(30, f'fps: {clock.get_fps():.0f}', (240, 248, 255), (10, WIN_HEIGHT - 70))
            self.level_text(30, f'entidades: {len(self.entity_list)}', (240, 248, 255), (10, WIN_HEIGHT - 35))

            pygame.display.flip()

            #Process entity collisions and health validation via EntityMediator
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            clock.tick(60)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        #Helper method to render custom HUD text on screen
        text_font: Font = pygame.font.SysFont(name="Agency FB", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)