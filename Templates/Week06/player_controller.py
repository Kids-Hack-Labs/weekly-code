'''
    Player Controller class
    Inherits from Behaviour
    Basically, a rehash
    of what we did last time
'''
import pygame
from behaviour import Behaviour

class PlayerController(Behaviour):
    def __init__(self):
        #Setup variables go here
        super().__init__()
    def update(self):
        #Getting pressed keys
        key_list = pygame.key.get_pressed()

        #Decoding pressed keys
        w = key_list[pygame.K_w]
        a = key_list[pygame.K_a]
        s = key_list[pygame.K_s]
        d = key_list[pygame.K_d]

        #key use
        target = [0,0]

        if w:
            target[1] -= 1
        if a:
            target[0] -= 1
        if s:
            target[1] += 1
        if d:
            target[0] += 1

        #Something goes here

        #Something else goes here

        #Boundary check
        
    def render(self):
        #Movement does not concern
        #itself with rendering
        pass
