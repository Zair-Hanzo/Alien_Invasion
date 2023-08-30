# 29.08.2023

import sys

import pygame

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """

    def __init__(self):
        """ initializa the game, and create game resources.  """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (100, 200, 180)

    
    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

            # Redraw the screen  during each pass through the loop.
            self.screen.fill(self.bg_color)

if __name__ == '__main__':
    # Make a game instance and run the game 
    ai = AlienInvasion()
    ai.run_game()



