import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
       

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        