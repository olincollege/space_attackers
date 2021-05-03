# Import and initialize the pygame library
import pygame
import random
import math

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

class Score():
    """
    This class that takes an instance of a Score as a parameter and stores it 
    as a private instance attribute.
    """
    font=pygame.font.Font('freesansbold.ttf',32)
    def __init__(self):
        global font 
        self.score_value=0
        self.textX=10
        self.textY=10

    def show_score(self,x,y):
        """
        Renders the current score of rge game on the game board
        """
        font=pygame.font.Font('freesansbold.ttf',32)
        score=font.render("Score : "+ str(self.score_value),True,(255,255,255))
        screen.blit(score,(x,y))
