
import pygame

from toolbox import game_state
from toolbox.dialogue_system import DialogueSystem

from states.gameplay.header import GamePlayHeader
from states.gameplay.board_of_cards import GamePlayBoardOfCards


class GamePlayState(game_state.GameState):
    def __init__(self, state_manager):
        super().__init__(state_manager=state_manager)
        self.settings = state_manager.settings
        unit = self.settings.UNIT
        self.palette = self.settings.palette
        self.angle = 0
        self.header = GamePlayHeader(
            state_manager,
            (self.settings.WINDOW_WIDTH, 6 * unit),
            (0, 0),
            self.palette[3]
        )
        self.board = GamePlayBoardOfCards(
            (self.settings.WINDOW_WIDTH, 10), (0, self.settings.HEADER_HEIGHT), self.settings)

        # Load avatar
        avatar_img = pygame.image.load("./assets/img/flag32x32.png")
        avatar_img = pygame.transform.scale(avatar_img, (64, 64))
        self.dialogue = DialogueSystem(
            self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        self.dialogue.set_dialogue([
            {"avatar": "avatar.png", "text": "Welcome to the Christmas party!"},
            {"avatar": "avatar.png", "text": "Get ready for a festive night!"}
        ])
        self.dialogue.avatar = avatar_img  # Set avatar

    def handle_events(self, event, state_manager):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and state_manager.current_state_name == 'game_play':
                state_manager.set_state('main_menu')

        self.board.handle_events(event, state_manager)
        self.dialogue.handle_event(event)

    def render(self, screen, state_manager):
        screen.fill(self.palette[8])

        # header
        self.header.render(
            screen, (self.board.player_matched_pairs, self.board.ai_matched_pairs))

        # board
        self.board.render(screen)

        if self.board.is_everything_visible:
            self.dialogue.update(screen)
            # TODO
            # self.board.setup(self.settings)
            # won
            if self.board.player_matched_pairs > self.board.ai_matched_pairs:
                # show dialog as GB
                print("you won!!")

            # lose
            if self.board.player_matched_pairs < self.board.ai_matched_pairs:
                # show dialog as GB
                print("you lose!!")

            # drawn
            if self.board.player_matched_pairs == self.board.ai_matched_pairs:
                # show dialog as GB
                print("draw!!")
