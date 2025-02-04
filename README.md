# Alien Invasion Game
A Python game featuring a player-controlled spaceship that shoots bullets to destroy descending aliens.

## Features
* Player-controlled spaceship that moves left and right.
* Bullet firing mechanics with collision detection.
* Alien fleet generation and movement.
* Game statistics tracking, including remaining lives.
* Progressive difficulty as aliens are cleared.


## Installation
Clone the repository:
```
git clone https://github.com/yourusername/alien-invasion.git
cd alien-invasion
```

## Install dependencies: Make sure you have Python 3.x and Pygame installed.
```
pip install pygame
```

## Running the Game
Run the main game file:
```
python alien_invasion.py
```
## Controls

Right Arrow: Move ship right
Left Arrow: Move ship left
Spacebar: Fire bullets

Q: Quit game

## Testing
Unit tests are written using pytest.

* Running Tests
To run all tests:
```
pytest
```

## Test Coverage
* Ship Tests: Verify ship movement, positioning, and boundaries.
  
* Bullet Tests: Check bullet creation, movement, and off-screen behavior.
  
* Alien Tests: Ensure proper alien movement, edge detection, and collisions.
  
* Game Tests: Validate overall game logic, including bullet firing and game over conditions.

## Technologies Used
* Python 3
* Pygame
* Pytest

