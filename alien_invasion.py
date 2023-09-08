# 29.08.2023

import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """

    def __init__(self):
        """ initializa the game, and create game resources.  """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    
    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
            """ Respond to keypresses and mouse events """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


    def _update_screen(self):
            """ Update images on the screen, and flip to the new screen """
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()



# if __name__ == '__main__':
#     # Make a game instance and run the game 
#     ai = AlienInvasion()
#     ai.run_game()


# # 12-2. Game Character

# import pygame 

# import sys

# class Bitch_in_Rectangle:
#     def __init__(self):
#         pygame.init()
#         self.screen_width = 1920
#         self.screen_height = 1080
#         self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
#         self.bg_color = (100, 200, 185)
#         pygame.display.set_caption("Beautiful Bitch")
#         self.bitch = Bitch(self)


#     def bitchh(self):
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()
            
#             self.screen.fill(self.bg_color)
#             self.bitch.draw_bitch()
#             pygame.display.flip()            


        



# class Bitch:
#     def __init__(self, ai):
#         self.screen = ai.screen
#         self.screen_rect = ai.screen.get_rect()          
#         self.image = pygame.image.load("images/bb.bmp") 
#         self.rect = self.image.get_rect()
  
#         # Start each new session at the center of the panarama
#         self.rect.center = self.screen_rect.center

#     def draw_bitch(self):
#          self.screen.blit(self.image, self.rect)



# if __name__ == "__main__":
#     aai = Bitch_in_Rectangle()
#     aai.bitchh()






import pygame 

import sys

from bitch_settings import Bitch_sets
from bitch_module import Bitchi

class Bitch_image:
    def __init__(self):
          pygame.init()
          self.settings = Bitch_sets()
          self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
          pygame.display.set_caption("The Image of Girl")
          self.bitch = Bitchi(self)    

    def run_game(self):
        while True:
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                      sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.bitch.blitgirl()
            pygame.display.flip()

    # def draw_girl(self):
    #      self.bitch.blitgirl()


if __name__ == "__main__":
    ai = Bitch_image()
    ai.run_game()


         
     