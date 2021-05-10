"""
Define the Player class, inheriting from the Spaceship class.
"""
# Import and initialize the pygame library
import math
import pygame
from spaceship import Spaceship

pygame.init()
screen = pygame.display.set_mode([800, 600])

class Player(Spaceship):
    """
    This class takes an instance of spaceship as a parameter and stores it
    as an instance attribute, and has methods to represent the player on
    the screen.
    """
    def __init__(self, spaceship):
        # Initialize the player's spaceship as an inheriting class of
        # spaceship.
        self.spaceship = spaceship
        # Initialize the image and position of the player spaceship.
        self.player_image=pygame.image.load('assets/space-invaders.png')
        self.player_x=370
        self.player_y=480
        self.player_x_change=0

    def __repr__(self):
        return f'{self.player_x}'

    def player(self,coordinate_x,coordinate_y):
        """
        Display the player on the game screen
        """
        screen.blit(self.spaceship.representation(),(coordinate_x,coordinate_y))

def is_collision(enemy_x,enemy_y,bullet_x,bullet_y):
    """
    Detecting collision between the bullets from the player and the enemy.
    """
    distance=math.sqrt((math.pow
    (enemy_x-bullet_x,2))+(math.pow(enemy_y-bullet_y,2)))
    return distance < 27

def is_killed(enemy_x,enemy_y,player_x,player_y):
    """
    Detecting collision between the bullets from the player and the enemy.
    """
    distance=math.sqrt((math.pow
    (enemy_x-player_x,2))+(math.pow(enemy_y-player_y,2)))
    return distance < 27
