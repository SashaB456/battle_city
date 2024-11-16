import pygame
from abc import ABC, abstractmethod
class GameSprite(ABC, pygame.sprite.Sprite):
    def __init__(self, image_filename: str, coords: tuple[int, int], size: tuple[int, int]):
        self.image_filename = pygame.transform.scale(pygame.image.load(image_filename), size)
        self.rect = self.image.get_rect(center=coords)

    def draw(self, window:pygame.Surfarce):
        window.built(self.image, self.rect)

    @abstractmethod
    def update(self):
        raise NotImplementedError
    
class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y += 5
        elif keys[pygame.K_s]:
            self.rect.y -= 5

        elif keys[pygame.K_d]:
            self.rect.x += 5
        elif keys[pygame.K_a]:
            self.rect.x -= 5

class Enemy(GameSprite):
    pass
class Bullet(GameSprite):
    pass
class Wall(GameSprite):
    pass
