import pygame
from toolbox.font import pixel_font


class DialogueSystem:
    def __init__(self, width, height):
        """Initialize the dialogue system."""
        self.width = width
        self.height = height
        self.dialogue_rect = pygame.Rect(
            0, height, width, 120)  # Off-screen initially
        self.dialogue_speed = 5  # Sliding speed
        self.dialogue = []  # List of dialogue dictionaries
        self.text_index = 0
        self.letter_index = 0
        self.current_text = ""
        self.show_dialogue = False
        self.avatar = None  # Placeholder for the current avatar image
        self.font = pixel_font()  # Customize with a retro font
        self.buttons = [
            pygame.Rect(width - 190, height - 60, 170,
                        40)  # Example button ("Next")
        ]

    def set_dialogue(self, dialogue_data):
        """Set the dialogue data (array of dictionaries)."""
        self.dialogue = dialogue_data
        self.text_index = 0
        self.letter_index = 0
        self.show_dialogue = True
        self.dialogue_rect.y = self.height  # Reset the dialogue box for sliding

    def slide_in(self):
        """Slide the dialogue box into view."""
        if self.dialogue_rect.y > self.height - self.dialogue_rect.height:
            self.dialogue_rect.y -= self.dialogue_speed
            return False  # Animation not finished
        return True  # Animation complete

    def draw(self, screen):
        """Draw the dialogue box, avatar, and text."""
        if not self.show_dialogue:
            return

        # Draw the dialogue box
        pygame.draw.rect(screen, (50, 50, 50), self.dialogue_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.dialogue_rect, 2)


        # Draw the text
        if self.text_index < len(self.dialogue):
            full_text = self.dialogue[self.text_index]["text"]
            if self.letter_index < len(full_text):
                self.letter_index += 1  # Reveal one letter at a time
            self.current_text = full_text[:self.letter_index]
            text_surface = self.font.render(
                self.current_text, True, (255, 255, 255))
            screen.blit(text_surface, (self.dialogue_rect.x +
                        80, self.dialogue_rect.y + 20))
            if "avatar" in self.dialogue[self.text_index]:
                avatar = self.dialogue[self.text_index]["avatar"]
                screen.blit(avatar, (self.dialogue_rect.x + 10, self.dialogue_rect.y + 10))
            # Draw the avatar by default
            if not "avatar" in self.dialogue[self.text_index] and self.avatar:
                screen.blit(self.avatar, (self.dialogue_rect.x +
                        10, self.dialogue_rect.y + 10))


        # Draw buttons
        for button in self.buttons:
            pygame.draw.rect(screen, (255, 255, 255), button)
            button_text = self.font.render("Next [Enter]", True, (0, 0, 0))
            button_rect = button_text.get_rect(topleft=(button.x + 8, button.y + 8))
            screen.blit(button_text, button_rect)

    def update(self, screen):
        """Update the dialogue box animation and drawing."""
        if self.show_dialogue:
            if self.slide_in():
                self.draw(screen)

    def handle_event(self, event):
        """Handle input events for advancing dialogue or interacting with buttons."""
        if not self.show_dialogue:
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            # "Next" button clicked
            if self.buttons[0].collidepoint(event.pos):
                self.advance_text()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Advance with Enter key
                self.advance_text()

    def advance_text(self):
        """Advance to the next piece of dialogue."""
        self.text_index += 1
        self.letter_index = 0  # Reset for the new text
        if self.text_index >= len(self.dialogue):  # End of dialogue
            self.show_dialogue = False

    def prepare_avatar(self, img_path):
        avatar_img = pygame.image.load(img_path)
        avatar_img = pygame.transform.scale(avatar_img, (64, 64))
        return avatar_img