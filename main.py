
# Import and initialize the pygame library
import pygame
import random
import math
# Simple pygame program
# from enemy import Enemy
# from player import Player



# enemy=Enemy()
# player=Player()
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


#PLayer
playerImg=pygame.image.load('space-invaders.png')
playerX=370
playerY=480
playerX_change=0

#Enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change_value = []
enemyX_change=[]
enemyY_change=[]
num_of_enemies=7
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    # enemyX_change_value.append(1)
    enemyX_change.append(4)
    enemyY_change.append(40)

#Bullets
#Ready-bullet is not yet been dispatched
#FIre-bullet has been fired
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=2
bullet_state="ready"
score=0
def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def has_Collided(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10 ))
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow
    (enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance <27:
        return True
    else:
        return False
# def changeEnemyPosition():
    
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
                playerX_change =-2
            if event.key==pygame.K_RIGHT:
                playerX_change =2
            if event.key==pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type== pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
               playerX_change =0
           
            
    #checking for boundaries of spaceship so that ir doesnt go out of bounds
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    #enemy mobement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=4
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-4
            enemyY[i]+=enemyY_change[i]

         #Collision
        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            print("collision happened")
            bulletY=480
            bullet_state="ready"
            score+=1
            print(score)
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)

    # # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    
   

    player(playerX,playerY)
    
    # Flip the display
    pygame.display.update()


# Done! Time to quit.
pygame.quit()