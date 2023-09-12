import pygame

class Ship:
    """ A class to manage the ship """

    def __init__(self, ai_game):
        """ Initialize the ship and set its starting position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()              # to place the ship in the correct location on the screen
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen

        self.rect.midbottom = self.screen_rect.midbottom

        # self.x = 1100
        # self.y = 700
        # self.rect = self.image.get_rect(x=self.x, y=self.y)

        # # Store a decimal value for the ship's horizontal position.
        # self.x = float(self.rect.x)

    #     # Movement flag
        self.moving_right = False
        self.moving_left = False

    # def update(self):
    #     """ Update the ship's position based on the movement flags. """
    #     """ Update the ship's x value, not the rect """
    #     if self.moving_right:
    #         self.x += self.settings.ship_speed
    #     if self.moving_left:
    #         self.x -= self.settings.ship_speed

    #     # Update rect object from self x
    #     self.rect.x = self.x


# With this modification for 'moving left' flag rect.x attribute decreases in 1(instead of 1.5) and increases on 2(instead of 1.5)

    # def update(self):
    #     if self.moving_right:
    #     #     self.rect.x += self.settings.ship_speed
    #     # if self.moving_left:
    #     #     # self.rect.x -= self.settings.ship_speed


    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)
