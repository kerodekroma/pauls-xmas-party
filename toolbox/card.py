import pygame


class SpriteCard(pygame.sprite.Sprite):
    def __init__(self, img_front_path, img_back_path, position, value):
        super().__init__()
        # images
        self.front_image = pygame.image.load(img_front_path).convert_alpha()
        self.back_image = pygame.image.load(img_back_path).convert_alpha()

        self.image = self.back_image
        self.rect = self.image.get_rect(topleft=position)

        # value
        self.is_flipped = False
        self.is_matched = False
        self.value = value

        # fx
        self.is_flipping = False
        self.start_flipping_time = 0
        self.flip_duration = 1000

    def update(self):
        if self.is_flipping:
            self.transition_flip()

    def transition_flip(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_flipping_time

    # basic flip
    def flip(self):
        self.is_flipped = not self.is_flipped
        self.image = self.front_image if self.is_flipped else self.back_image

    # TODO
    def animated_flip(self):
        if not self.is_flipping:
            self.is_flipping = True
            self.start_flipping_time = pygame.time.get_ticks()