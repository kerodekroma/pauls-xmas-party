import pygame

from toolbox import font
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
        self.text_color = self.palette[9]
    
    def render(self, screen, mushroom_name, score):
        pygame.draw.rect(screen, self.color, self.rect)
        text_content = f"""MY SCORE: {score[0]}"""
        font.render_pixel_text(self.pixel_font, (self.unit * 14, self.unit * 2), text_content, self.text_color, screen)

        # ai score
        text_content = f"""{mushroom_name.upper()} SCORE: {score[1]}"""
        font.render_pixel_text(self.pixel_font, (self.screen_width - self.unit * 42, self.unit * 2), text_content, self.text_color, screen)