import pygame, sys

# blueprint for the everything in our scene
class GameObject:

    # this is where we 'construct' our object
    # the 'x', and 'y' values will be passed to our 'constructor' as arguments
    def __init__(self, x, y):

        # here is where we create and set the position of our object
        self.x = x
        self.y = y

        # controls the speed our gameobject can move at
        self.speed = 10

    # this function is called every frame
    def update(self):

        # a list of every key state (true == pressed, false == not pressed)
        keysDown = pygame.key.get_pressed()

        # get the keys we want from the list
        w = keysDown[pygame.K_w]
        a = keysDown[pygame.K_a]
        s = keysDown[pygame.K_s]
        d = keysDown[pygame.K_d]

        # this will store our desired movement as a 2d vector
        # essentially a vector is a value with 2 (or more) components
        target = [0, 0]

        # by default the target wont 'point' anywhere
        # if we add one to the x value the vector will look like
        # -> (1, 0)

        # the 'w' key is pressed
        if w == True:
            target[1] -= 1

        # if the 'a' key is pressed
        if a == True:
            target[0] -= 1
        if s == True:
            target[1] += 1
        if d == True:
            target[0] += 1

        # multiply both components of our target vector by our speed
        # ps speed is defined in our __init__ method
        target = [i * self.speed for i in target]

        # apply the transformation
        self.x += target[0]
        self.y += target[1]

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

    
