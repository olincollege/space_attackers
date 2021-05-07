
# Import and initialize the pygame library
import pygame
import random
import math
from spaceship import Spaceship
pygame.init()



screen = pygame.display.set_mode([800, 600])

class Player(Spaceship):
    """
    This class that takes an instance of a Enemy as a parameter and stores it 
    as a private instance attribute.
    """
    def __init__(self, spaceship):
        #PLayer'
        # Set up the drawing window
        
        self._spaceship = spaceship
        self._player_image=pygame.image.load('assets/space-invaders.png')
        self.player_x=370
        self.player_y=480
        self.player_x_change=0
        
    def __repr__(self):
        return f'{self.player_x}' 
          
    def player(self,x,y):
        """
        Display the player on the game screen
        """
        
        screen.blit(self._spaceship.representation(),(x,y))


    def isCollision(self,enemy_x,enemy_y,bullet_x,bullet_y):
        """
        Detecting collision between the bullets from the player and the enemy
        """
        distance=math.sqrt((math.pow
        (enemy_x-bullet_x,2))+(math.pow(enemy_y-bullet_y,2)))
        if distance <27:
            return True
        else:
            return False
    
    def isKilled(self,enemy_x,enemy_y,player_x,player_y):
        """
        Detecting collision between the bullets from the player and the enemy
        """
        distance=math.sqrt((math.pow
        (enemy_x-player_x,2))+(math.pow(enemy_y-player_y,2)))
        if distance <27:
            return True
        else:
            return False
    