import pygame
import sys
from dotenv import load_dotenv
from level import Level
import settings

load_dotenv()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.TITLE)
        self.screen = pygame.display.set_mode((int(settings.WIDTH), int(settings.HEIGHT)))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(int(settings.FPS))


if __name__ == '__main__':
    game = Game()
    game.run()
