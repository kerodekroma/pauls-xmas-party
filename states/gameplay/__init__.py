
import pygame

from toolbox import game_state

from states.gameplay.header import GamePlayHeader
from states.gameplay.board_of_cards import GamePlayBoardOfCards


class GamePlayState(game_state.GameState):
    def __init__(self, state_manager):
        super().__init__(state_manager=state_manager)
        settings = state_manager.settings
        unit = settings.UNIT
        self.palette = settings.palette
        self.angle = 0
        self.header = GamePlayHeader( 
            state_manager,
            (settings.WINDOW_WIDTH, 6 * unit), 
            (0, 0), 
            self.palette[3]
        )
        self.board = GamePlayBoardOfCards(
            (settings.WINDOW_WIDTH, 10), (0, settings.HEADER_HEIGHT), settings)

    def handle_events(self, event, state_manager):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and state_manager.current_state_name == 'game_play':
                state_manager.set_state('main_menu')

        self.board.handle_events(event, state_manager)

    def render(self, screen, state_manager):
        screen.fill(self.palette[8])

        # header
        self.header.render(screen, (self.board.player_matched_pairs, self.board.ai_matched_pairs))

        # board
        self.board.render(screen)

        # won
        if self.board.player_matched_pairs > self.board.ai_matched_pairs:
            # show dialog as GB
            pass

        # lose the player
        if self.board.player_matched_pairs < self.board.ai_matched_pairs:
            # show dialog as GB
            pass

        # draw
        if self.board.player_matched_pairs == self.board.ai_matched_pairs:
            # show dialog as GB
            pass