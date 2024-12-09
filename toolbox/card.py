import pygame

class SpriteCard(pygame.sprite.Sprite):
    def __init__(self, img_front_path, img_back_path, x, y):
        super().__init__()
        # images
        self.front_image = pygame.image.load(img_front_path).convert_alpha()
        self.back_image = pygame.image.load(img_back_path).convert_alpha()

        self.image = self.back_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_flipped = False

    def handle_click(self, pos):
        if self.rect.collidepoint(pos):
            self.flip() 
    
    def flip(self):
        self.is_flipped = not self.is_flipped
        self.image = self.front_image if self.is_flipped else self.back_image

    def update(self):
        pass