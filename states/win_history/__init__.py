import pygame

from toolbox import game_state
from toolbox import singl_button
from toolbox.dialogue_system import DialogueSystem
from toolbox.image_transition import ImageTransition

from states import GAME_STATES

PY_SINGLE_BUTTON_Events = singl_button.PY_SINGLE_BUTTON_Events

class WinHistoryState(game_state.GameState):
    def __init__(self, state_manager):
        super().__init__(state_manager=state_manager)
        self.setup(state_manager)

    def setup(self, state_manager):
        self.settings = state_manager.settings
        self.unit = self.settings.UNIT
        self.current_level = self.settings.game_data['level'] 
        self.is_last_level_completed = self.current_level == self.settings.game_data['max_level']
        self.image_transition = ImageTransition(60)

        # dialog
        self.dialog = DialogueSystem(
            self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        dialogs = []

        if not self.is_last_level_completed:
            self.current_mushroom = self.settings.mushroom_by_level(self.current_level - 1)
            self.current_bg = pygame.image.load(self.settings.bg_by_level(self.current_level - 1))
            self.next_bg = pygame.image.load(self.settings.bg_by_level(self.current_level))

            self.image_transition.start_transition(
                self.current_bg,
                self.next_bg,
            )

            self.dialog.avatar = self.dialog.prepare_avatar(self.current_mushroom["img"])
            dialogs = [
                *self.settings.get_dialogue_by_level(self.current_level - 1)['post'],
            ]

        if self.is_last_level_completed:
            self.current_mushroom = self.settings.mushroom_by_level(self.current_level - 1)
            self.dialog.avatar = self.dialog.prepare_avatar(self.current_mushroom["img"])
            self.current_bg = pygame.image.load(self.settings.bg_by_level(self.current_level))
            self.next_bg = pygame.image.load(self.settings.bg_by_level())
            self.image_transition.start_transition(
                self.current_bg,
                self.next_bg,
            )
            dialogs = [
                *self.settings.get_dialogue_by_level(self.current_level - 1)['post'],
                {"text": "Thanks for playing :D"}
            ]
        
        self.dialog.set_dialogue(dialogs)

    def handle_events(self, event, state_manager):
        # debug
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE and state_manager.current_state_name == GAME_STATES.WIN_HISTORY:
        #             state_manager.set_state(GAME_STATES.GAMEPLAY)
        
        self.dialog.handle_event(event)

    def render(self, screen, state_manager):
        # pixel_font = self.settings.font['pixel']
        # palette = state_manager.settings.palette
        # text_content = f"""
        #     Win History here, press space to continue {self.current_level}
        # """
        # text_surface = pixel_font.render(text_content, True, palette[8])
        # text_rect = text_surface.get_rect(center=(state_manager.settings.WINDOW_WIDTH/2, 50))
        # screen.blit(text_surface, text_rect)
        self.image_transition.update()
        if not self.image_transition.transitioning:
            self.current_bg = self.next_bg
        self.image_transition.render(screen)

        self.dialog.update(screen)

        if not self.dialog.show_dialogue and not self.is_last_level_completed:
            state_manager.set_state(GAME_STATES.GAMEPLAY)
