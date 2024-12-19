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

        # assets
        self.IMG_INTRO = './assets/img/pauls-xmas-party-cover.png'
        self.BG_THANKS = './assets/img/pauls-xmas-party-thanks.jpg'
        self.CARD_BACK = './assets/img/card_back.png'
        self.CARD_IMAGES = [
            './assets/img/card_front_01.png',
            './assets/img/card_front_02.png',
            './assets/img/card_front_03.png',
            './assets/img/card_front_04.png',
            './assets/img/card_front_05.png',
            './assets/img/card_front_06.png',
            './assets/img/card_front_07.png',
            './assets/img/card_front_08.png',
        ]

        self.MUSHROOM_IMAGES = [
            './assets/img/mushroom_01.png',
            './assets/img/mushroom_02.png',
            './assets/img/mushroom_03.png',
            './assets/img/mushroom_04.png',
        ]

        self.CARD_VALUES = {
            './assets/img/card_front_01.png': '1',
            './assets/img/card_front_02.png': '2',
            './assets/img/card_front_03.png': '3',
            './assets/img/card_front_04.png': '4',
            './assets/img/card_front_05.png': '5',
            './assets/img/card_front_06.png': '6',
            './assets/img/card_front_07.png': '7',
            './assets/img/card_front_08.png': '8',
        }

        self.MUSHROOM_VALUES = {
            './assets/img/mushroom_01.png': 0,
            './assets/img/mushroom_02.png': 1,
            './assets/img/mushroom_03.png': 2,
            './assets/img/mushroom_04.png': 3,
        }

        self.MUSHROOM_NAMES = ['MUSHY KIDO', 'MR MUFFIN', 'MURNOLD CHAD', 'GRAND MUSHMA']
        # global state
        self.game_data = {
            'level': 1,
        } 

        # player
        self.data_player = {
            'score': 0,
        } 

        # rival
        self.data_mushroom = {
            'name': 0, 
            'score': 0
        }

    def get_card_img_by_level(self, num_level):
        """Returns a structure with the first two elements repeated to make 8 items."""
        imgs = list(self.CARD_VALUES.keys())[:2]  # Get the first 2 keys

        if num_level == 2:
            imgs = list(self.CARD_VALUES.keys())[:4]  # Get the first 4 keys
            return imgs * 2

        if num_level == 3 or num_level == 4:
            imgs = list(self.CARD_VALUES.keys())[:8]  # Get the first 8 keys
            return imgs

        return (imgs * 4)[:8]

    def mushroom_by_level(self, num_level):
        return {'img': self.MUSHROOM_IMAGES[num_level - 1], 'name': self.MUSHROOM_NAMES[num_level - 1]}

    def bg_by_level(self, num_level=-1):
        file_name = 'pauls-party'
        if num_level == 0:
            return f'./assets/img/{file_name}-00.png'
        if num_level == 1:
            return f'./assets/img/{file_name}-01.png'
        if num_level == 2:
            return f'./assets/img/{file_name}-02.png'
        if num_level == 3:
            return f'./assets/img/{file_name}-04.png'
        return f'./assets/img/{file_name}-05.jpg'