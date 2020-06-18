'''
    Button Behaviour Class
    KHL Engine
    Designed to demonstrate states
    and screen change
'''
#base imports
import pygame
from engine.behaviour import Behaviour

class ButtonBehaviour(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "ButtonBehaviour"
        self.is_hover = False
        self.is_pressed = False

    def start(self):
        super().start()
    def update(self):
        transf = self.game_object.get_behaviour("Transform")
        collider = self.game_object.get_behaviour("BoxCollider")
        renderer = self.game_object.get_behaviour("RectRenderer")

        collider.box.center = transf.position
        renderer.rect.center = transf.position
        renderer.rect.width = collider.box.width
        renderer.rect.height = collider.box.height

        self.is_hover = collider.box.collidepoint(pygame.mouse.get_pos())

        mouse_buttons = pygame.mouse.get_pressed()

        self.is_pressed = self.is_hover and mouse_buttons[0] == True

        if (self.is_pressed):
            renderer.colour = (0, 255, 0)
            from engine.game_env import Game
            from src.test_screen import TestScreen
            Game.instance.set_screen(TestScreen())
        elif (self.is_hover):
            renderer.colour = (0, 0, 255)
        else:
            renderer.colour = (255, 0, 0)
    def render(self):
        super().render()
