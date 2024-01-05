import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.W = 800
        self.H = 800
        self.WIDTH_CELL = 150
        self.screen = pygame.display.set_mode((self.W, self.H))
        self.screen.fill((250, 243, 223))
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.load_map()

            pygame.display.update()
            self.clock.tick(self.FPS)

    def load_map(self):
        pygame.draw.rect(self.screen, (183, 183, 182), (100, 150, self.WIDTH_CELL * 4, self.WIDTH_CELL * 4))
        pygame.draw.rect(self.screen, (133, 133, 133), (100, 150, self.WIDTH_CELL * 4, self.WIDTH_CELL * 4), 10)
        for k in range(1, 4):
            start_horizontal = (100, 150 + self.WIDTH_CELL * k)
            end_horizontal = (self.WIDTH_CELL * 4 + 90, 150 + self.WIDTH_CELL * k)
            start_vertical = (100 + self.WIDTH_CELL * k, 150)
            end_vertical = (100 + self.WIDTH_CELL * k, 150 + self.WIDTH_CELL * 4)
            pygame.draw.line(self.screen, (133, 133, 133), start_horizontal, end_horizontal, 10)
            pygame.draw.line(self.screen, (133, 133, 133), start_vertical, end_vertical, 10)


if __name__ == '__main__':
    session = Game()
    session.run()
