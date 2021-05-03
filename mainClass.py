
# Import and initialize the pygame library
import pygame
import random
import math
from enemy import Enemy
from player import Player
from score import Score
from bullet import Bullets
pygame.init()

def main():
    """
    Play a game of space invaders
    """ 
    # Set up the drawing window
    screen = pygame.display.set_mode([800, 600])

    clock = pygame.time.Clock()
    clock.tick(60)
    #Title and icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('ufo.png')
    pygame.display.set_icon(icon)
    #backgroundimage
    background=pygame.image.load('background.png')
    background = pygame.transform.scale(background, (1000, 700))

    player=Player()
    enemy=Enemy()
    bullet=Bullets()
    score=Score()

    # Run until the user asks to quit
    running = True
    while running:
        # Fill the background with white
        screen.fill((255, 255, 255))
        # Did the user click the window close button?
        # playerX+=0.1
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    player.playerX_change =-2
                if event.key==pygame.K_RIGHT:
                    player.playerX_change =2
                if event.key==pygame.K_SPACE:
                    print("bullet here")
                    if bullet.bullet_state == "ready":
                        bullet.bulletX = player.playerX
                        bullet.fire_bullet(bullet.bulletX,bullet.bulletY)

            if event.type== pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                   player.playerX_change =0
            
                
        #checking for boundaries of spaceship so that ir doesnt go out of bounds
        player.playerX+=player.playerX_change
        if player.playerX<=0:
           player.playerX=0
        elif player.playerX>=736:
            player.playerX=736
        #enemy mobement
        for i in range(enemy.num_of_enemies):
            enemy.enemyX[i] += enemy.enemyX_change[i]
            if enemy.enemyX[i]<=0:
                enemy.enemyX_change[i]=4
                enemy.enemyY[i]+=enemy.enemyY_change[i]
            elif enemy.enemyX[i]>=736:
                enemy.enemyX_change[i]=-4
                enemy.enemyY[i]+=enemy.enemyY_change[i]

            #Collision
            collision=player.isCollision(enemy.enemyX[i],enemy.enemyY[i],bullet.bulletX,bullet.bulletY)
            if collision:
                print("collision happened")
                bullet.bulletY=480
                bullet.bullet_state="ready"
                score.score_value+=1
                print(score.score_value)
                enemy.enemyX[i]=900
                enemy.enemyY[i]=250
                # enemy.enemyX[i]=random.randint(0,735)
                # enemy.enemyY[i]=random.randint(50,150)
                

            enemy.enemy(enemy.enemyX[i],enemy.enemyY[i],i)

        # # # Bullet Movement
        if bullet.bulletY <= 0:
            bullet.bulletY = 480
            bullet.bullet_state = "ready" 
        if bullet.bullet_state is "fire":
            print("bullet_state",bullet.bullet_state)
            bullet.fire_bullet(bullet.bulletX,bullet.bulletY)
            bullet.bulletY-=bullet.bulletY_change
        
    

        player.player(player.playerX,player.playerY)
        score.show_score(score.textX,score.textY)
        # Flip the display
        pygame.display.update()


      # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    main()


        