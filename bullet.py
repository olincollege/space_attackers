"""
Define the Bullets class.
"""

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])
class Bullets:
    """
    This class that takes an instance of a Enemy as a parameter and stores it 
    as a private instance attribute.
    """
    def __init__(self):
        self.bullet_image=pygame.image.load('assets/bullet.png')
        self.explosion_image=pygame.image.load('assets/explosion.png')
        self.bullet_x=0
        self.bullet_y=480
        self.bullet_x_change=0
        self.bullet_y_change=4
        self.bullet_state="ready"
        self.font=pygame.font.Font('freesansbold.ttf',32)
        self.text_x=10
        self.text_y=10

    def fire_bullet(self,coordinate_x,coordinate_y):
        """
        Triggers the firing of the bullet from the player to initiate collision with the enemy
        """
        global bullet_state
        self.bullet_state="fire"
        screen.blit(self.bullet_image,(coordinate_x+16,coordinate_y+10 ))

    def explosion(self,coordinate_x,coordinate_y):
        print(coordinate_x,coordinate_y)
        screen.blit(self.explosion_image,(coordinate_x,coordinate_y))
