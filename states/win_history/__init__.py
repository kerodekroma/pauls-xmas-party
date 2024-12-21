import pygame
import random

from toolbox import game_state
from toolbox import singl_button
from toolbox.dialogue_system import DialogueSystem
from toolbox.image_transition import ImageTransition
from toolbox.firework import Firework

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
        # self.is_last_level_completed = self.current_level == self.settings.game_data['max_level']
        self.is_last_level_completed = True
        self.image_transition = ImageTransition(60)

        # FINAL SCREEN
        self.image_ty = pygame.image.load(self.settings.BG_THANKS)
        self.default_btn_bg_color = self.settings.palette[62]
        self.restart_btn = singl_button.SinglSquareButton(
            (self.settings.WINDOW_WIDTH // 2 - self.unit * 25, self.unit * 60),
            {
                "height": self.unit * 8,
                "width": self.unit * 50,
                "bg_color": self.default_btn_bg_color,
                "text_color": self.settings.palette[22],
                "text": "PLAY AGAIN [CLICK HERE]"
            }
        )
        self.fireworks = []
        self.is_pressed_restart = False

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

        if not self.dialog.show_dialogue and self.is_last_level_completed:
            self.restart_btn.listen_events(event)

    def render_ending(self, screen, state_manager):
        settings = state_manager.settings
        palette = settings.palette
        screen.blit(self.image_ty, (0, 0))

        if self.restart_btn.current_event == PY_SINGLE_BUTTON_Events.PRESSED:
            self.restart_btn.options['bg_color'] = palette[30]
            self.restart_btn.options["text_color"] = self.default_btn_bg_color

            # restart and go the level 0
            state_manager.settings.game_data["level"] = 0
            state_manager.set_state(GAME_STATES.GAMEPLAY)

        if self.restart_btn.current_event == PY_SINGLE_BUTTON_Events.RELEASED:
            self.restart_btn.options['bg_color'] = self.default_btn_bg_color
            self.restart_btn.options["text_color"] = palette[30]

        self.restart_btn.render(screen)


    def render(self, screen, state_manager):
        settings = state_manager.settings
        self.image_transition.update()
        if not self.image_transition.transitioning:
            self.current_bg = self.next_bg
        self.image_transition.render(screen)

        self.dialog.update(screen)

        if not self.dialog.show_dialogue and self.is_last_level_completed:
            self.render_ending(screen, state_manager)
            # Add new firework occasionally
            if random.random() < 0.02:
                self.fireworks.append(Firework(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

            # Update and draw fireworks
            for firework in self.fireworks:
                firework.update()
                firework.draw(screen)


        if not self.dialog.show_dialogue and not self.is_last_level_completed:
            state_manager.set_state(GAME_STATES.GAMEPLAY)
