import pytest
import pygame
from main.alien_invasion import AlienInvasion

@pytest.fixture
def alien_invasion():
    pygame.init()
    game = AlienInvasion()
    yield game
    pygame.quit()

def test_game_initialization(alien_invasion):
    assert alien_invasion.game_active is True, "Game should be active after initialization."
    assert alien_invasion.ship is not None, "Ship should be initialized in the game."
    assert alien_invasion.bullets is not None, "Bullets group should be initialized in the game."
    assert alien_invasion.aliens is not None, "Aliens group should be initialized in the game."

def test_ship_initial_position(alien_invasion):
    assert alien_invasion.ship.rect.midbottom == alien_invasion.screen.get_rect().midbottom, "Ship should be centered at the bottom of the screen."

def test_bullet_firing(alien_invasion):
    initial_bullet_count = len(alien_invasion.bullets)
    alien_invasion._fire_bullet()
    assert len(alien_invasion.bullets) == initial_bullet_count + 1, "Bullet should be fired and added to the bullets group."

def test_alien_fleet_creation(alien_invasion):
    assert len(alien_invasion.aliens) > 0, "Aliens fleet should be created after game initialization."

def test_ship_hit(alien_invasion):
    initial_ships_left = alien_invasion.stats.ships_left
    alien_invasion._ship_hit()
    assert alien_invasion.stats.ships_left == initial_ships_left - 1, "Ship hit should decrease the ships left by 1."


def test_game_over(alien_invasion):
    alien_invasion.stats.ships_left = 1
    alien_invasion._ship_hit()
    assert alien_invasion.game_active is False, "Game should become inactive when all ships are lost."

def test_alien_reaches_bottom(alien_invasion):
    alien = next(iter(alien_invasion.aliens))
    alien.rect.bottom = alien_invasion.settings.screen_height
    alien_invasion._check_aliens_bottom()
    assert alien_invasion.stats.ships_left < alien_invasion.settings.ship_limit, "Alien reaching bottom should decrease ships left."
