
# Import and initialize the pygame library
import pygame
import random
import math

pygame.init()

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



class Enemy:
    def __init__(self):
        self.enemyImg=[]
        self.enemyX=[]
        self.enemyY=[]
        self.enemyX_change_value = []
        self.enemyX_change=[]
        self.enemyY_change=[]
        self.num_of_enemies=7
        for i in range(self.num_of_enemies):
            self.enemyImg.append(pygame.image.load('space_invader.png'))
            self.enemyX.append(random.randint(0,735))
            self.enemyY.append(random.randint(50,150))
            # enemyX_change_value.append(1)
            self.enemyX_change.append(4)
            self.enemyY_change.append(40)
       

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def enemy(self,x,y,i):
        screen.blit(self.enemyImg[i],(x,y))


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player:
    def __init__(self):
        #PLayer
        self.playerImg=pygame.image.load('space-invaders.png')
        self.playerX=370
        self.playerY=480
        self.playerX_change=0
        
    def __repr__(self):
        return f'{self.playerX}' 
          
    def player(self,x,y):
        screen.blit(self.playerImg,(x,y))

    def fire_bullet(self,x,y):
        global bullet_state
        bullet=Bullets()
        bullet.bullet_state="fire"
        screen.blit(bullet.bulletImg,(x+16,y+10 ))

    def isCollision(self,enemyX,enemyY,bulletX,bulletY):
        distance=math.sqrt((math.pow
        (enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
        if distance <27:
            return True
        else:
            return False
        

class Bullets:
    def __init__(self):
        self.bulletImg=pygame.image.load('bullet.png')
        self.bulletX=0
        self.bulletY=480
        self.bulletX_change=0
        self.bulletY_change=2
        self.bullet_state="ready"
        self.font=pygame.font.Font('freesansbold.ttf',32)
        self.textX=10
        self.textY=10
    

    def fire_bullet(self,x,y):
        global bullet_state
        self.bullet_state="fire"
        screen.blit(self.bulletImg,(x+16,y+10 ))
        
 
class Score():
    font=pygame.font.Font('freesansbold.ttf',32)
    def __init__(self):
        global font 
        self.score_value=0
        self.textX=10
        self.textY=10

    def show_score(self,x,y):
        font=pygame.font.Font('freesansbold.ttf',32)
        score=font.render("Score : "+ str(self.score_value),True,(255,255,255))
        screen.blit(score,(x,y))



player=Player()
enemy=Enemy()
bullet=Bullets()
score=Score()
print(player)
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
            
            enemy.enemyX[i]=random.randint(0,735)
            enemy.enemyY[i]=random.randint(50,150)
            

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

        