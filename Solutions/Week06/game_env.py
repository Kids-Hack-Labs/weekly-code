import sys, pygame
#Base Game Object
from game_object import GameObject

#custom behaviours
from movement import Movement
from circle_renderer import CircleRenderer
from player_controller import PlayerController
from square_renderer import SquareRenderer

class Game:
    def __init__(self, _width, _height, _title):
        pygame.init()
        window_size = _width, _height
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption(_title)
        
        self.bg_colour = (98, 127, 255)

        #maybe convert this into a dictionary in the future
        self.game_objects = []
        self.populate()

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
        for game_object in self.game_objects:
            if game_object.is_active:
                game_object.update()

    def render(self):
        self.screen.fill(self.bg_colour)
        #other renders go here
        for game_object in self.game_objects:
            if game_object.is_active:
                game_object.render()
        pygame.display.flip()

    def cleanup(self):
        print("bye")
        pygame.quit()
        sys.exit()

    #future functionality: Screen loading
    def populate(self):
        player = GameObject(400, 225)
        player.add_behaviour(PlayerController())
        player.add_behaviour(SquareRenderer())
        self.game_objects.append(player)
        
        for i in range(8):
            obstacle = GameObject(0, 0)
            obstacle.x = i * 100 + 50
            obstacle.y = i * 50
            obstacle.add_behaviour(Movement())
            obstacle.add_behaviour(CircleRenderer())
            self.game_objects.append(obstacle)
