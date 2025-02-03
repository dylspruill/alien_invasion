import pytest
import pygame
from main.ship import Ship
from main.settings import Settings

@pytest.fixture
def init_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    yield screen, settings
    pygame.quit()

@pytest.fixture
def ship(init_game):
    screen, settings = init_game
    return Ship(ai_game=type('MockGame', (object,), {'screen': screen, 'settings': settings}))

def test_ship_initial_position(ship):
    screen_rect = ship.screen.get_rect()
    assert ship.rect.midbottom == screen_rect.midbottom, "Ship is not centered at the bottom of the screen."

def test_ship_movement_right(ship):
    initial_x = ship.x
    ship.moving_right = True
    ship.update()
    assert ship.x > initial_x, "Ship did not move right when moving_right was set to True."

def test_ship_movement_left(ship):
    ship.rect.x = ship.settings.screen_width / 2  # Position ship in the middle
    ship.x = float(ship.rect.x)
    initial_x = ship.x
    ship.moving_left = True
    ship.update()
    assert ship.x < initial_x, "Ship did not move left when moving_left was set to True."

def test_ship_stops_at_right_edge(ship):
    ship.rect.right = ship.screen.get_rect().right
    ship.x = float(ship.rect.x)
    ship.moving_right = True
    ship.update()
    assert ship.rect.right <= ship.screen.get_rect().right, "Ship moved beyond the right edge of the screen."

def test_ship_stops_at_left_edge(ship):
    ship.rect.left = 0
    ship.x = float(ship.rect.x)
    ship.moving_left = True
    ship.update()
    assert ship.rect.left >= 0, "Ship moved beyond the left edge of the screen."

def test_center_ship(ship):
    ship.rect.x = 100  # Move ship away from center
    ship.center_ship()
    screen_rect = ship.screen.get_rect()
    assert ship.rect.midbottom == screen_rect.midbottom, "Ship did not re-center correctly."
