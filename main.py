
# Import and initialize the pygame library
import pygame
import random
# Simple pygame program
# from enemy import Enemy
# from player import Player



# enemy=Enemy()
# player=Player()
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])
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
enemyImg=pygame.image.load('enemy.png')
enemyX=random.randint(0,800)
enemyY=random.randint(50,150)
enemyX_change=2
enemyY_change=40

#Bullets
#Ready-bullet is not yet been dispatched
#FIre-bullet has been fired
bulletImg=pygame.image.load('enemy.png')
bulletX=0
bulletY=480
bulletX_change=4
bulletY_change=40
bullet_state="ready"

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    print("pressed")
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10 ))

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
                playerX_change =-0.3
            if event.key==pygame.K_RIGHT:
               playerX_change =0.3
            if event.key==pygame.K_SPACE:
               fire_bullet(playerX,bulletY)

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
    enemyX+=enemyX_change
    if enemyX<=0:
        enemyX_change=2
        enemyY+=enemyY_change
    elif enemyX>=736:
         enemyX_change=-2
         enemyY+=enemyY_change

    # # BUllet Movement
    if bullet_state is "fire":
       fire_bullet(playerX,bulletY)
       bulletY-=bulletY_change

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    # Flip the display
    pygame.display.update()


# Done! Time to quit.
pygame.quit()