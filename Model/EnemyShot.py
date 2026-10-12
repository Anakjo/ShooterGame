from Model.entity import Entity
from Model.const import ENTITY_SPEED

#Manages enemy projectile behavior and movement trajector
class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        #Move the enemy projectile horizontally from right to left across the screen
        self.rect.centerx -= ENTITY_SPEED[self.name]