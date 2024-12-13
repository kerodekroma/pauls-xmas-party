import pygame

class SpriteCard(pygame.sprite.Sprite):
    def __init__(self, img_front_path, img_back_path, position, value):
        super().__init__()
        # images
        self.front_image = pygame.image.load(img_front_path).convert_alpha()
        self.back_image = pygame.image.load(img_back_path).convert_alpha()

        self.image = self.back_image
        self.rect = self.image.get_rect(topleft=position)
        self.is_flipped = False
        self.is_matched = False
        self.value = value
        self.is_animating = False
        self.animation_progress = 0 # from 0 to 100

    def update(self):
        if self.is_animating:
            self.animate_flip()

    def animate_flip(self):
        # animation logic
        animation_speed = 1 # speed of the animation
        self.animation_progress += animation_speed
        if self.animation_progress <= 50:
            # Shrink the width to 0
            scale_factor = 1 - (self.animation_progress / 50)
            self.image = pygame.transform.scale(
                self.back_image if not self.is_flipped else self.front_image, 
                (int(self.rect.width * scale_factor), self.rect.height)
            )

        elif self.animation_progress <= 100:
            # Grow the width back to full while flipping the image
            if self.animation_progress == 51:
                self.is_flipped = not self.is_flipped

            scale_factor = (self.animation_progress - 50) / 50
            self.image = pygame.transform.scale(
                self.front_image if self.is_flipped else self.back_image,
                (int(self.rect.width * scale_factor), self.rect.height)
            )
        else:
            # end of the animation
            self.is_animating = False
            self.image = self.front_image if self.is_flipped else self.back_image
            self.animation_progress = 0

    def flip(self):
        # self.is_flipped = not self.is_flipped
        # self.image = self.front_image if self.is_flipped else self.back_image
        if not self.is_animating:
            self.is_animating = True
            self.animation_progress = 0

    def flip_back(self):
        self.is_flipped = True
        if not self.is_animating:
            self.is_animating = True
            self.animation_progress = 0
