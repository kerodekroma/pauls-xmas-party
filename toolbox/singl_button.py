import pygame

from enum import Enum, auto
from .font import pixel_font

class PY_SINGLE_BUTTON_Events(Enum):
    PRESSED = auto()
    RELEASED = auto()

class SinglButton:
    def __init__(self, position, options):
        self.options = options
        self.position = position
        self.track_touches = []
        self.current_event = PY_SINGLE_BUTTON_Events.RELEASED
        self.setup()

    def setup(self):

        if "radius" in self.options:
            radius = self.options['radius']
            self.surface = pygame.Surface(( radius * 2, radius * 2))
            self.surface.set_alpha(0)
            self.rect = self.surface.get_rect()
            self.rect.x = self.position[0] - radius
            self.rect.y = self.position[1] - radius
            return
        
        width = self.options["width"]
        height = self.options["height"]
        self.surface = pygame.Surface(( width, height ))
        self.rect = self.surface.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def listen_events(self, event):
        mouse_pos = pygame.mouse.get_pos()
        # Check if the click is inside the circle
        is_button_down = event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN
        is_button_up = event.type == pygame.MOUSEBUTTONUP or event.type == pygame.FINGERUP

        if is_button_down and not self.rect.collidepoint(mouse_pos):
            if 0 in self.track_touches:
                return
            self.track_touches.append(0)

        if is_button_down and self.rect.collidepoint(mouse_pos):
            if 1 in self.track_touches:
                self.track_touches.append(0)
                return
            self.track_touches.append(1)
            self.current_event = PY_SINGLE_BUTTON_Events.PRESSED

        if is_button_up:
            num_touches = len(self.track_touches)
            if num_touches > 0 and self.track_touches[num_touches - 1] == 0:
                for item in self.track_touches:
                    if item == 0:
                        self.track_touches.remove(item)
                return
            self.track_touches = []
            self.current_event = PY_SINGLE_BUTTON_Events.RELEASED

    def render(self, screen):
        pass
    
class SinglSquareButton(SinglButton):
    def __init__(self, position, options):
        defaults = {
            "width": 80,
            "height": 80,
            "text": "",
            "text_color": (0, 0, 0),
            "bg_color": (0, 0, 255)
        }
        self.settings = defaults.copy()
        self.settings.update(options)
        self.position = position
        # Font
        self.pixel_font = pixel_font()
        super().__init__(position, self.settings)

    def listen_events(self, event):
        super().listen_events(event)

    def render(self, screen):
        bg_color = self.settings['bg_color']
        pygame.draw.rect(screen, bg_color, self.rect)
        
        # text to debug
        if self.settings['text']:
            text_color = self.settings['text_color']
            text_surface = self.pixel_font.render(f"{self.settings['text']}", True, text_color)
            text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.centery))
            screen.blit(text_surface, text_rect)

class SinglCircularButton(SinglButton):
    def __init__(self, position, options):
        defaults = {
            "radius": 50,
            "text": "A",
            "text_color": (0, 0, 0),
            "bg_color": (0, 0, 255)
        }
        self.settings = defaults.copy()
        self.settings.update(options)
        self.position = position
        super().__init__(position, self.settings)

    def listen_events(self, event):
        super().listen_events(event)

    def render(self, screen):
        bg_color = self.settings['bg_color']
        radius = self.settings['radius']
        pygame.draw.circle(screen, bg_color, self.position, radius)