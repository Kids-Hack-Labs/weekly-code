'''
    Movement Behaviour
    (for obstacles)
'''
import pygame
from behaviour import Behaviour

class Movement(Behaviour):
    def __init__(self):
        self.speed = 1
        super().__init__()

    def update(self):
        self.game_object.y += self.speed
        surf = pygame.display.get_surface()
        if (self.game_object.y >= surf.get_height()
            or self.game_object.y < 0):
            self.speed *= -1
    def render(self):
        pass
