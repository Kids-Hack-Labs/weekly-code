'''
    ***Standalone AABB model viewer***
    Created:       Jun 01, 2020
    Last Modified: Jun 04, 2020

    Remarks:
    -> Designed in "pure" pygame, for
       visualization purposes only

    Code Task:
    -> Implement a list of rects (DONE)
    -> Implement a sole Rect() to
       view an overlap result (DONE)
'''
#Basic imports
#imported Rect directly to simplify names
import sys, pygame
from pygame import Rect

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Rect Test")

    #Create a Rectangle
    #Obs.: will be mouse-controlled
    #optional: create a tuple for the rectangle's colour
    player_rect = Rect(0, 0, 100, 100)
    player_colour = (0, 255, 0)
         
    #Create a list of rectangles
    rect_list = [Rect(550, 100, 200, 200),
                 Rect(150, 150, 350, 350),
                 Rect(800, 600, 150, 150)]

    #optional: create a list of colours (should match rect
    #list length) 
    colours = [(255, 255,   0),
               (255,   0, 255),
               (  0, 255, 255)]

    #Create an extra rectangle for overlap detection
    result = Rect(0, 0, 0, 0)
    
    is_running = True

    #Game loop
    while is_running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                is_running = False

        #Controlling the player rectangle with the mouse
        #(uncomment code below)
        player_rect.center = pygame.mouse.get_pos()

        #clip result rectangle:
        #result = player_rect.clip(rect_list[0])
        #advanced: clip against a list
        result = player_rect.clip(rect_list[player_rect.collidelist(rect_list)])

        #Render part
        screen.fill((0, 0, 127))

        #Render rectangles:
        #1: Render player rectangle
        pygame.draw.rect(screen, player_colour, player_rect)

        #2: Render list of rectangles
        #optional: use a for loop to render them with the
        #same or different colours. If using a for loop, the
        #example code below should be adjusted accordingly
        for i in range(len(rect_list)):            
            pygame.draw.rect(screen, colours[i], rect_list[i])

        #If there is a collision, render it here
        #Alternative if statements:
        #if player_rect.collidelist(rect_list) > -1:
        #if result.width > 0 and result.height > 0:
        if result.width > 0 < result.height:
            pygame.draw.rect(screen, (255, 0, 0), result, 5)

        #Render loop end
        pygame.display.flip()

    #cleanup
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    
