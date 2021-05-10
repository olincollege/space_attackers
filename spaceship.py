"""
Define the Spaceship class.
"""

# Import and initialize the pygame library
import pygame
pygame.init()



# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'

class Spaceship:
    """
    This class defines the attributes of the enemy.
    """
    def __init__(self, image,speed,enemies):
        self.image = pygame.image.load(image)
        self.enemy_speed=(speed,)
        self.enemies=enemies

    def representation(self):
        """
        Display the player on the game screen.
        """
        return self.image

    def __repr__(self):

        return f"The {self.enemy_speed[0]} and number of {self.enemies}"

    def speed(self):
        """
        Return the speed.
        """
        return self.speed
