'''
    Movement Class
    Inherits from Behaviour
    Built for automatic movement.
    Will simply bounce things
    up and down the screen
'''
from behaviour import Behaviour

class Movement(Behaviour):
    def __init__(self):
        #Movement specifics go here
        super().__init__()
    def update(self):
        #update specifics go here
    def render(self):
        #Movement does not render
        pass 
