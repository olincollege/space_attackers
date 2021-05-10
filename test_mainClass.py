# Import all required libraries.
import pytest
import requests
from player import Player

# enemyX=0
# enemyY=1
# bulletX=2
# bulletY=1
# playerX=2
# playerY=1


DISTANCES=[
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),                   
]


PLAYER_DISTANCES=[
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),
 (0,1,2,1,False),                   
]

@pytest.mark.parametrize("enemyX,enemyY,bulletX,bulletY,status", DISTANCES)
def test_collision(enemyX,enemyY,bulletX,bulletY,status):
    """
    Check that distances between the enemy cordinates and the bullet cordinates are close
    enough to lead to the death of a player
    Args:
        enemyX: X cordinate of the enemy.
        enemyY: Y cordinate of the enemy
        bulletX:X cordinate of the bullet
        bulletY:Y cordinate of the bullet
        status: status of the collission, true or false
    """
    assert Player.isCollision(enemyX,enemyY,bulletX,bulletY) == status
@pytest.mark.parametrize("enemyX,enemyY,playerX,playerY,status", PLAYER_DISTANCES)
def test_isKilled(enemyX,enemyY,playerX,playerY,status):
    """
    Check that distances between the enemy cordinates and the player cordinates are close
    enough to lead to the death of a player

    Args:
        enemyX: X cordinate of the enemy.
        enemyY: Y cordinate of the enemy
        playerX:X cordinate of the player
        playerY:Y cordinate of the player
        status: status of the death, true or false
    """
    assert Player.isKilled(enemyX,enemyY,playerX,playerY) == status

