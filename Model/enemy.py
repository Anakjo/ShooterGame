#!/usr/bin/python
# -*- coding: utf-8 -*-

from Model.entity import Entity
from Model.const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from Model.EnemyShot import EnemyShot

#Handles enemy movement patterns and attack/shooting cooldown mechanics
class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        #Move the enemy horizontally across the screen from right to left
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        #Decrease shooting cooldown timer on each frame update
        self.shot_delay -= 1
        #When cooldown reaches zero, fire a projectile and reset the delay timer
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))