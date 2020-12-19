import math
import random

import pygame

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assets/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(10)

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
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Position of Scoreboard
textX = 10
textY = 10


# Show the score to screen
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Drawing Player to Screen
def player(x, y):
    screen.blit(playerImg, (x, y))


# Drawing enemy to Screen
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Change the bullet state to Fire
def fire_bullet(x, y):
    # Making variable global
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


# Check Whether bullet is hit to enemy
def is_Collision(enemyX, enemyY, bulletX, bulletY):
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

    for i in range(num_of_enemies):
        # Add new position to Enemy
        enemyX[i] += enemyX_change[i]

        # Change direction of enemy when hit to boundary
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]  # Move Enemy Down
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]  # Move Enemy Down

        # Collision
        collision = is_Collision(enemyX[i], enemyY[i], bulletX, bulletY)

        # Respawn enemy when being hit and increase score
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Reset bullet to original position after shot
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    # Bullet Movement
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)

    # Updating the Game Screen
    pygame.display.update()
