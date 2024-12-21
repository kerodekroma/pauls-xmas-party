
import pygame

from toolbox import game_state
from toolbox.dialogue_system import DialogueSystem

from states.gameplay.header import GamePlayHeader
from states.gameplay.board_of_cards import GamePlayBoardOfCards

from states import GAME_STATES


class GamePlayState(game_state.GameState):
    def __init__(self, state_manager):
        super().__init__(state_manager=state_manager)
        self.setup(state_manager)

    def setup(self, state_manager):
        self.settings = state_manager.settings
        self.current_level = self.settings.game_data['level'] 
        self.is_all_levels_win = self.settings.game_data['level'] >= self.settings.game_data['max_level']
        unit = self.settings.UNIT
        self.palette = self.settings.palette
        self.angle = 0
        self.header = GamePlayHeader(
            state_manager,
            (self.settings.WINDOW_WIDTH, 6 * unit),
            (0, 0),
            self.palette[52]
        )
        self.board = GamePlayBoardOfCards(
            (self.settings.WINDOW_WIDTH, 10), (0, self.settings.HEADER_HEIGHT), self.settings)

        # bg level image
        self.bg_level_image = pygame.image.load(self.settings.bg_by_level(self.current_level))

        # mushroom
        self.mushroom = self.settings.mushroom_by_level(self.current_level)

        # dialogs
        # intro
        self.mushroom_intro = self.settings.mushroom_by_level(self.current_level)
        self.dialog_intro = DialogueSystem(
            self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT
        )
        self.dialog_intro.set_dialogue(self.settings.get_dialogue_by_level(self.current_level)['prev'])
        self.dialog_intro.avatar = self.dialog_intro.prepare_avatar(self.mushroom_intro["img"])

        self.setup_basic_dialogs()

    def setup_basic_dialogs(self):
        self.dialogue_lose = DialogueSystem(
            self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        self.dialogue_lose.set_dialogue([
            {"text": "Never give up"},
            {"text": "Try again!"}
        ])
        self.dialogue_lose.avatar = self.dialogue_lose.prepare_avatar(self.mushroom_intro['img'])

        self.dialogue_draw = DialogueSystem(
            self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        self.dialogue_draw.set_dialogue([
            {"text": "What a good match!"},
            {"text": "Get ready to try again!"}
        ])
        self.dialogue_draw.avatar = self.dialogue_draw.prepare_avatar(self.mushroom_intro['img'])

    def handle_events(self, event, state_manager):
        # START debugging jumping LEVELS
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE and state_manager.current_state_name == GAME_STATES.GAMEPLAY:
        #         if not self.is_all_levels_win:
        #             self.settings.game_data['level'] += 1
        #             state_manager.set_state(GAME_STATES.WIN_HISTORY)
        #         return
        # END debugging

        if not self.dialog_intro.show_dialogue:
            self.board.handle_events(event, state_manager)

        if self.board.is_everything_visible and self.board.player_matched_pairs < self.board.ai_matched_pairs:
            self.dialogue_lose.handle_event(event)

        if self.board.is_everything_visible and self.board.player_matched_pairs == self.board.ai_matched_pairs:
            self.dialogue_draw.handle_event(event)

        self.dialog_intro.handle_event(event)

    def render(self, screen, state_manager):
        screen.fill(self.palette[52])

        screen.blit(self.bg_level_image, (0, 0))

        # header
        self.header.render(
            screen, self.mushroom['name'], (self.board.player_matched_pairs, self.board.ai_matched_pairs))

        # board
        self.board.render(screen)

        if self.board.is_everything_visible:
            # won
            if self.board.player_matched_pairs > self.board.ai_matched_pairs:
                if self.settings.game_data['level'] <= self.settings.game_data['max_level']:
                    self.settings.game_data['level'] += 1
                    state_manager.set_state(GAME_STATES.WIN_HISTORY)
            # lose
            if self.board.player_matched_pairs < self.board.ai_matched_pairs:
                self.dialogue_lose.update(screen)
                if not self.dialogue_lose.show_dialogue:
                    self.setup_basic_dialogs()
                    self.board.setup(self.settings)

            # drawn
            if self.board.player_matched_pairs == self.board.ai_matched_pairs:
                self.dialogue_draw.update(screen)
                if not self.dialogue_draw.show_dialogue:
                    self.setup_basic_dialogs()
                    self.board.setup(self.settings)

        # dialog intro
        self.dialog_intro.update(screen)
