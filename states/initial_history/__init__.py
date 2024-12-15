import pygame

from toolbox import game_state
from toolbox import singl_button

from states import GAME_STATES

PY_SINGLE_BUTTON_Events = singl_button.PY_SINGLE_BUTTON_Events

class InitialHistoryState(game_state.GameState):
    def __init__(self, state_manager):
        super().__init__(state_manager=state_manager)
        self.settings = state_manager.settings
        self.unit = self.settings.UNIT
        self.skip_btn = singl_button.SinglSquareButton(
            (self.settings.WINDOW_WIDTH // 2 - self.unit * 2, self.unit * 50),
            {
                "height": self.unit * 4,
                "bg_color": self.settings.palette[63],
                "text_color": self.settings.palette[30],
                "text": "SKIP [space bar]"
            }
        )

    def handle_events(self, event, state_manager):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and state_manager.current_state_name == GAME_STATES.INIT_HISTORY:
                state_manager.set_state(GAME_STATES.PICK_PLAYER)

        self.skip_btn.listen_events(event)

    def render(self, screen, state_manager):
        pixel_font = self.settings.font['pixel']
        palette = state_manager.settings.palette
        text_content = f"""
            HISTORY HERE
        """
        text_surface = pixel_font.render(text_content, True, palette[8])
        text_rect = text_surface.get_rect(center=(state_manager.settings.WINDOW_WIDTH/2, 50))
        screen.blit(text_surface, text_rect)

        if self.skip_btn.current_event == PY_SINGLE_BUTTON_Events.PRESSED:
            self.skip_btn.options['bg_color'] = palette[30]
            self.skip_btn.options["text_color"] = palette[63]
            state_manager.set_state(GAME_STATES.PICK_PLAYER)

        if self.skip_btn.current_event == PY_SINGLE_BUTTON_Events.RELEASED:
            self.skip_btn.options['bg_color'] = palette[63]
            self.skip_btn.options["text_color"] = palette[30]

        self.skip_btn.render(screen)

