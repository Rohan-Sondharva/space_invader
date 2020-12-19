import pygame

# Initialize the Pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

# Adding player image and position
playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0


# Drawing Player to Screen
def player(x, y):
    screen.blit(playerImg, (x, y))


running = True

# Game Loop
while running:

    # Fill the screen with RGB color
    screen.fill((0, 0, 0))

    # Loop through all the events in game
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Checks whether the key is pressed or not
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        # Checks whether the key is released or not
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Add new position to PlayerX
    playerX += playerX_change
    player(playerX, playerY)

    pygame.display.update()
