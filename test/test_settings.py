import pytest
from main.settings import Settings

@pytest.fixture
def settings():
    return Settings()

def test_screen_settings(settings):
    assert settings.screen_width == 1200, "Screen width should be 1200."
    assert settings.screen_height == 800, "Screen height should be 800."
    assert settings.bg_color == (180, 0, 180), "Background color should be (180, 0, 180)."

def test_ship_settings(settings):
    assert settings.ship_speed == 2, "Ship speed should be 2."
    assert settings.ship_limit == 3, "Ship limit should be 3."

def test_bullet_settings(settings):
    assert settings.bullet_speed == 2.5, "Bullet speed should be 2.5."
    assert settings.bullet_width == 3, "Bullet width should be 3."
    assert settings.bullet_height == 15, "Bullet height should be 15."
    assert settings.bullet_color == (60, 60, 60), "Bullet color should be (60, 60, 60)."
    assert settings.bullets_allowed == 3, "Bullets allowed should be 3."

def test_alien_settings(settings):
    assert settings.alien_speed == 1.0, "Alien speed should be 1.0."
    assert settings.fleet_drop_speed == 10, "Fleet drop speed should be 10."
    assert settings.fleet_direction == 1, "Fleet direction should be 1 (right)."
