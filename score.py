"""
Define the Score class.
"""

# Import and initialize the pygame library
import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])


class Score():
    """
    This class that takes an instance of a Score as a parameter and stores it
    as a private instance attribute.
    """
    font=pygame.font.Font('freesansbold.ttf',32)
    def __init__(self,level):
        global font
        self.score_value=0
        self.text_x=10
        self.level=level
        self.text_y=10

    def __repr__(self):
        return f"{self.score_value}"

    def show_score(self,coordinate_x,coordinate_y):
        """
        Renders the current score of rge game on the game board
        """

        font=pygame.font.Font('freesansbold.ttf',32)
        score=font.render(
            "The level is" + " "+ self.level +" " +
            " and score is : "+ str(self.score_value),True,(255,255,255)
        )
        screen.blit(score,(coordinate_x,coordinate_y))
