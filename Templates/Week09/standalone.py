'''
    Now I feel weird without headers...
'''

import sys, pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Rect Test")
    #Create a list of rectangles

    #use "Rect().clip(Rect())" to create a third rectangle
    
    is_running = True
    while is_running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                is_running = False
        #mouse-controlled rectangle (uncomment code)
        #rects[0].center = pygame.mouse.get_pos()
        #clip result rectangle (insert code)

        #Render part
        screen.fill((0, 0, 127))

        #Render rectangles
        pygame.draw.rect(screen, (0, 255, 0), rects[0])
        pygame.draw.rect(screen, (255, 255, 0), rects[1])

        #If there is a collision, render it here


        #Render loop end
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    
