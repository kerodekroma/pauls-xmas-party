import toolbox.colors as colors
import toolbox.font as font

class Settings:
    def __init__(self):
        self.font  = {
            'pixel': font.pixel_font()
        }
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.palette = colors.PALETTE
        self.UNIT = 8
        self.HEADER_HEIGHT = 6 * self.UNIT
        self.MARGIN = 2 * self.UNIT
        self.BOARD_MARGIN_X = 12 * self.UNIT
        
        # ROWS, COLS to the board
        self.ROWS, self.COLS = 4, 4
        GAME_AREA_WIDTH = self.WINDOW_WIDTH - 2 * self.BOARD_MARGIN_X
        GAME_AREA_HEIGHT = self.WINDOW_HEIGHT - self.HEADER_HEIGHT
        self.CARD_WIDTH = (GAME_AREA_WIDTH - (self.COLS + 1) * self.MARGIN) // self.COLS
        self.CARD_HEIGHT = (GAME_AREA_HEIGHT - (self.ROWS + 1) * self.MARGIN) // self.ROWS

        print(self.CARD_WIDTH, self.CARD_HEIGHT)
        
        
