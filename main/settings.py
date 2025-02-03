class Settings:
    """A collection of the game settings for Alien Invasions"""

    def __init__(self):
        """Initialize the settings for the Alien Invasion instance"""

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (180,0,180)

        #ship settings
        self.ship_speed = 2
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #Fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
