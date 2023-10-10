import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single alien in the fleet """

    def __init__(self, ai_game):
        """ Initialize the alien and set its starting position. """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()


        """ Load the alien image and set its rect attribute """
        self.image = pygame.image.load("images/ufo1.png")
        self.rect = self.image.get_rect()

        """ Start each new alien near the top left of the screen """
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y) 


    def check_edges(self):
        """ Return true if alien is at edge of screen """
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
             return True

    def update(self):
            """ Move the alien to the right """
            self.x += (self.settings.alien_speed *
                       self.settings.fleet_direction)
            self.rect.x = self.x
            print(self.rect.x)
            print(self.rect.y)


    def check_bottom(self):
        if self.rect.top >= self.screen_rect.bottom:
             return True