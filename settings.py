class Settings:
    """ A class to store all settings for Alien Invasion """

    def __init__(self):
        """ Initialize the game's STATIC settings """
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (100, 200, 180)
        # self.ship_speed = 1.5       # 2.61 sec for speed 1, 1.82 sec for speed 1.5, 1.31 sec for speed 2
        # Bullet settings
        self.bullet_width = 800
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.fleet_drop_speed = 15

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the the alien point values increase
        self.score_scale = 1.5
        
        self.difficulty_level = 'medium'

        """ DYNAMIC settings  """
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout hte game """
        if self.difficulty_level == 'easy':
            self.ship_limit = 6
            self.bullets_allowed = 12
            self.ship_speed = 2.0
            self.bullet_speed = 3.0
            self.alien_speed = 0.5
        elif self.difficulty_level == 'medium':
            self.ship_limit = 4
            self.bullets_allowed = 8
            self.ship_speed = 3.5
            self.bullet_speed = 5.5
            self.alien_speed = 1.2
        elif self.difficulty_level == "difficult":
            self.ship_limit = 3
            self.bullets_allowed = 5
            self.ship_speed = 5.0
            self.bullet_speed = 8.0
            self.alien_speed = 2.3

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """ Increase speed settings """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale 

        """ Increase alien point values """
        self.alien_points = int(self.alien_points*self.score_scale)
        print(self.alien_points)