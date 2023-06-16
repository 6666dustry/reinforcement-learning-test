import pygame
import random
from game import Game

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

# Create a game instance
game = Game(width, height)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game
    game.update()

    # Clear the screen
    screen.fill(game.get_background_color())

    # Draw the game objects
    game.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
