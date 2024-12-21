# HOW TO RUN THIS SCRIPT IN TERMINAL:
# python -m snippets.fireworks.py

import pygame
import random

from toolbox.firework import Firework

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireworks Display")

# Colors
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60


# Main game loop
fireworks = []
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add new firework occasionally
    if random.random() < 0.02:
        fireworks.append(Firework(WIDTH, HEIGHT))

    # Update and draw fireworks
    for firework in fireworks:
        firework.update()
        firework.draw(screen)

    # Remove finished fireworks
    fireworks = [fw for fw in fireworks if fw.particles or not fw.exploded]

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
