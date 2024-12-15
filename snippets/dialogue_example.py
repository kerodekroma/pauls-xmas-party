
# python -m snippets.dialogue_example.py
import pygame

from toolbox.dialogue_system import DialogueSystem

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dialogue System Example")

# Load avatar
avatar_img = pygame.image.load("./assets/img/flag32x32.png")
avatar_img = pygame.transform.scale(avatar_img, (64, 64))

# Dialogue system instance
dialogue_system = DialogueSystem(WIDTH, HEIGHT)
dialogue_system.set_dialogue([
    {"avatar": "avatar.png", "text": "Welcome to the Christmas party!"},
    {"avatar": "avatar.png", "text": "Get ready for a festive night!"}
])
dialogue_system.avatar = avatar_img  # Set avatar

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear the screen

    # Update and draw dialogue
    dialogue_system.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        dialogue_system.handle_event(event)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
