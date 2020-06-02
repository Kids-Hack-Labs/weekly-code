'''
    ***Test Screen class***
    Pygame "engine"
    Designed to test a couple effects
'''
import pygame
from engine.screen import Screen
from engine.game_object import GameObject
from engine.box_collider import BoxCollider
#Behaviour Imports
from src.rect_renderer import RectRenderer
from src.ship_renderer import ShipRenderer
from src.movement import Movement
from src.shield_renderer import ShieldRenderer
from src.ship_commands import ShipCommands


class TestScreen(Screen):
    def __init__(self):
        super().__init__()

    def start(self):
        self.image = pygame.image.load("assets/Images/Space.jpg")
        test_go = GameObject()
        test_go.name = "Ship"
        test_go.get_behaviour("Transform").position.x = 512
        test_go.get_behaviour("Transform").position.y = 388
        test_go.add_behaviour(BoxCollider())
        test_go.get_behaviour("BoxCollider").is_debug = False
        test_go.get_behaviour("BoxCollider").extent = pygame.math.Vector2(150)
        test_go.add_behaviour(ShipRenderer())
        test_go.add_behaviour(ShieldRenderer())
        test_go.add_behaviour(Movement())
        test_go.add_behaviour(ShipCommands())
        self.add_game_object(test_go)

        #insert obstacle here
        #suggestion: Name: "Obstacle", position: 200, 200, size: 350
        

        #insert overlap here
        #suggestion: Name: "Overlap", add BoxCollider and RectRenderer
        #It might be a good idea to recolour the RectRenderer
        
        super().start()
        
    def update(self):
        super().update()

        #create a rect from the overlap using the collider's clip function
        #assign the afore-created rect to the overlap object's collider box
        #reposition the overlap's transform to that center
        #assign the overlap's collider box to the overlap's RectRenderer
        
    def render(self):
        surf = pygame.display.get_surface()
        if self.bg_colour != None:
            surf.fill(self.bg_colour)
        if self.image != None:
            surf.blit(self.image, (0, 0))
        super().render()
        
    def add_game_object(self, game_object):
        super().add_game_object(game_object)
        
    def remove_game_object(self, game_object):
        super().remove_game_object(game_object)
