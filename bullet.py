
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
        self.bulletImg=pygame.image.load('assets/bullet.png')
        self.explosionImg=pygame.image.load('assets/explosion.png')
        self.bulletX=0
        self.bulletY=480
        self.bulletX_change=0
        self.bulletY_change=4
        self.bullet_state="ready"
        self.font=pygame.font.Font('freesansbold.ttf',32)
        self.textX=10
        self.textY=10
    

    def fire_bullet(self,x,y):
        """
        Triggers the firing of the bullet from the player to initiate collision with the enemy
        """
        global bullet_state
        self.bullet_state="fire"
        screen.blit(self.bulletImg,(x+16,y+10 ))

    def explosion(self,x,y):
        print(x,y)
        screen.blit(self.explosionImg,(x,y ))
