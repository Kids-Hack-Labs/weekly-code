'''
    Player Controller class
'''
import pygame
from behaviour import Behaviour

class PlayerController(Behaviour):
    def __init__(self):
        self.hor_speed = 2
        self.vert_speed = 1
        super().__init__()
    def update(self):
        key_list = pygame.key.get_pressed()

        w = key_list[pygame.K_w]
        a = key_list[pygame.K_a]
        s = key_list[pygame.K_s]
        d = key_list[pygame.K_d]

        target = [0, 0]
        if w:
            target[1] -= 1
        if a:
            target[0] -= 1
        if s:
            target[1] += 1
        if d:
            target[0] += 1

        target[0] *= self.hor_speed
        target[1] *= self.vert_speed

        self.game_object.x += target[0]
        self.game_object.y += target[1]

        #boundary checks
        surf = pygame.display.get_surface()
        if self.game_object.x < 0:
            self.game_object.x = 0
        if self.game_object.x > surf.get_width():
            self.game_object.x = surf.get_width()
        if self.game_object.y < 0:
            self.game_object.y = 0
        if self.game_object.y > surf.get_height():
            self.game_object.y = surf.get_height()
            

    def render(self):
        pass
