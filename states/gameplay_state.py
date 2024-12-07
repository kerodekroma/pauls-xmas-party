import pygame
import math

from toolbox import game_state

class GamePlayState(game_state.GameState):
    def __init__(self, state_manager):
        super().__init__(state_manager=state_manager)
        settings = state_manager.settings
        palette = settings['palette']
        self.angle = 0

    def handle_events(self, event, state_manager):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and state_manager.current_state_name == 'game_play':
                state_manager.set_state('main_menu')

        mouse_pos = pygame.mouse.get_pos()

    def render(self, screen, state_manager):
        palette = state_manager.settings['palette']
        screen.fill(palette[8])
        pixel_font = state_manager.settings['font']['pixel']
        text_content = f"""
            Let's play! {self.angle}
        """
        text_surface = pixel_font.render(text_content, True, palette[2])
        text_rect = text_surface.get_rect(center=(200, 50))
        screen.blit(text_surface, text_rect)