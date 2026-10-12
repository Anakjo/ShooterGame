#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame
from Model.const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE, WIN_HEIGHT, WIN_WIDTH

#Abstract base class for all game entities (players, enemies, backgrounds, and shots)
class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        #Load the corresponding image asset based on the entity name
        self.surf = pygame.image.load('./Asset/' + name + '.png').convert_alpha()
        #Automatically resize background images to fit the screen dimensions
        if 'Level' in self.name:
            self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        #Initialize attributes mapped from configuration dictionaries
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        #Abstract method to be implemented by all subclasses for custom movement logic
        pass
