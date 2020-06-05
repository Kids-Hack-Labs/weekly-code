'''
    ***Standalone AABB model viewer***
    Created:       Jun 01, 2020
    Last Modified: Jun 04, 2020

    Remarks:
    -> Designed in "pure" pygame, for
       visualization purposes only

    Code Task:
    -> Implement a list of rects
    -> Implement a sole Rect() to
       view an overlap result
'''
#Basic imports
#imported Rect directly to simplify names
import sys, pygame
from pygame import Rect

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Rect Test")

    #Create a Rectangle:
    #Obs.: will be mouse-controlled
    #optional: create a tuple for the rectangle's colour
    
    #Create a list of (at least 3) rectangles
    #optional: create a list of colours
    #(should match rect list length)

    #Create an extra rectangle for overlap detection
    
    is_running = True

    #Game loop
    while is_running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                is_running = False

        #Controlling player rect with mouse
        #(uncomment code below)
        #player_rect.center = pygame.mouse.get_pos()

        #clip result rectangle (insert code below)
        #advanced: clip against a list

        #Render part
        screen.fill((0, 0, 127))

        #Render rectangles:
        #1: Render player rectangle

        #2: Render list of rectangles
        #optional: use a for loop to render them with the
        #same or different colours. If using a for loop, the
        #example code below should be adjusted accordingly
        #pygame.draw.rect(screen, (0, 255, 0), rect_list[0])
        #pygame.draw.rect(screen, (255, 255, 0), rect_list[1])

        #If there is a collision, render it here:

        #Render loop end
        pygame.display.flip()

    #cleanup:
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    
