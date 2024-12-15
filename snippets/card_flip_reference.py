# python -m snippets.card_flip_reference.py
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Card Flip")
clock = pygame.time.Clock()
FPS = 60


# Card example
img_card_back = './assets/img/card_back.png'
img_card_front = './assets/img/card_front.png'

# Load images
front_image = pygame.image.load(img_card_front).convert_alpha()
back_image = pygame.image.load(img_card_back).convert_alpha()

# Resize images
CARD_WIDTH, CARD_HEIGHT = 200, 300
front_image = pygame.transform.scale(front_image, (CARD_WIDTH, CARD_HEIGHT))
back_image = pygame.transform.scale(back_image, (CARD_WIDTH, CARD_HEIGHT))

# Card properties
card_rect = front_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
flip_angle = 0  # Start angle of the card
is_flipping = False
is_flipped = False  # Tracks whether the card is showing the back

# Flip duration and timing
FLIP_DURATION = 1000  # milliseconds
start_time = 0


def draw_card(angle, flipped):
    """Draw the card with a 3D flip effect."""
    # Calculate the scaling and perspective effect
    scale = abs(math.cos(math.radians(angle)))  # Scale based on angle
    scaled_width = max(1, int(CARD_WIDTH * scale))  # Avoid zero width

    # Determine which image to display
    if angle > 90:
        current_image = front_image if flipped else back_image
    else:
        current_image = back_image if flipped else front_image

    # Scale the image
    scaled_image = pygame.transform.scale(
        current_image, (scaled_width, CARD_HEIGHT))
    scaled_rect = scaled_image.get_rect(center=card_rect.center)

    # Draw the card
    screen.blit(scaled_image, scaled_rect)

# EXP: https://www.reddit.com/r/pygame/comments/z571pa/this_is_how_you_can_texture_a_polygon/


def lerp(p1, p2, f):
    return p1 + f * (p2 - p1)


def lerp2d(p1, p2, f):
    return tuple(lerp(p1[i], p2[i], f) for i in range(2))


def draw_quad(surface, quad, img):
    points = dict()
    for i in range(img.get_size()[1]+1):
        b = lerp2d(quad[1], quad[2], i/img.get_size()[1])
        c = lerp2d(quad[0], quad[3], i/img.get_size()[1])
        for u in range(img.get_size()[0]+1):
            a = lerp2d(c, b, u/img.get_size()[0])
            points[(u, i)] = a

    for x in range(img.get_size()[0]):
        for y in range(img.get_size()[1]):
            pygame.draw.polygon(
                surface,
                img.get_at((x, y)),
                [points[(a, b)]
                 for a, b in [(x, y), (x, y+1), (x+1, y+1), (x+1, y)]]
            )


running = True

while running:
    screen.fill((30, 30, 30))  # Background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not is_flipping:
            # Start flipping the card
            is_flipping = True
            start_time = pygame.time.get_ticks()

    if is_flipping:
        # Update the flip angle
        elapsed_time = pygame.time.get_ticks() - start_time
        flip_angle = (elapsed_time / FLIP_DURATION) * 180

        if flip_angle >= 180:
            is_flipping = False
            is_flipped = not is_flipped  # Toggle flipped state

    # Draw the card
    draw_card(flip_angle if is_flipping else (
        180 if is_flipped else 180), is_flipped)

    draw_quad(screen, ((300, 300), (600, 450),
              (600, 600), (400, 600)), front_image)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
