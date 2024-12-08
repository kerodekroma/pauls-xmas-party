from toolbox.state_manager import StateManager
# Defining the GameState base class
class GameState:
    def __init__(self, state_manager: StateManager):
        """Initialize the state(this can be empty or shared between states)"""
        pass

    def handle_events(self, events, state_manager: StateManager):
        """
        Handle events like key presses or mouse clicks.
        Each state will implement this method differently.
        :param events: List of Pygame events to handle
        :param state_manager: The state manager to enable state switching
        """
        pass

    def update(self, dt, state_manager: StateManager):
        """
        Update the state logic.
        :param dt: Delta time (time since the last frame) for smooth movement and updates
        """
        pass

    def render(self, surface, state_manager: StateManager):
        """
        Render the current state to the screen.
        :param surface: The Pygame surface (usually the main game screen)
        """
        pass