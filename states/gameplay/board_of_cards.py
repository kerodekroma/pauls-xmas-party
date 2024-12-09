import pygame
from toolbox.card import SpriteCard

class GamePlayBoardOfCards():
    def __init__(self, size, position, settings):
        self.size = size
        self.position = position
        self.color = (255, 102, 0)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.settings = settings
        self.cards = pygame.sprite.Group()
        img_card_front = './assets/img/card_front.png'
        img_card_back = './assets/img/card_back.png'
        self.revealed_boxes = []

        # preparing the cards
        for row in range(settings.ROWS):
            for col in range(settings.COLS):
                x = settings.BOARD_MARGIN_X + settings.MARGIN + (settings.CARD_WIDTH + settings.MARGIN) * col
                y = settings.HEADER_HEIGHT + settings.MARGIN + (settings.CARD_HEIGHT + settings.MARGIN) * row
                card = SpriteCard(img_card_front, img_card_back, x, y)
                self.cards.add(card)

    def handle_events(self, event, state_manager):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for card in self.cards:
                    card.handle_click(pos)
                    if card.is_flipped:
                        self.revealed_boxes(( card.x, card.y ))

    def render(self, screen):
        settings = self.settings
        pygame.draw.rect(screen, self.color, self.rect)
        self.cards.draw(screen)