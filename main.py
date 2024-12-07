# HOW TO RUN THIS SCRIPT IN TERMINAL:
# python -m main.py

import asyncio
import pygame
import sys

WIDTH, HEIGHT = 800, 600

# toolbox
import toolbox.colors as colors
import toolbox.font as font
from toolbox.state_manager import StateManager

# game states
from states.main_menu_state import MainMenuState
from states.gameplay_state import GamePlayState

# initializing pygame
pygame.init()

# SETTINGS
SETTINGS = {
    'font': {
        'pixel': font.pixel_font()
    },
    'WINDOW_WIDTH': WIDTH,
    'WINDOW_HEIGHT' : HEIGHT,
    'palette': colors.PALETTE
}

class App:
  def __init__(self):
    pygame.display.set_caption("Paul christmas party!")

    # state manager
    self.st_manager = StateManager(SETTINGS)
    self.st_manager.add_state('main_menu', MainMenuState(self.st_manager))
    self.st_manager.add_state('gameplay', GamePlayState(self.st_manager))

    # setting up the default state
    self.st_manager.set_state('main_menu')
    # self.st_manager.set_state('game_play')
    self.screen = pygame.display.set_mode((SETTINGS['WINDOW_WIDTH'], SETTINGS['WINDOW_HEIGHT']))

    # setting the clock
    self.clock = pygame.time.Clock()

    self.bg_color = SETTINGS['palette'][1]

  async def render(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            self.st_manager.handle_events(event)

        dt = self.clock.tick(60) / 1000
        self.screen.fill(self.bg_color)
        self.st_manager.update(dt)
        self.st_manager.render(self.screen)
        #update the display
        pygame.display.flip()
        await asyncio.sleep(0)
        
asyncio.run(App().render())