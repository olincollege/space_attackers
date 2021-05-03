
# Import and initialize the pygame library
import pygame
import random
import math

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'

class Spaceship:
    def __init__(self, Img):
        self.Img = pygame.image.load(Img)

    def representation(self):
        """
        Display the player on the game screen
        """
        return self.Img

class Player(Spaceship):
    """
    This class that takes an instance of a Enemy as a parameter and stores it 
    as a private instance attribute.
    """
    def __init__(self, spaceship):
        #PLayer
        self.spaceship = spaceship
        self.playerImg=pygame.image.load('space-invaders.png')
        self.playerX=370
        self.playerY=480
        self.playerX_change=0
        
    def __repr__(self):
        return f'{self.playerX}' 
          
    def player(self,x,y):
        """
        Display the player on the game screen
        """
        
        screen.blit(self.spaceship.representation(),(x,y))


    def isCollision(self,enemyX,enemyY,bulletX,bulletY):
        """
        Detecting collision between the bullets from the player and the enemy
        """
        distance=math.sqrt((math.pow
        (enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
        if distance <27:
            return True
        else:
            return False