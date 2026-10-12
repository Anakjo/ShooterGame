#!/usr/bin/python
# -*- coding: utf-8 -*-

from Model.entity import Entity
from Model.const import WIN_WIDTH, ENTITY_SPEED

#Handles background layers and infinite scrolling mechanics
class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        #Move the background to the left based on its configured speed
        self.rect.centerx -= ENTITY_SPEED[self.name]

        #Reset background position to the right side of the screen for infinite scrolling loop
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
