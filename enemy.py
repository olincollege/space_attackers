# Import and initialize the pygame library
import pygame
import random
import math

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

class Enemy:
    """
    This class that takes an instance of a Enemy as a parameter and stores it 
    as a private instance attribute.
    """
    def __init__(self):
        self.enemyImg=[]
        self.enemyX=[]
        self.enemyY=[]
        self.enemyX_change_value = []
        self.enemyX_change=[]
        self.enemyY_change=[]
        self.num_of_enemies=7
        for i in range(self.num_of_enemies):
            self.enemyImg.append(pygame.image.load('space_invader.png'))
            self.enemyX.append(random.randint(0,735))
            self.enemyY.append(random.randint(50,150))
            self.enemyX_change.append(4)
            self.enemyY_change.append(40)
       

    def enemy(self,x,y,i):
        """
        Display the enemies on the board
        """
        screen.blit(self.enemyImg[i],(x,y))