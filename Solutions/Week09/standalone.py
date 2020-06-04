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

    #Create a list of rectangles
    rects = [Rect(100, 100, 100, 100),
             Rect(150, 150, 150, 150),
             Rect(800, 600, 150, 150)]

    #optional: create a list of colours (should match rect
    #list length) 
    colours = [(  0, 255,   0),
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

        #mouse-controlled rectangle (first in rectangle list)
        rects[0].center = pygame.mouse.get_pos()

        #clip result rectangle:
        result = rects[0].clip(rects[1])

        #Render part
        screen.fill((0, 0, 127))

        #Render rectangles:
        #(Commented out due to optional implementation)
        #pygame.draw.rect(screen, (255, 255, 0), rects[0])
        #pygame.draw.rect(screen, (0, 255, 0), rects[1])
        
        #optional:
        #(implemented)
        #use a for loop to render them with the same or
        #different colours. If using a for loop, the code
        #below should be adjusting accordingly
        for i in range(len(rects)):            
            pygame.draw.rect(screen, colours[i], rects[i])

        #If there is a collision, render it here
        if result.width > 0 < result.height:
            pygame.draw.rect(screen, (255, 0, 0), result, 5)

        #Render loop end
        pygame.display.flip()

    #cleanup
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    
