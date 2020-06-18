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
        #Set image
        self.image = pygame.image.load("assets/images/nebula.jpg")
        #Create Button Game Object, name it "Button", set position
        #Add BoxCollider behaviour and set size
        #Add ButtonBehaviour
        #Add RectRenderer
        #Add game object to screen
        button_go = GameObject()
        button_go.name = "Button"
        button_go.get_behaviour("Transform").position = Vector2(512, 384)
        button_go.add_behaviour(BoxCollider())
        button_go.get_behaviour("BoxCollider").extent = Vector2(200, 100)
        button_go.add_behaviour(ButtonBehaviour())
        button_go.add_behaviour(RectRenderer())
        self.add_game_object(button_go)
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
