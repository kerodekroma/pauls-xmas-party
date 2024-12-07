class StateManager:
    def __init__(self, settings):
        self.states = {}
        self.settings = settings
        self.current_state = None
        self.current_state_name = ''

    def add_state(self, name, state):
        self.states[name] = state

    def set_state(self, name):
        if name in self.states:
            self.current_state = self.states[name]
            self.current_state_name = name
            self.current_state.__init__(self)

    def handle_events(self, event):
        if self.current_state:
            self.current_state.handle_events(event, self)

    def update(self, dt):
        if self.current_state:
            self.current_state.update(dt, self)

    def render(self, surface):
        if self.current_state:
            self.current_state.render(surface, self)