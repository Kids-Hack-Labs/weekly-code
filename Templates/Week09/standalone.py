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
    #Create a list of rectangles
    #optional: create a list of colours (should match rect
    #list length)

    #Create an extra rectangle for overlap detection
    
    is_running = True

    #Game loop
    while is_running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                is_running = False

        #mouse-controlled rectangle (uncomment code below)
        #rects[0].center = pygame.mouse.get_pos()

        #clip result rectangle (insert code below)

        #Render part
        screen.fill((0, 0, 127))

        #Render rectangles:
        #optional: use a for loop to render them with the
        #same or different colours. If using a for loop,
        #the code below should be adjusting accordingly
        #pygame.draw.rect(screen, (0, 255, 0), rects[0])
        #pygame.draw.rect(screen, (255, 255, 0), rects[1])

        #If there is a collision, render it here:

        #Render loop end
        pygame.display.flip()

    #cleanup:
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    
