"""Boilerplate pygame

Which got me wondering about boilerplate?
https://en.wikipedia.org/wiki/Boilerplate_text
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pygame Template')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock to control the frame rate
clock = pygame.time.Clock()
FPS = 60

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic
    # Update game state here

    # Drawing
    screen.fill(BLACK)  # Fill the screen with black color
    # Draw everything here

    pygame.display.flip()  # Update the full display Surface to the screen

    # Cap the frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()
