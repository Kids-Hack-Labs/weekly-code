'''
    Now I feel weird without headers...
'''

import sys, pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Rect Test")
    rects = [pygame.Rect(100, 100, 100, 100), pygame.Rect(150, 150, 150, 150)]
    result = rects[0].clip(rects[1])
    
    is_running = True
    while is_running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                is_running = False
        rects[0].center = pygame.mouse.get_pos()
        result = rects[0].clip(rects[1])
        screen.fill((0, 0, 127))
        pygame.draw.rect(screen, (0, 255, 0, 127), rects[0])
        pygame.draw.rect(screen, (255, 255, 0, 127), rects[1])
        if result.width > 0 < result.height:
            pygame.draw.rect(screen, (255, 0, 0), result, 5)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    
