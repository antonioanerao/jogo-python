import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, type):
        super().__init__(groups)

        if type == 'x':
            self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()
            inflate = (0, -10)
        if type == 'z':
            self.image = pygame.image.load('../graphics/objects/bush_simple.png').convert_alpha()
            self.image = pygame.transform.scale2x(self.image)
            inflate = (0, -50)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(inflate)
