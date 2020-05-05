import pygame

from gameobject_example import GameObject

pygame.init()

# 16:9 aspect ratio
screen_size = (800, 450)
screen = pygame.display.set_mode(screen_size)

screen.fill((255, 255, 255))

def gameLoop():
    myObject = GameObject(200, 200)

    isRunning = True
    while isRunning:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('closing...')
                isRunning = False
                pygame.quit()

        target = pygame.mouse.get_pos()
        myObject.translate(target)

        screen.fill((255, 255, 255))
        
        myObject.render(screen)
        pygame.display.flip()

if __name__ == '__main__':
    gameLoop()
