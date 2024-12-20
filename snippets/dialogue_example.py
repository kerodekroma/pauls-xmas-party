
# python -m snippets.dialogue_example.py
import pygame

from toolbox.dialogue_system import DialogueSystem

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dialogue System Example")

# Load avatars
avatar_img = pygame.image.load("./assets/img/flag32x32.png")
avatar_img = pygame.transform.scale(avatar_img, (64, 64))

avatar_img_b = pygame.image.load("./assets/img/mushroom_01.png")
avatar_img_b = pygame.transform.scale(avatar_img_b, (64, 64))

# Dialogue system instance
dialogue_system = DialogueSystem(WIDTH, HEIGHT)
dialogue_system.set_dialogue([
    {"avatar": avatar_img, "text": "Welcome to the Christmas party!"},
    {"text": "Get ready for a festive night!"},
    {"avatar": avatar_img_b, "text": "Think you can match my memory, Paul? Prove it!"},
    {"avatar": avatar_img_b, "text": "Paul! Before we bring out the Christmas tree, how about a quick game? Let’s see if you’ve been paying attention this year!"}
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
