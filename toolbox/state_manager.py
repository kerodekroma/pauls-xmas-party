import pygame
import settings
class StateManager:
    def __init__(self, settings: settings.Settings):
        self.states = {}
        self.settings = settings
        self.current_state = None
        self.current_state_name = ''

        # fx
        self.current_set_state_time = 0
        self.delay_set_state = 300
        self.has_state_changed = False

    def add_state(self, name, state):
        self.states[name] = state

    def set_state(self, name):
        if name in self.states:
            self.current_state = self.states[name]
            self.current_state_name = name
            self.current_state.__init__(self)
            self.current_set_state_time = pygame.time.get_ticks()
            self.has_state_changed = True

    def handle_events(self, event):
        if self.current_state:
            self.current_state.handle_events(event, self)

    def update(self, dt):
        current_time = pygame.time.get_ticks()
        diff_time = current_time - self.current_set_state_time
        if self.current_state and diff_time > self.delay_set_state:
            self.has_state_changed = False
            self.current_state.update(dt, self)

    def render(self, surface):
        if self.current_state:
            self.current_state.render(surface, self)