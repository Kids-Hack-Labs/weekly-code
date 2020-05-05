import pygame, sys

# blueprint for the everything in our scene
class GameObject:

    # this is where we 'construct' our object
    # the 'x', and 'y' values will be passed to our 'constructor' as arguments
    def __init__(self, x, y):

        # here is where we create and set the position of our object
        self.x = x
        self.y = y

    # this function is called every frame
    def update(self):
        pass        

    def translate(self, target):

        # target is a 'tuple'

        # ( x, y )
        #   0  1

        # move to the position
        self.x = target[0]
        self.y = target[1]

    # this method is responsible for rendering (drawing) our object
    def render(self, surface):

        # the colour of the rect
        # stored in type 'tuple'
        colour = (0, 0, 0) # black

        # width and height of our object
        width = 10
        height = 10
        
        # here we create the dimensions for our object
        # the dimensions are stored in a 'tuple'
        dimensions = (self.x, self.y, width, height)

        # how could you centre the rectangle on the position?

        # draw the rectangle
        pygame.draw.rect(surface, colour, dimensions, 1)

    
