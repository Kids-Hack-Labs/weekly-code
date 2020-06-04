'''
    ***Test Screen class***
    Implemented with the KHL Engine
    Created       May 23, 2020
    Last Modified Jun 06, 2020

    Remarks:
    -> Implementation of KHL Engine's Screen class
    -> Contains the Game Objects and Behaviours
       needed for the demo
    -> Implements custom collision detection, for
       visualization purposes
'''
#Basic (and Engine) imports
import pygame
from engine.screen import Screen
from engine.game_object import GameObject
from engine.box_collider import BoxCollider
#Behaviour (source code) Imports
from src.rect_renderer import RectRenderer
from src.ship_renderer import ShipRenderer
from src.movement import Movement
from src.shield_renderer import ShieldRenderer
from src.ship_commands import ShipCommands
#"Convenience" imports
from pygame.math import Vector2

class TestScreen(Screen):
    def __init__(self):
        super().__init__()

    def start(self):
        #Background setting functionality
        self.image = pygame.image.load("assets/Images/Space.jpg")

        #player character setting:
        #-> Sets the Transform so that the ship begins the game
        #   in the middle of the screen
        #-> Adds a box collider and sets its size
        #-> Also adds Movement, ShipCommands and ShipRenderer
        #   functionality
        #-> Adds the Game Object to the game_objects list
        test_go = GameObject()
        test_go.name = "Ship"
        test_go.get_behaviour("Transform").position = Vector2(512, 388)
        test_go.add_behaviour(BoxCollider())
        test_go.get_behaviour("BoxCollider").extent = Vector2(150)
        test_go.add_behaviour(ShipRenderer())
        test_go.add_behaviour(ShieldRenderer())
        test_go.add_behaviour(Movement())
        test_go.add_behaviour(ShipCommands())
        self.add_game_object(test_go)

        #insert obstacle below:
        #-> Name it "Obstacle"
        #-> Position its Transform at 200, 200
        #-> Add a BoxCollider behaviour
        #-> Set the BoxCollider's is_debug flag to True
        #-> Set the BoxCollider's extent to 350, 350
        #->Add it to the screen's game_objects list
        another_go = GameObject()
        another_go.name = "Obstacle"
        another_go.get_behaviour("Transform").position = Vector2(200, 200)
        another_go.add_behaviour(BoxCollider())
        another_go.get_behaviour("BoxCollider").is_debug = True
        another_go.get_behaviour("BoxCollider").extent = pygame.math.Vector2(350)
        self.add_game_object(another_go)

        #insert the overlap game object here:
        #-> Name it "Overlap"
        #-> Add a RectRenderer behaviour
        #-> Set the RectRenderer's colour
        #-> Add the Game Object to the screen's game_objects list
        overlap_go = GameObject()
        overlap_go.name = "Overlap"
        overlap_go.add_behaviour(RectRenderer())
        overlap_go.get_behaviour("RectRenderer").colour = (255, 0, 0)
        self.add_game_object(overlap_go)

        #base class start() call
        super().start()
        
    def update(self):
        super().update()

        #Overlap management:
        #-> Get the Ship's BoxCollider behaviour
        #   and store it in a variable
        #-> Get the Obstacle's BoxCollider behaviour
        #   and store it in a variable
        #-> Assign the result of the ship box's clipping
        #   by the obstacle's box to a temporary variable
        #-> Assign the temporary box's centre to the Overlap's position
        #-> Assign the temporary box to the rect attribute of the
        #   Overlap's RectRenderer behaviour
        ship_box = self.game_objects["Ship"].get_behaviour("BoxCollider").box
        obst_box = self.game_objects["Obstacle"].get_behaviour("BoxCollider").box
        temp_box = ship_box.clip(obst_box)
        self.game_objects["Overlap"].get_behaviour("Transform").position = temp_box.center
        self.game_objects["Overlap"].get_behaviour("RectRenderer").rect = temp_box
        
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
