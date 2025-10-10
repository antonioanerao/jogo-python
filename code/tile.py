import pygame
import os
from dotenv import load_dotenv

load_dotenv()


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((int(os.getenv('TILESIZE')), int(os.getenv('TILESIZE'))))):
        super().__init__(groups)

        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 10)
