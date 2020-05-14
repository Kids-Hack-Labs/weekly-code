'''
    Circle Renderer Behaviour
'''
import pygame
from behaviour import Behaviour

class CircleRenderer(Behaviour):
    def __init__(self):
        self.radius = 25
        self.fill = (0, 225, 0)
        self.outline = (0, 200, 50)
        self.line_width = 3
        super().__init__()
    def update(self):
        pass
    def render(self):
        surf = pygame.display.get_surface()
        center = (self.game_object.x,
                  self.game_object.y)
        pygame.draw.circle(surf, self.fill, center, self.radius)
        pygame.draw.circle(surf, self.outline, center,
                           self.radius, self.line_width)
