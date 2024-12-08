import pygame

class GamePlayHeader():
    def __init__(self, size, position, color):
        self.size = size
        self.position = position
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)