import pygame

# Initialize the Pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
