import pygame

class GamePlayHeader():
    def __init__(self, state_manager, size, position, color):
        self.size = size
        self.position = position
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

        settings = state_manager.settings
        self.unit = settings.UNIT
        self.screen_width = settings.WINDOW_WIDTH
        self.palette = settings.palette
        self.pixel_font = settings.font['pixel']

    def render(self, screen, score):
        pygame.draw.rect(screen, self.color, self.rect)

        print("score", score)
        # player score
        text_content = f"""
            SCORE: {score[0]}
        """
        text_surface = self.pixel_font.render(text_content, True, self.palette[2])
        text_rect = text_surface.get_rect(topleft=(self.unit, 50))

        # ai score
        text_content = f"""
            AI: {score[1]}
        """
        text_surface = self.pixel_font.render(text_content, True, self.palette[2])
        text_rect = text_surface.get_rect(topleft=(self.unit, self.screen_width - self.unit))

        screen.blit(text_surface, text_rect)