from Model.const import WIN_WIDTH
from Model.entity import Entity
from Model.enemy import Enemy
from Model.PlayerShot import PlayerShot
from Model.player import Player
from Model.EnemyShot import EnemyShot

#Mediator class responsible for managing game rules, window bounds, and entity collisions
class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        #Check if entities go out of screen boundaries and eliminate them by setting health to 0
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        #Validate authorized interaction pairs between different entity types
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        #If interaction is valid, check for bounding box overlap and apply damage/effects
        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and 
                ent1.rect.left <= ent2.rect.right and 
                ent1.rect.bottom >= ent2.rect.top and 
                ent1.rect.top <= ent2.rect.bottom):

                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        #Attribute points to the specific player who delivered the final blow to the enemy
        if enemy.last_dmg == 'PlayerSShot':
            for ent in entity_list:
                if ent.name == 'PlayerS':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'PlayerS2Shot':
            for ent in entity_list:
                if ent.name == 'PlayerS2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        #Iterate through all entities to check window boundaries and pairwise collisions
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        #Remove dead entities from the active list and reward scores if applicable
        for ent in entity_list[:]:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)