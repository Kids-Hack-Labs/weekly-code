'''
    Square Renderer class
'''
import pygame
from behaviour import Behaviour

class SquareRenderer(Behaviour):
    def __init__(self):
        self.width = 50
        self.height = 75
        self.fill = (90, 90, 0)
        self.outline = (90, 0, 100)
        self.line_width = 7
        super().__init__()
    def update(self):
        pass
    def render(self):
        surf = pygame.display.get_surface()
        render_rect = pygame.Rect(self.game_object.x,
                                 self.game_object.y,
                                 self.width, self.height)
        pygame.draw.rect(surf, self.fill, render_rect)
        pygame.draw.rect(surf, self.outline, render_rect)
