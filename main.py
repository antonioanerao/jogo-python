import os
import sys
import pygame
from dotenv import load_dotenv

load_dotenv()


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((int(os.getenv('WIDTH')), int(os.getenv('HEIGHT'))))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            pygame.draw.circle(self.screen, 'red', self.player_pos, 40)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.player_pos.y -= 300 * self.dt
            if keys[pygame.K_s]:
                self.player_pos.y += 300 * self.dt
            if keys[pygame.K_a]:
                self.player_pos.x -= 300 * self.dt
            if keys[pygame.K_d]:
                self.player_pos.x += 300 * self.dt

            pygame.display.flip()
            self.dt = self.clock.tick(int(os.getenv('FPS'))) / 1000


if __name__ == '__main__':
    game = Game()
    game.run()
