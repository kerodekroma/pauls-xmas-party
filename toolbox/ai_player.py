import random
import pygame


class AIPlayer:
    def __init__(self, difficulty='beginner'):
        self.difficulty = difficulty
        self.memory = []  # Store the card values and positions
        self.thinking_start_time = 0
        self.action_step = 0
        self.selected_cards = []
        self.thinking_delay = 1000  # Default 1-second delay between actions
        self.matched_pairs = 0

    def start_turn(self, card_group):
        """Start the AI's turn."""
        self.thinking_start_time = pygame.time.get_ticks()
        self.action_step = 1
        self.selected_cards = self.make_move(card_group)

    def update_turn(self):
        """Handle the AI's turn logic step-by-step."""
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.thinking_start_time

        if self.action_step == 1 and elapsed_time > self.thinking_delay:
            # Step 1: Flip the first card
            self.selected_cards[0].flip()
            self.action_step = 2
            self.thinking_start_time = current_time

        elif self.action_step == 2 and elapsed_time > self.thinking_delay:
            # Step 2: Flip the second card
            self.selected_cards[1].flip()
            self.action_step = 3
            self.thinking_start_time = current_time

        elif self.action_step == 3 and elapsed_time > self.thinking_delay:
            # Step 3: Check match or reset
            if self.selected_cards[0].value == self.selected_cards[1].value:
                print("AI found a match!")
                self.matched_pairs += 100
            else:
                # Flip the cards back
                self.selected_cards[0].flip()
                self.selected_cards[1].flip()

            # End turn
            self.action_step = 4  # Marks the turn as finished

        return self.action_step == 4  # True if the turn is complete

    def make_move(self, card_group):
        """Simulate AI picking two cards based on difficulty."""
        visible_cards = [
            card for card in card_group if not card.is_flipped and not card.is_matched]

        if self.difficulty == "beginner":
            # Completely random moves
            return random.sample(visible_cards, 2) if len(visible_cards) >= 2 else []

        elif self.difficulty == "normal":
            # Memory-based with some randomness
            matched = self.get_memory_matches(card_group)
            if matched:
                return matched
            else:
                return random.sample(visible_cards, 2) if len(visible_cards) >= 2 else []

        elif self.difficulty == "expert":
            # Always memory-based, no randomness
            matched = self.get_memory_matches(card_group)
            if matched:
                return matched
            else:
                # Random fallback in case no known matches
                return random.sample(visible_cards, 2) if len(visible_cards) >= 2 else []

    def get_memory_matches(self, card_group):
        """Find cards the AI has seen but haven't matched."""
        memory = [
            card for card in card_group if card.is_flipped and not card.is_matched]
        for card in memory:
            # Check if a pair exists
            match = next((c for c in memory if c !=
                         card and c.value == card.value), None)
            if match:
                return [card, match]
        return None
