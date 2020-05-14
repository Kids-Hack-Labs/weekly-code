import sys, pygame

class Game:
    def __init__(self, _width, _height, _title):
        pygame.init()
        window_size = _width, _height
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption(_title)
        
        self.bg_colour = (98, 127, 255)

        #Something has to go here
        
        self.is_running = True

    def run(self):
        while self.is_running:
            self.process_events()
            self.update()
            self.render()
        self.cleanup()
        
    def process_events(self):
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                self.is_running = False
            #other event processing functionality goes here

    def update(self):
        #something has to go here
        pass

    def render(self):
        self.screen.fill(self.bg_colour)
        #Something has to go here
        pygame.display.flip()

    def cleanup(self):
        print("bye")
        pygame.quit()
        sys.exit()

    #future functionality: Screen loading
