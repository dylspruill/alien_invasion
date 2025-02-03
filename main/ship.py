import pygame

class Ship:
    """A ship in the game alien invasion"""

    def __init__(self, ai_game):
        """Initialize the image and attributes of an ai ship"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/shuttle2.png')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for the ships exact horizontal position
        self.x = float(self.rect.x)

        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        #Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw the ship on the game screen at its current location"""

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        






