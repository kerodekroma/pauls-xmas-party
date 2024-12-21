import pygame

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

        self.sfx = {
            'bg_sound': pygame.mixer.Sound('./assets/sound/bg_sound.ogg'),
            'click_card': pygame.mixer.Sound('./assets/sound/click_card.ogg'),
            'win': pygame.mixer.Sound('./assets/sound/win.ogg'),
        }

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

        self.MUSHROOM_NAMES = ['MUSHY KIDO', 'MR MUFFIN', 'MUSH CHAD', 'MUSHMAMA']
        # global state
        self.game_data = {
            'level': 0,
            'max_level': 4
        } 

        # player
        # self.data_player = {
        #     'score': 0,
        #     'loses': 0,
        #     'draws': 0
        # } 

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
        if num_level < self.game_data['max_level']:
            return {'img': self.MUSHROOM_IMAGES[num_level], 'name': self.MUSHROOM_NAMES[num_level]}
        return {'img': './assets/img/paul_avatar.png', 'name': 'Paul'}

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

    def get_dialogue_by_level(self, num_level=-1):
        if num_level == 0:
            return  {
                "prev": [
                    {"text": "Think you can match my memory, Paul? Prove it!."},
                    {"text": "Try to pick up a couple of cards and see what happens."}
                ],
                "post": [
                    {"text": "Okay, you win! Let's start with the tree."},
                    {"text": "Let me introduce to you my friend to play too."},
                ]
            }
        if num_level == 1:
            return {
                "prev": [
                    {"text": "Nice to meet you Paul!"},
                    {"text": "I got the next challenge for you. Let's a go!."}
                ],
                "post": [
                    {"text": "You’re good, Paul! The tree is in place."},
                    {"text": "Good luck with the next one :)"}
                ]
            }
        if num_level == 2:
            return {
                "prev": [
                    {"text": "Ey, wanna play?"},
                    {"text": "Adding decorations is no easy feat. Are you ready?."}
                ],
                "post": [
                    {"text": "Nice one! The valley feels livelier now."},
                    {"text": "Now, It's turn to play with a legend..."}
                ]
            }
        if num_level == 3:
            return {
                "prev": [
                    {"text": "Let’s test your skills again. People need cheering!."}
                ],
                "post": [
                    {"text": "Great job! Everyone’s ready for more fun."},
                    {"text": "Thanks for playing!"},
                ]
            }
        return {"prev":[], "post":[]}
