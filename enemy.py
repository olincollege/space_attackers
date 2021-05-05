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
        self.spaceship = spaceship
        self.enemyImg=[]
        self.enemyX=[]
        self.enemyY=[]
        self.enemyX_change_value = []
        self.enemyX_change=[]
        self.enemyY_change=[]
        self.num_of_enemies=spaceship.enemies
        for i in range(self.num_of_enemies):
            self.enemyImg.append(self.spaceship.representation())
            self.enemyX.append(random.randint(0,735))
            self.enemyY.append(random.randint(50,150))
            self.enemyX_change.append(self.spaceship.enemy_speed[0])
            self.enemyY_change.append(40)
       

    def enemy(self,x,y,i):
        """
        Display the enemies on the board
        """
       
        screen.blit(self.enemyImg[i],(x,y))
