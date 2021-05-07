
# Import and initialize the pygame library
import pygame
import random
import math
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])
class Bullets:
    """
    This class that takes an instance of a Enemy as a parameter and stores it 
    as a private instance attribute.
    """
    def __init__(self):
        self._bullet_image=pygame.image.load('assets/bullet.png')
        self._explosion_image=pygame.image.load('assets/explosion.png')
        self.bullet_x=0
        self.bullet_y=480
        self._bullet_x_change=0
        self.bullet_y_change=4
        self.bullet_state="ready"
        self._font=pygame.font.Font('freesansbold.ttf',32)
        self._text_x=10
        self._text_y=10
    

    def fire_bullet(self,x,y):
        """
        Triggers the firing of the bullet from the player to initiate collision with the enemy
        """
        global bullet_state
        self.bullet_state="fire"
        screen.blit(self._bullet_image,(x+16,y+10 ))

    def explosion(self,x,y):
        print(x,y)
        screen.blit(self._explosion_image,(x,y))
