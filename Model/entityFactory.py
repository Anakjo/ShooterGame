#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from Model.background import Background
from Model.const import WIN_WIDTH, WIN_HEIGHT
from Model.player import Player
from Model.enemy import Enemy

class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(1, 4):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(1, 4):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            
            case 'PlayerS':
                return Player('PlayerS', (10, WIN_HEIGHT / 2 - 30))
            case 'PlayerS2':
                return Player('PlayerS2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40)))