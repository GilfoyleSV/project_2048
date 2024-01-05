import random

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.W = 630
        self.H = 780
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
        self.font = pygame.font.SysFont('arial', 125)
        self.font_score = pygame.font.SysFont('arial', 100)
        self.score = 0
        self.dictionary_colors = {
            0: (183, 183, 182),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46),
        }

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

                    if self.checking_the_end_of_the_game():
                        exit()
            self.screen.fill((250, 243, 223))
            self.render_score()
            self.load_map()
            self.render_numbers_on_map()
            pygame.display.update()
            self.clock.tick(self.FPS)

    def load_map(self):
        pygame.draw.rect(self.screen, (133, 133, 133), (0, 150, self.W, self.H))

    def render_numbers_on_map(self):
        for y in range(4):
            for x in range(4):
                surf = pygame.Surface((self.WIDTH_CELL, self.WIDTH_CELL))
                surf.fill((133, 133, 133))
                pygame.draw.rect(surf, (self.dictionary_colors[self.map[y][x]]), (0, 0, self.WIDTH_CELL, self.WIDTH_CELL), border_radius=15)
                if self.map[y][x] == 0:
                    c = ''
                else:
                    c = str(self.map[y][x])
                char = self.font.render(c, 1, (255, 255, 255))
                position = char.get_rect(center=(75, 75))
                surf.blit(char, position)
                self.screen.blit(surf, ((self.WIDTH_CELL + 10) * x, 150 + (self.WIDTH_CELL + 10) * y))

    def render_score(self):
        score = self.font_score.render(f"Score: {self.score}", 1, (65, 65, 65))
        pos = score.get_rect(center=(300, 75))
        self.screen.blit(score, pos)

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
                    self.score += self.map[y][x]
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
                    self.score += self.map[y][x]
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
                    self.score += column[i]
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
                    self.score += column[i]
                    del column[i - 1]
                    column.insert(0, 0)
            for y in range(4):
                self.map[y][x] = column[y]

        self.add_random_numbers()

    def checking_the_end_of_the_game(self):
        for i in self.map:
            if 0 in i:
                return False
        return True


if __name__ == '__main__':
    session = Game()
    session.load_map()
    session.add_random_numbers()
    session.add_random_numbers()
    session.render_numbers_on_map()
    session.run()
