# python -m snippets.card_flip.py
import pygame

from toolbox.card import SpriteCard

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Flip")

# Card example
img_card_back = './assets/img/card_back.png'
img_card_front = './assets/img/card_front.png'

single_card = SpriteCard(img_card_front, img_card_back, (50, 50), '0')
cards = [single_card]
cards_group = pygame.sprite.Group(cards)

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()

                # check for card click using collision detection
                for index, card in enumerate(cards):
                    if card.rect.collidepoint(pos) and not card.is_flipped:
                        card.animated_flip()
                        break

    # Update and draw dialogue
    cards_group.update()
    cards_group.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
