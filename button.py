import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """ Initialize button attributes """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.base_color = (0, 125, 0)
        self.highlighted_color = (0, 36, 0)

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = self.base_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.msg = msg

        # The button message needs to be prepped only once.
        self._prep_msg()

    def _prep_msg(self):
        """ Turn msg into a rendered image and center text on the button """
        self.msg_image = self.font.render(self.msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def update_msg_position(self):
        self.msg_image_rect.center = self.rect.center
    
    def set_base_color(self):
        self.button_color = self.base_color
        self._prep_msg()

    def set_highlighted_color(self):
        self.button_color = self.highlighted_color
        self._prep_msg()

    def draw_button(self):
        """ Draw blank button and then draw message """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        