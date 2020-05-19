'''
    ***Main game App file***
    Pygame "engine"
    Designed to test effects different effects
'''
from engine.game_env import Game

def main():
    g = Game(1024, 768, "my first pygame-engine")
    g.run()

if __name__ == "__main__":
    main()
