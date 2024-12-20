import pygame

class ImageTransition:
    def __init__(self, duration=60):
        self.duration = duration
        self.alpha = 255
        self.current_image = None
        self.next_image = None
        self.transitioning = False
        self.fade_out = True

    def start_transition(self, current_image, next_image):
        """Initialize the transition between two images."""
        self.current_image = current_image
        self.next_image = next_image
        self.alpha = 255
        self.transitioning = True
        self.fade_out = True

    def update(self):
        """Update the transition animation."""
        if not self.transitioning:
            return

        if self.fade_out:
            self.alpha -= 255 // self.duration  # Fade out step
            if self.alpha <= 0:
                self.alpha = 0
                self.fade_out = False  # Switch to fade in
        else:
            self.alpha += 255 // self.duration  # Fade in step
            if self.alpha >= 255:
                self.alpha = 255
                self.transitioning = False  # Transition finished

    def render(self, screen):
        """Draw the transition effect."""
        # if not self.transitioning:
        #     return

        if self.fade_out:
            # Draw the current image with decreasing alpha
            temp_surface = self.current_image.copy()
            temp_surface.set_alpha(self.alpha)
            screen.blit(temp_surface, (0, 0))
        else:
            # Draw the next image with increasing alpha
            temp_surface = self.next_image.copy()
            temp_surface.set_alpha(self.alpha)
            screen.blit(temp_surface, (0, 0))