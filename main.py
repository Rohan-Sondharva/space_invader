import pygame
import math
import random

# Initialize the Pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Loading Background Image
background = pygame.image.load('assets/background.png')

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

# Adding player image and position
playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Adding enemy image and position
enemyImg = pygame.image.load('assets/enemy.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 10

# Adding bullet image and position
# Ready - You can't see the Bullet
# Fire - You can see the bullet and it is moving
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 20
bullet_state = 'ready'

# Score Variable that count how many time you hit enemy
score = 0

# Drawing Player to Screen
def player(x, y):
    screen.blit(playerImg, (x, y))


# Drawing enemy to Screen
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Change the bullet state to Fire
def fire_bullet(x, y):
    # Making variable global
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def Is_Collision(enemyX, enemyy, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True

# Game Loop
while running:

    # Fill the screen with RGB color
    screen.fill((0, 0, 0))

    # Adding Background
    screen.blit(background, (0, 0))

    # Loop through all the events in game
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Checks whether the key is pressed or not
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                # Only fires bullet when state is ready
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        # Checks whether the key is released or not
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Add new position to PlayerX
    playerX += playerX_change

    # Stop the spaceship to go beyond screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Add new position to Enemy
    enemyX += enemyX_change

    # Change direction of enemy when hit to boundary
    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change  # Move Enemy Down
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change  # Move Enemy Down

    # Reset bullet to original position after shot
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    # Bullet Movement
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = Is_Collision(enemyX, enemyY, bulletX, bulletY)

    # Respawn enemy when being hit and increase score
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # Updating the Game Screen
    pygame.display.update()
