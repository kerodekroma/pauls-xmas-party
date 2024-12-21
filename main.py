# HOW TO RUN THIS SCRIPT IN TERMINAL:
# python -m main.py

import asyncio
import pygame
import sys
import random

# toolbox
from toolbox.state_manager import StateManager

# game states
from states import GAME_STATES
from states.main_menu import MainMenuState
from states.initial_history import InitialHistoryState
from states.pick_player import PickPlayerState
from states.tournament_tree import TournamentTreeState
from states.gameplay import GamePlayState
from states.win_history import WinHistoryState
from states.lose_history import LoseHistoryState

# settings
from settings import Settings

# initializing pygame
pygame.init()

# SETTINGS
SETTINGS = Settings() 

class App:
  def __init__(self):
    pygame.display.set_caption("Paul christmas party!")

    self.screen = pygame.display.set_mode((SETTINGS.WINDOW_WIDTH, SETTINGS.WINDOW_HEIGHT))

    #FX
    self.display = pygame.Surface((SETTINGS.WINDOW_WIDTH, SETTINGS.WINDOW_HEIGHT), pygame.SRCALPHA)
    self.display_2 = pygame.Surface((SETTINGS.WINDOW_WIDTH, SETTINGS.WINDOW_HEIGHT))
    self.screen_shake = 0
    self.transition = -30

    # state manager
    self.st_manager = StateManager(SETTINGS)
    self.st_manager.add_state(GAME_STATES.MAIN_MENU, MainMenuState(self.st_manager))
    # self.st_manager.add_state(GAME_STATES.INIT_HISTORY, InitialHistoryState(self.st_manager))
    # self.st_manager.add_state(GAME_STATES.PICK_PLAYER, PickPlayerState(self.st_manager))
    # self.st_manager.add_state(GAME_STATES.TOURNAMENT_TREE, TournamentTreeState(self.st_manager))
    self.st_manager.add_state(GAME_STATES.GAMEPLAY, GamePlayState(self.st_manager))
    self.st_manager.add_state(GAME_STATES.WIN_HISTORY, WinHistoryState(self.st_manager))
    # self.st_manager.add_state(GAME_STATES.LOSE_HISTORY, LoseHistoryState(self.st_manager))

    # setting up the default state
    self.st_manager.set_state(GAME_STATES.MAIN_MENU)
    # self.st_manager.set_state(GAME_STATES.WIN_HISTORY)
    # self.st_manager.set_state('gameplay')

    # setting the clock
    self.clock = pygame.time.Clock()

    self.bg_color = SETTINGS.palette[40]

  async def render(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            self.st_manager.handle_events(event)

        dt = self.clock.tick(60) / 1000
        self.display.fill(self.bg_color)

        self.st_manager.update(dt)
        self.st_manager.render(self.display)

        if self.st_manager.has_state_changed:
          self.transition += 10
          transition_surf = pygame.Surface(self.display.get_size())
          transition_surf.fill((0, 0, 0))
          transition_surf.set_alpha(100 - self.transition)
          self.display.blit(transition_surf, (0, 0))
        
        if not self.st_manager.has_state_changed:
          self.transition = 0

        self.display_2.blit(self.display, (0, 0))
        screen_shake_offset = (random.random() * self.screen_shake - self.screen_shake / 2, random.random() * self.screen_shake - self.screen_shake / 2)
        self.screen.blit(pygame.transform.scale(self.display_2, self.screen.get_size()), (screen_shake_offset, screen_shake_offset))

        #update the display
        pygame.display.flip()
        await asyncio.sleep(0)
        
asyncio.run(App().render())