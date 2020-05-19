'''
    Movement Class file
    Pygame "engine"
    Designed to test different effects
'''
import pygame
import pygame.math as p_math
import math
from engine.behaviour import Behaviour

class Movement(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "Movement"
        self.forward_speed = 1
        self.movement_info = [0,0]
        
    def update(self):
        key_list = pygame.key.get_pressed()

        w = key_list[pygame.K_w]
        a = key_list[pygame.K_a]
        s = key_list[pygame.K_s]
        d = key_list[pygame.K_d]

        self.movement_info = [0,0]

        if w:
            self.movement_info[1] -= 1
        if a:
            self.movement_info[0] -= 1
        if s:
            self.movement_info[1] += 1
        if d:
            self.movement_info[0] += 1

        self.game_object.get_behaviour('Transform').translate(self.movement_info) 
        
    def render(self):
        pass
        
