import pygame

# Initialize the Pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

# Adding player image
playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 480

# Drawing Player to Screen
def player():
    screen.blit(playerImg, (playerX, playerY))


# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
