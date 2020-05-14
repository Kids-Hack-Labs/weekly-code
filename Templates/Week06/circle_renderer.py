'''
    Circle Renderer Class
    Inherits from Behaviour
    A simple circle renderer
'''
import pygame
from behaviour import Behaviour

class CircleRenderer(Behaviour):
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
        center = None #MUST CHANGE
        #Draw calls go here
