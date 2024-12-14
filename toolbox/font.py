import pygame

def pixel_font(size=32):
    font = pygame.font.Font('./assets/font/PixelSimpel.otf', size)
    return font


def render_pixel_text(font_instance, pos, text, color, screen):
    text_surface = font_instance.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=pos)
    screen.blit(text_surface, text_rect)