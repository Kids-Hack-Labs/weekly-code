'''
    Intro Screen class
    KHL Engine
    Designed to demonstrate screen change
    and states
'''
#Base imports
import pygame
from engine.screen import Screen
from engine.game_object import GameObject
from engine.box_collider import BoxCollider
#Source-specific Behaviour imports
from src.rect_renderer import RectRenderer
from src.button_behaviour import ButtonBehaviour
#Convenience imports
from pygame.math import Vector2

class IntroScreen(Screen):
    def __init__(self):
        super().__init__()

    def start(self):
        #Set image (a different one)
        
        #Create Button Game Object, name it "Button", set position
        #Add BoxCollider behaviour and set size
        #Add ButtonBehaviour
        #Add RectRenderer
        #Add game object to screen

        super().start()
    def update(self):
        super().update()
    def render(self):
        surf = pygame.display.get_surface()
        if self.bg_colour != None:
            surf.fill(self.bg_colour)
        if self.image != None:
            surf.blit(self.image, (0,0))
        super().render()
    def add_game_object(self, go):
        super().add_game_object(go)
    def remove_game_object(self, go):
        super().remove_game_object(go)
