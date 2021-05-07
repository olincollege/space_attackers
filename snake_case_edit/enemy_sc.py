# Import and initialize the pygame library
import pygame
import random
import math
from spaceship import Spaceship

pygame.init()
screen = pygame.display.set_mode([800, 600])

class Enemy(Spaceship):
    """
    This class that takes an instance of a Enemy as a parameter and stores it 
    as a private instance attribute.
    """
    def __init__(self, spaceship):
        self._spaceship = spaceship
        self._enemy_image=[]
        self.enemy_x=[]
        self.enemy_y=[]
        self._enemy_x_change_value = []
        self.enemy_x_change=[]
        self.enemy_y_change=[]
        self.num_of_enemies=spaceship.enemies
        for i in range(self.num_of_enemies):
            self._enemy_image.append(self._spaceship.representation())
            self.enemy_x.append(random.randint(0,735))
            self.enemy_y.append(random.randint(50,150))
            self.enemy_x_change.append(self._spaceship.enemy_speed[0])
            self.enemy_y_change.append(40)
       

    def enemy(self,x,y,i):
        """
        Display the enemies on the board
        """
       
        screen.blit(self._enemy_image[i],(x,y))
