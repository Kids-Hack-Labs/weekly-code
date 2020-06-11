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
        #Button states: Hover and Pressed
        self.is_hover = False
        self.is_pressed = False

    def start(self):
        super().start()
    def update(self):
        #Button depends on the game object's transform,
        #box collider and rect renderer
        

        #Center the collider and the renderer in the transform's position
        #Set the renderer's size to match the collider box's size
        

        #Check for mouse hovering over button
        
        #Get mouse buttons pressed and store them in a variable

        #We just want to detect button presses
        #when the mouse is over the button
        

        #State checking:
        #if pressed:
        #   set rect's colour to green
        #   import Game Class and TestScreen Class
        #   Set screen to TestScreen
        #if hovered:
        #   set rect's colour to blue
        #else:
        #   set rect's colour to red
        
    def render(self):
        super().render()
