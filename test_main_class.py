"""
Test the collision calculations of the Player class, inheriting from the
Spaceship class.
"""

# Import all required libraries.
import pytest
from player import Player, is_collision, is_killed
from spaceship import Spaceship

DISTANCES=[
 # Check that if they are at the same coordinate, they have collided.
 (0,0,0,0,True),
 # Check that if each variable is below 27, they return True, and if
 # they are greater than or equal to 27, that they return False, as
 # the cutoff distance for collision is 27.
 (26,0,0,0,True),
 (27,0,0,0,False),
 (28,0,0,0,False),
 (0,26,0,0,True),
 (0,27,0,0,False),
 (0,28,0,0,False),
 (0,0,26,0,True),
 (0,0,27,0,False),
 (0,0,28,0,False),
 (0,0,0,26,True),
 (0,0,0,27,False),
 (0,0,0,28,False),
 # Test that the cutoff distance is correct when shared across the
 # two-variables, and lines up with the calculations.
 (19.091883,19.091883,0,0,True),
 (19.091884,19.091884,0,0,False),
]

playerSpaceship = Spaceship('assets/space-invaders.png',2,7)
player=Player(playerSpaceship)
@pytest.mark.parametrize("enemy_x,enemy_y,bullet_x,bullet_y,status", DISTANCES)
def test_collision(enemy_x,enemy_y,bullet_x,bullet_y,status):
    """
    Check that distances between the enemy cordinates and the bullet cordinates are close
    enough to lead to the death of a player
    Args:
        enemy_x: An int or float value representing the X cordinate of the
                 enemy, but in actual functioning code is an int.
        enemy_y: An int or float value representing the Y cordinate of the
                 enemy, but in actual functioning code is an int.
        bullet_x: An int or float value representing the X cordinate of the
                  bullet, but in actual functioning code is an int.
        bullet_y: An int or float value representing the Y cordinate of the
                  bullet, but in actual functioning code is an int.
        status: A boolean value representing the status of the collision.
    """

    assert is_collision(enemy_x,enemy_y,bullet_x,bullet_y) == status

@pytest.mark.parametrize("enemy_x,enemy_y,player_x,player_y,status", DISTANCES)
def test_is_killed(enemy_x,enemy_y,player_x,player_y,status):
    """
    Check that distances between the enemy cordinates and the player cordinates are close
    enough to lead to the death of a player

    Args:
        enemy_x: An int or float value representing the X cordinate of the
                 enemy, but in actual functioning code is an int.
        enemy_y: An int or float value representing the Y cordinate of the
                 enemy, but in actual functioning code is an int.
        player_x: An int or float value representing the X cordinate of the
                  player, but in actual functioning code is an int.
        player_y: An int or float value representing the Y cordinate of the
                  player, but in actual functioning code is an int.
        status: A boolean value representing the status of the collision.
    """
    assert is_killed(enemy_x,enemy_y,player_x,player_y) == status
