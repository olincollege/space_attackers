"""
Define the Enemy class, inheriting from the Spaceship class.
"""

# Import and initialize the pygame library
import random
import pygame
from spaceship import Spaceship

pygame.init()
screen = pygame.display.set_mode([800, 600])

class Enemy(Spaceship):
    """
    This class takes an instance of spaceship as a parameter and stores it
    as an instance attribute, and has methods to represent the enemies on
    the screen.
    """
    def __init__(self, spaceship):
        self.spaceship = spaceship
        self.enemy_image=[]
        self.enemy_x=[]
        self.enemy_y=[]
        self.enemy_x_change=[]
        self.enemy_y_change=[]
        self.num_of_enemies=spaceship.enemies
        for element in range(self.num_of_enemies):
            self.enemy_image.append(self.spaceship.representation())
            self.enemy_x.append(random.randint(0,735))
            self.enemy_y.append(random.randint(50,150))
            self.enemy_x_change.append(self.spaceship.enemy_speed[0])
            self.enemy_y_change.append(40)


    def enemy(self,coordinate_x,coordinate_y,element):
        """
        Display the enemies on the board.
        """
        screen.blit(self.enemy_image[element],(coordinate_x,coordinate_y))
