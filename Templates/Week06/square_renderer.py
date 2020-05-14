'''
    Square Renderer Class
    Inherits from Behaviour
    A simple Square renderer
'''
import pygame
from behaviour import Behaviour

class SquareRenderer(Behaviour):
    def __init__(self):
        #Setup info goes here
        super().__init__()
    def update(self):
        #Renderers usually don't
        #concern themselves with updates
        pass
    def render(self):
        #Render functionality goes here
        surf = pygame.display.get_surface()
        render_rect = pygame.Rect()#MUST INCLUDE STUFF
        #Draw calls go here
