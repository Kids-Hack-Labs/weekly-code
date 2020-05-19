'''
    ***Test Screen class***
    Pygame "engine"
    Designed to test a couple effects
'''
import pygame
from engine.screen import Screen
from engine.game_object import GameObject

from engine.rect_renderer import RectRenderer
from engine.movement import Movement

class TestScreen(Screen):
    def __init__(self):
        super().__init__()
        self.bg_colour = (255, 255, 0)

    def start(self):

        # this is the player's gameobject
        player = GameObject()

        player.add_behaviour( RectRenderer() )
        player.add_behaviour( Movement() )

        self.add_game_object(player)
        
        super().start()
        
    def update(self):
        super().update()
        
    def render(self):
        background = pygame.display.get_surface()
        background.fill(self.bg_colour)
        super().render()
        
    def add_game_object(self, game_object):
        super().add_game_object(game_object)
        
    def remove_game_object(self, game_object):
        super().remove_game_object(game_object)
