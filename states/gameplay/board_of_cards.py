import pygame
import random
from toolbox.card import SpriteCard
from toolbox.ai_player import AIPlayer


class GamePlayBoardOfCards():
    def __init__(self, size, position, settings):
        self.size = size
        self.position = position
        self.color = (255, 102, 0)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.settings = settings
        self.setup(settings)

    def setup(self, settings):
        self.flipped_cards = []

        self.not_matched = []
        self.current_not_matched_time = 0
        self.flip_back_delay_time = 400
        self.is_everything_visible = False

        # setup of the ai
        self.ai_player = AIPlayer()
        self.is_ai_player_turn = False

        # preparing the cards
        img_card_back = './assets/img/card_back.png'
        card_images = [
            './assets/img/card_front.png',
            './assets/img/card_front.png',
            './assets/img/card_front.png',
            './assets/img/card_front.png',
            './assets/img/card_front_dem1.png',
            './assets/img/card_front_dem1.png',
            './assets/img/card_front_dem1.png',
            './assets/img/card_front_dem1.png',
        ]
        self.card_values = {
            './assets/img/card_front.png': '0',
            './assets/img/card_front_dem1.png': '1',
        }
        self.cards = self.generate_card_grid(
            settings, card_images, img_card_back)
        self.cards_group = pygame.sprite.Group(self.cards)

        self.player_matched_pairs = 0
        self.ai_matched_pairs = 0

    def generate_card_grid(self, settings, card_images, back_image):
        pairs = card_images * 2  # Duplicate the image to pairs
        random.shuffle(pairs)  # Shuffle the list
        result = []

        for row in range(settings.ROWS):
            for col in range(settings.COLS):
                x = settings.BOARD_MARGIN_X + settings.MARGIN + \
                    (settings.CARD_WIDTH + settings.MARGIN) * col
                y = settings.HEADER_HEIGHT + settings.MARGIN + \
                    (settings.CARD_HEIGHT + settings.MARGIN) * row
                img = pairs.pop()
                value = self.card_values[img]
                card = SpriteCard(img, back_image, (x, y), value)
                result.append(card)
        return result

    def handle_events(self, event, state_manager):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_ai_player_turn == False:
                pos = pygame.mouse.get_pos()

                # check for card click using collision detection
                for index, card in enumerate(self.cards):
                    if card.rect.collidepoint(pos) and not card.is_flipped:
                        card.flip()
                        self.flipped_cards.append(index)
                        break

                # check for match when two cards are flipped
                if len(self.flipped_cards) == 2 and self.is_ai_player_turn == False:
                    first_card = self.cards[self.flipped_cards[0]]
                    second_card = self.cards[self.flipped_cards[1]]

                    if first_card.value == second_card.value:
                        first_card.is_matched = True
                        second_card.is_matched = True
                        self.player_matched_pairs += 100
                        self.start_ai_player_turn()

                    if first_card.value != second_card.value:
                        self.current_not_matched_time = pygame.time.get_ticks()
                        self.not_matched = [first_card, second_card]

                self.is_everything_visible = self.check_all_is_visible()

    # ai's turn
    def start_ai_player_turn(self):
        self.not_matched = []
        self.flipped_cards = []
        self.is_ai_player_turn = True
        self.ai_player.action_step = 0

    def check_all_is_visible(self):
        matched_cards = [
            card for card in self.cards if card.is_matched]
        return len(matched_cards) == len(self.cards)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.current_not_matched_time

        if len(self.not_matched) and elapsed_time > self.flip_back_delay_time:
            self.current_not_matched_time = 0
            for card in self.not_matched:
                card.flip()
            self.start_ai_player_turn()

        if self.is_ai_player_turn and not self.is_everything_visible:
            if self.ai_player.action_step == 0:
                self.ai_player.start_turn(self.cards)

            if self.ai_player.update_turn():
                self.ai_matched_pairs = self.ai_player.matched_pairs
                self.ai_player.action_step == 0
                self.is_ai_player_turn = False
                self.is_everything_visible = self.check_all_is_visible()

        self.cards_group.update()
        self.cards_group.draw(screen)
