import pygame

from toolbox import game_state
from toolbox import singl_button

PY_SINGLE_BUTTON_Events = singl_button.PY_SINGLE_BUTTON_Events

class WinHistoryState(game_state.GameState):
    def __init__(self, state_manager):
        super().__init__(state_manager=state_manager)
        self.settings = state_manager.settings
        self.unit = self.settings.UNIT

    def handle_events(self, event, state_manager):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and state_manager.current_state_name == 'main_menu':
                state_manager.set_state('gameplay')

    def render(self, screen, state_manager):
        pixel_font = self.settings.font['pixel']
        palette = state_manager.settings.palette
        text_content = f"""
            Win History here
        """
        text_surface = pixel_font.render(text_content, True, palette[8])
        text_rect = text_surface.get_rect(center=(state_manager.settings.WINDOW_WIDTH/2, 50))
        screen.blit(text_surface, text_rect)