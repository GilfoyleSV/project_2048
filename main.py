import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.W = 1000
        self.H = 1000
        self.screen = pygame.display.set_mode((self.W, self.H))
        self.screen.fill((0, 0, 0))
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.clock.tick(self.FPS)


if __name__ == '__main__':
    session = Game()
    session.run()
