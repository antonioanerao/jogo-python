import os
import sys
import pygame
from dotenv import load_dotenv

load_dotenv()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(os.getenv('TITLE'))
        self.screen = pygame.display.set_mode((int(os.getenv('WIDTH')), int(os.getenv('HEIGHT'))))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('Black')
            pygame.display.update()
            self.clock.tick(int(os.getenv('FPS')))


if __name__ == '__main__':
    game = Game()
    game.run()
