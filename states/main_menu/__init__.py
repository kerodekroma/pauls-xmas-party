import pygame

from toolbox import game_state
from toolbox import singl_button
from states import GAME_STATES

PY_SINGLE_BUTTON_Events = singl_button.PY_SINGLE_BUTTON_Events

class MainMenuState(game_state.GameState):
    def __init__(self, state_manager):
        super().__init__(state_manager=state_manager)
        self.settings = state_manager.settings
        self.unit = self.settings.UNIT
        self.default_btn_bg_color = self.settings.palette[62]
        self.start_btn = singl_button.SinglSquareButton(
            (self.settings.WINDOW_WIDTH // 2 - self.unit * 10, self.unit * 60),
            {
                "height": self.unit * 8,
                "width": self.unit * 20,
                "bg_color": self.default_btn_bg_color,
                "text_color": self.settings.palette[22],
                "text": "START"
            }
        )
        self.is_pressed_start = False
        self.intro_image = pygame.image.load( self.settings.IMG_INTRO )

    def handle_events(self, event, state_manager):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN and state_manager.current_state_name == GAME_STATES.MAIN_MENU:
                state_manager.set_state(GAME_STATES.GAMEPLAY)

        self.start_btn.listen_events(event)

    def render(self, screen, state_manager):
        palette = state_manager.settings.palette
        screen.blit(self.intro_image, (0, 0))

        if self.start_btn.current_event == PY_SINGLE_BUTTON_Events.PRESSED:
            self.start_btn.options['bg_color'] = palette[30]
            self.start_btn.options["text_color"] = self.default_btn_bg_color
            state_manager.set_state(GAME_STATES.GAMEPLAY)

        if self.start_btn.current_event == PY_SINGLE_BUTTON_Events.RELEASED:
            self.start_btn.options['bg_color'] = self.default_btn_bg_color
            self.start_btn.options["text_color"] = palette[30]

        self.start_btn.render(screen)

