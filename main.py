import random

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
        self.free_cells = [(y, x) for x in range(4) for y in range(4)]
        self.font = pygame.font.SysFont('arial', 150)

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    self.add_random_numbers()
                    self.load_map()
                    self.render_numbers_on_map()
            pygame.display.update()
            self.clock.tick(self.FPS)

    def load_map(self):
        pygame.draw.rect(self.screen, (183, 183, 182), (100, 150, self.WIDTH_CELL * 4, self.WIDTH_CELL * 4))
        pygame.draw.rect(self.screen, (133, 133, 133), (100, 150, self.WIDTH_CELL * 4, self.WIDTH_CELL * 4), 10)
        for k in range(1, 4):
            start_horizontal = (100, 150 + self.WIDTH_CELL * k)
            end_horizontal = (self.WIDTH_CELL * 4 + 90, 150 + self.WIDTH_CELL * k)
            start_vertical = (100 + self.WIDTH_CELL * k, 150)
            end_vertical = (100 + self.WIDTH_CELL * k, 140 + self.WIDTH_CELL * 4)
            pygame.draw.line(self.screen, (133, 133, 133), start_horizontal, end_horizontal, 10)
            pygame.draw.line(self.screen, (133, 133, 133), start_vertical, end_vertical, 10)

    def render_numbers_on_map(self):
        for y in range(4):
            for x in range(4):
                if self.map[y][x] != 0:
                    char = self.font.render(str(self.map[y][x]), 1, (133, 133, 133))
                    position = char.get_rect(center=((175 + self.WIDTH_CELL * x), 225 + self.WIDTH_CELL * y))
                    self.screen.blit(char, position)

    def add_random_numbers(self):
        if len(self.free_cells) > 0:
            index = random.randrange(len(self.free_cells))
            cell = self.free_cells.pop(index)
            self.map[cell[0]][cell[1]] = random.choice([2] * 10 + [4])


if __name__ == '__main__':
    session = Game()
    session.load_map()
    session.add_random_numbers()
    session.add_random_numbers()
    session.render_numbers_on_map()
    session.run()
