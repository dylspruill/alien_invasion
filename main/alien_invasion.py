#Dylan Spruill
#References: Textbook (Python Crash Course third edition)

import pygame
import sys
from time import sleep
import settings
from game_stats import GameStats

from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """This is the class for the game AlienInvasion"""

    def __init__(self):
        """initialize the alien invasion game"""
        self.settings = settings.Settings()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  #Size of screen (if it doesn't work use 900,600)
        # Do not use full screen mode
        self.bg_color = (self.settings.bg_color) #Search up rbg color to get the three numbers that are dif than ones chap used
        pygame.display.set_caption("Alien Invasion - David Kordziel")

        #Create an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Start Alien Invasion in an active state
        self.game_active = True
    
    def _check_events(self):
        """Respond to user events (keyboard/mouse) and return 'quit_game' to end the game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit_game'
            elif event.type == pygame.KEYDOWN:
                if self._check_keydown_events(event) == 'quit_game':
                    return 'quit_game'
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to Keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
        elif event.key == pygame.K_q:
            return 'quit_game'
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        
    def _check_keyup_events(self, event):
        """Respond to quick key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """update the position of bullets and get ride of old bullets"""
        #Update bullet positions
        self.bullets.update()

        #Get ride of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        # Remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            #Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_screen(self):
        """update the main game screen"""

        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        #Create an alien and keep adding aliens until there no room left
        #Spacing between aliens is one alien width and one alien height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height    
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            #Finished a row; reset x value, and increment y value/
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position   
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions"""
        self._check_fleet_edges()
        self.aliens.update()

        #Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        #Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            #Decrement ships_left
            self.stats.ships_left -= 1

            #Get ride of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            #Create a new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #Treat this the same as if the ship got hit
                self._ship_hit()
                break

    def run_game(self):
        """Start the game and loop until the game ends"""

        play = True
        while play:

            if self._check_events() == 'quit_game':
                play = False
            else:
                self._check_events()

                if self.game_active:
                    self.ship.update()
                    self._update_bullets()
                    self._update_aliens()

                self._update_screen()
                self.clock.tick(60)

           
        sys.exit()


    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()




