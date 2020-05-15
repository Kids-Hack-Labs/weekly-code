import pygame
from example import Example

class KeyboardExample(Example):
    def __init__(self, _x, _y):
        self.size = 50
        self.speed = 2
        super().__init__(_x, _y)

    def update(self):
        pressedKeys = pygame.key.get_pressed()

        w = pressedKeys[pygame.K_w]
        a = pressedKeys[pygame.K_a]
        s = pressedKeys[pygame.K_s]
        d = pressedKeys[pygame.K_d]

        target = [0, 0]

        if w == True:
            target[1] -= 1
        if a == True:
            target[0] -= 1
        if s == True:
            target[1] += 1
        if d == True:
            target[0] += 1
    
        target[0] *= self.speed
        target[1] *= self.speed

        self.x += target[0]
        self.y += target[1]
        
    def render(self):
        square = pygame.Rect(self.x, self.y, self.size, self.size)
        square_colour = pygame.Color(255, 127, 0)
        square_outline = pygame.Color(0, 255, 0)
        pygame.draw.rect(pygame.display.get_surface(), square_colour, square)
        pygame.draw.rect(pygame.display.get_surface(), square_outline, square, 3)
        
