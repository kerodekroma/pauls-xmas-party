
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

        # Load avatar
        avatar_img = pygame.image.load("./assets/img/flag32x32.png")
        avatar_img = pygame.transform.scale(avatar_img, (64, 64))

        # dialogs
        # intro
        mushroom_intro = self.settings.mushroom_by_level(self.current_level)
        self.dialog_intro = DialogueSystem(
            self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT
        )
        self.dialog_intro.set_dialogue(self.settings.get_dialogue_by_level(self.current_level)['prev'])
        self.dialog_intro.avatar = self.dialog_intro.prepare_avatar(mushroom_intro["img"])

        self.dialogue_lose = DialogueSystem(
            self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        self.dialogue_lose.avatar = self.dialogue_lose.prepare_avatar(mushroom_intro['img'])
        self.lose_dialogue = [
            {"text": "Never give up"},
            {"text": "Try again!"}
        ]
        self.dialogue_lose.set_dialogue(self.lose_dialogue)

        self.dialogue_draw = DialogueSystem(
            self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        self.dialogue_draw.avatar = self.dialogue_draw.prepare_avatar(mushroom_intro['img'])
        self.draw_dialogue = [
            {"text": "What a match!"},
            {"text": "Get ready for a next round!"}
        ]
        self.dialogue_draw.set_dialogue(self.draw_dialogue)

    def handle_events(self, event, state_manager):
        # START debugging jumping LEVELS
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and state_manager.current_state_name == GAME_STATES.GAMEPLAY:
                if not self.is_all_levels_win:
                    self.settings.game_data['level'] += 1
                    state_manager.set_state(GAME_STATES.WIN_HISTORY)
                return
        # END debugging

        self.board.handle_events(event, state_manager)

        # self.dialogue_win.handle_event(event)
        self.dialogue_lose.handle_event(event)
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
                # self.dialogue_win.update(screen)
                #if not self.dialogue_win.show_dialogue:
                if self.settings.game_data['level'] <= self.settings.game_data['max_level']:
                    self.settings.game_data['level'] += 1
                    state_manager.set_state(GAME_STATES.WIN_HISTORY)
                    # self.setup(state_manager)
                    # self.board.setup(self.settings, self.settings.game_data['level'])
            # lose
            if self.board.player_matched_pairs < self.board.ai_matched_pairs:
                # show dialog as GB
                self.dialogue_lose.update(screen)
                if not self.dialogue_lose.show_dialogue:
                    self.board.setup(self.settings)

            # drawn
            if self.board.player_matched_pairs == self.board.ai_matched_pairs:
                # show dialog as GB
                self.dialogue_draw.update(screen)
                if not self.dialogue_draw.show_dialogue:
                    self.board.setup(self.settings)

        # dialog intro
        self.dialog_intro.update(screen)
