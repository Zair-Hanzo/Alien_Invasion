class Settings:
    """ A class to store all settings for Alien Invasion """

    def __init__(self):
        """ Initialize the game's settings """
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (100, 200, 180)
        self.ship_speed = 1.5       # 2.61 sec for speed 1, 1.82 sec for speed 1.5, 1.31 sec for speed 2
        