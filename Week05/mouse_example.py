import pygame
from example import Example

class MouseExample(Example):
    def __init__(self):
        self.radius = 25
        #meets super's initializer argument requirements
        super().__init__(400, 225)

    def update(self):
        target = pygame.mouse.get_pos()
        self.x = target[0]
        self.y = target[1]

    def render(self):
        center = (self.x, self.y)
        circle_colour = pygame.Color(255, 0, 255)
        circle_outline = pygame.Color(255, 255, 0)
        pygame.draw.circle(pygame.display.get_surface(), circle_colour, center, self.radius)
        pygame.draw.circle(pygame.display.get_surface(), circle_outline, center, self.radius, 3)
        
