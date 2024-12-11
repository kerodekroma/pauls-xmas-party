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
        self.flipped_cards = []

        # setup of the ai
        self.ai_player = AIPlayer()
        self.is_ai_player_turn = False

        # preparing the cards
        img_card_back = './assets/img/card_back.png'
        card_images = [
            './assets/img/card_front.png',
            './assets/img/card_front_dem1.png',
            './assets/img/card_front.png',
            './assets/img/card_front_dem1.png',
            './assets/img/card_front.png',
            './assets/img/card_front_dem1.png',
            './assets/img/card_front.png',
            './assets/img/card_front_dem1.png',
            './assets/img/card_front.png',
            './assets/img/card_front_dem1.png',
            './assets/img/card_front.png',
            './assets/img/card_front_dem1.png',
        ]
        self.card_values = {
            './assets/img/card_front.png': '0',
            './assets/img/card_front_dem1.png': '1',
        }
        self.cards = self.generate_card_grid(
            settings, card_images, img_card_back)
        self.cards_group = pygame.sprite.Group(self.cards) 
        self.matched_pairs = 0
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
            if event.button == 1:
                pos = pygame.mouse.get_pos()

                # check for card click using collision detection
                for index, card in enumerate(self.cards):
                    if card.rect.collidepoint(pos) and not card.is_flipped:
                        card.flip()
                        self.flipped_cards.append(index)
                        break

                # check for match when two cards are flipped
                if len(self.flipped_cards) == 2 and self.is_ai_player_turn == False:
                    pygame.time.wait(500)  # Pause for visual feedback
                    first_card = self.cards[self.flipped_cards[0]]
                    second_card = self.cards[self.flipped_cards[1]]

                    if first_card.value == second_card.value:
                        first_card.is_matched = True
                        second_card.is_matched = False
                        self.matched_pairs += 1
                        print("matched_pairs", self.matched_pairs)

                    if first_card.value != second_card.value:
                        first_card.flip()
                        second_card.flip()

                    self.flipped_cards.clear()

                    print("AI TURN!")
                    # ai's turn
                    self.is_ai_player_turn = True
                    self.ai_player.action_step = 0

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

        if self.is_ai_player_turn:
            if self.ai_player.action_step == 0:
                self.ai_player.start_turn(self.cards)

            if self.ai_player.update_turn():
                self.ai_player.action_step == 0
                self.is_ai_player_turn = False

        self.cards_group.draw(screen)