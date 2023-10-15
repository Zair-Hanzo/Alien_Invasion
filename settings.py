class Settings:
    """ A class to store all settings for Alien Invasion """

    def __init__(self):
        """ Initialize the game's settings """
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (100, 200, 180)
        self.ship_speed = 1.5       # 2.61 sec for speed 1, 1.82 sec for speed 1.5, 1.31 sec for speed 2
        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 10
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        self.alien_speed = 1.8
        self.fleet_drop_speed = 15
        self.fleet_direction = 1
        self.ship_limit = 3