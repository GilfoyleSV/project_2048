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
        self.font = pygame.font.SysFont('arial', 150)

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.move_down()
                    elif event.key == pygame.K_UP:
                        self.move_up()
                    elif event.key == pygame.K_RIGHT:
                        self.move_right()
                    elif event.key == pygame.K_LEFT:
                        self.move_left()

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
        free_cells = []
        for y in range(4):
            for x in range(4):
                if self.map[y][x] == 0:
                    free_cells.append((y, x))
        if len(free_cells) > 0:
            index = random.randrange(len(free_cells))
            cell = free_cells.pop(index)
            self.map[cell[0]][cell[1]] = random.choice([2] * 10 + [4])

    def move_left(self):
        for row in self.map:
            while 0 in row:
                row.remove(0)
            while len(row) < 4:
                row.append(0)

        for y in range(4):
            for x in range(3):
                if self.map[y][x] == self.map[y][x + 1] and self.map[y][x] != 0:
                    self.map[y][x] *= 2
                    del self.map[y][x + 1]
                    self.map[y].append(0)

        self.add_random_numbers()

    def move_right(self):
        for row in self.map:
            while 0 in row:
                row.remove(0)
            while len(row) < 4:
                row.insert(0, 0)

        for y in range(4):
            for x in range(3, 0, -1):
                if self.map[y][x] == self.map[y][x - 1] and self.map[y][x] != 0:
                    self.map[y][x] *= 2
                    del self.map[y][x - 1]
                    self.map[y].insert(0, 0)

        self.add_random_numbers()

    def move_up(self):
        for x in range(4):
            column = [self.map[y][x] for y in range(4)]
            while 0 in column:
                column.remove(0)
            while len(column) < 4:
                column.append(0)

            for i in range(3):
                if column[i] == column[i + 1] and column[i] != 0:
                    column[i] *= 2
                    del column[i + 1]
                    column.append(0)
            for y in range(4):
                self.map[y][x] = column[y]

        self.add_random_numbers()

    def move_down(self):
        for x in range(4):
            column = [self.map[y][x] for y in range(4)]
            while 0 in column:
                column.remove(0)
            while len(column) < 4:
                column.insert(0, 0)

            for i in range(3, 0, -1):
                if column[i] == column[i - 1] and column[i] != 0:
                    column[i] *= 2
                    del column[i - 1]
                    column.insert(0, 0)
            for y in range(4):
                self.map[y][x] = column[y]

        self.add_random_numbers()


if __name__ == '__main__':
    session = Game()
    session.load_map()
    session.add_random_numbers()
    session.add_random_numbers()
    session.render_numbers_on_map()
    session.run()
