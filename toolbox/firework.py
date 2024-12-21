import pygame
import math
import random

# Particle class
class Particle:
    def __init__(self, x, y, color, angle, speed, lifespan):
        self.x = x
        self.y = y
        self.color = color
        self.angle = angle
        self.speed = speed
        self.lifespan = lifespan
        self.age = 0

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.speed *= 0.98  # Simulate air resistance
        self.age += 1
        self.lifespan -= 1

    def draw(self, surface):
        alpha = max(0, int(255 * (self.lifespan / 60)))  # Fade out
        color = (*self.color, alpha)
        s = pygame.Surface((4, 4), pygame.SRCALPHA)
        pygame.draw.circle(s, color, (2, 2), 2)
        surface.blit(s, (self.x, self.y))

class Firework:
    def __init__(self, screen_width, screen_height):
        self.x = random.randint(100, screen_width - 100)
        self.y = screen_height
        self.target_y = random.randint(100, screen_height // 2)
        self.color = [random.randint(50, 255) for _ in range(3)]
        self.exploded = False
        self.particles = []

    def update(self):
        if not self.exploded:
            self.y -= 5
            if self.y <= self.target_y:
                self.exploded = True
                self.create_particles()
        else:
            for particle in self.particles:
                particle.update()
            self.particles = [p for p in self.particles if p.lifespan > 0]

    def draw(self, surface):
        if not self.exploded:
            pygame.draw.circle(surface, self.color, (self.x, self.y), 5)
        else:
            for particle in self.particles:
                particle.draw(surface)

    def create_particles(self):
        for _ in range(100):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 5)
            lifespan = random.randint(30, 60)
            self.particles.append(Particle(self.x, self.y, self.color, angle, speed, lifespan))
