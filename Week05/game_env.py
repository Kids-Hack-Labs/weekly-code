import sys, pygame
from example import Example
from mouse_example import MouseExample
from keyboard_example import KeyboardExample

def main(): #application entry point
  #SETUP STEP:
  pygame.init() #pygame initialization
  #screen size settings
  screenSize = width, height = 800, 450
  #set screen size in pygame
  screen = pygame.display.set_mode(screenSize)
  #screen title
  pygame.display.set_caption("Week 05 class")

  isRunning = True #flag to control app execution

  bgColour = (98, 127, 255) #Background colour - Tuple
  examples = [KeyboardExample(200, 200), MouseExample()]

  #GAME LOOP STEP
  while (isRunning):
    for evt in pygame.event.get():
      if evt.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    #Update part of the loop
    #mousePos = pygame.mouse.get_pos()
    #mySquare.translate(mousePos)
    for example in examples:
      example.update()

    #Draw/render part of the loop
    screen.fill(bgColour)
    for example in examples:
      example.render()
    pygame.display.flip()

if __name__ == "__main__":
  main()
