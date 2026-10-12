from Model.entity import Entity
from Model.const import ENTITY_SPEED

#Manages player projectile behavior and forward movement trajectory
class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        #Move the player projectile horizontally from left to right across the screen
        self.rect.centerx += ENTITY_SPEED[self.name]