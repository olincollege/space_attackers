
# Import and initialize the pygame library
import pygame
import random
import math
from enemy import Enemy
from player import Player, Spaceship
from score import Score
from bullet import Bullets
pygame.init()

def main():
    """
    Play a game of space invaders.
    """
    level=input("At what level of difficulty would you like to play? (easy,medium,hard)")
    
    screen = pygame.display.set_mode([800, 600])
    # Set up the drawing window

    clock = pygame.time.Clock()
    clock.tick(60)
    # #Title and icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('assets/space-invaders.png')
    pygame.display.set_icon(icon)

    ## Game level
    enemies=0
    speed=0
    if level=="easy":
        enemies=8
        speed=1
    elif level=="medium":
        enemies=13
        speed=2
    else:
        enemies=20
        speed=5
    #backgroundimage
    background=pygame.image.load('assets/background.png')
    background = pygame.transform.scale(background, (1000, 700))
    enemy_spaceship = Spaceship('assets/space_invader.png',speed,enemies)
    player_spaceship = Spaceship('assets/space-invaders.png',speed,enemies)
    print(enemy_spaceship)
    player=Player(player_spaceship)
    enemy=Enemy(enemy_spaceship)
    bullet=Bullets()
    score=Score(level)
    print("SCORE",score)
   

   # Run until the user asks to quit
    running = True
    while running:
        # Fill the background with white
        screen.fill((255, 255, 255))
        # Did the user click the window close button?

        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    player.player_x_change =-2
                if event.key==pygame.K_RIGHT:
                    player.player_x_change =2
                if event.key==pygame.K_SPACE:
                   
                    if bullet.bullet_state == "ready":
                        bullet.bullet_x = player.player_x
                        bullet.fire_bullet(bullet.bullet_x,bullet.bullet_y)

            if event.type== pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                   player.player_x_change =0
            
                
        #checking for boundaries of spaceship so that ir doesnt go out of bounds
        player.player_x+=player.player_x_change
        if player.player_x<=0:
           player.player_x=0
        elif player.player_x>=736:
            player.player_x=736
        #enemy movement
        for i in range(enemy.num_of_enemies):
            enemy.enemy_x[i] += enemy.enemy_x_change[i]
            if enemy.enemy_x[i]<=0:
                enemy.enemy_x_change[i]=speed
                enemy.enemy_y[i]+=enemy.enemy_y_change[i]
            elif enemy.enemy_x[i]>=736:
                enemy.enemy_x_change[i]=-speed
                enemy.enemy_y[i]+=enemy.enemy_y_change[i]

            #Collision and player killed
            collision=player.isCollision(enemy.enemy_x[i],enemy.enemy_y[i],bullet.bullet_x,bullet.bullet_y)
            killed=player.isKilled(enemy.enemy_x[i],enemy.enemy_y[i],player.player_x,player.player_x) 
            if collision:
                print("collision happened")
                bullet.bullet_y=480
                bullet.bullet_state="ready"
                score.score_value+=1
                bullet.explosion(random.randint(100,735),random.randint(50,150))
                enemy.enemy_x[i]=900
                enemy.enemy_y[i]=450
   
            #CHeck if player has been killed
            if killed:
               print(killed)
               running = False 

            enemy.enemy(enemy.enemy_x[i],enemy.enemy_y[i],i)
    

        # # # Bullet Movement
        if bullet.bullet_y <= 0:
            bullet.bullet_y = 480
            bullet.bullet_state = "ready" 
        if bullet.bullet_state is "fire":
            bullet.fire_bullet(bullet.bullet_x,bullet.bullet_y)
            bullet.bullet_y-=bullet.bullet_y_change
        
        
        
        player.player(player.player_x,player.player_y)
        #show the score as game is played
        score.show_score(score.text_x,score.text_y)
        #if player has killed six enemies generage new ones
        if score.score_value %8 ==0:
           print("score-val")
           enemy_spaceship = Spaceship('assets/space_invader.png',speed,enemies)
           enemy=Enemy(enemy_spaceship)

        # Flip the display
        pygame.display.update()


      #Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    main()


        