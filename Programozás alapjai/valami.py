import pygame
import random



# Kezdeti beállítások
pygame.init()
width, height = 400, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")

# Színek
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Tetrominók alakja
tetrominos = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

# Színek listája
colors = [blue, green, red]

# Játékmező inicializálása
def create_grid():
    grid = [[black for _ in range(10)] for _ in range(20)]
    return grid

grid = create_grid()

# Tetrominó osztály
class Tetromino:
    def __init__(self):
        self.x = 4
        self.y = 0
        self.shape = random.choice(tetrominos)
        self.color = random.choice(colors)

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def valid_move(self, grid):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    if (
                        self.x + x < 0
                        or self.x + x >= 10
                        or self.y + y >= 20
                        or grid[self.y + y][self.x + x] != black
                    ):
                        return False
        return True

    def place(self, grid):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid[self.y + y][self.x + x] = self.color

    def draw(self, surface):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        surface,
                        self.color,
                        pygame.Rect((self.x + x) * 25, (self.y + y) *
25, 25, 25),
                    )

# Játék ciklus
def main():
    clock = pygame.time.Clock()
    tetromino = Tetromino()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetromino.move(-1, 0)
                    if not tetromino.valid_move(grid):
                        tetromino.move(1, 0)
                if event.key == pygame.K_RIGHT:
                    tetromino.move(1, 0)
                    if not tetromino.valid_move(grid):
                        tetromino.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    tetromino.move(0, 1)
                    if not tetromino.valid_move(grid):
                        tetromino.move(0, -1)
                if event.key == pygame.K_UP:
                    tetromino.rotate()
                    if not tetromino.valid_move(grid):
                        tetromino.rotate()

        tetromino.move(0, 1)
        if not tetromino.valid_move(grid):
            tetromino.move(0, -1)
            tetromino.place(grid)
            tetromino = Tetromino()

        # Ellenőrizze a sortörést
        for i, row in enumerate(grid[:-1]):
            if all(cell != black for cell in row):
                grid.pop(i)
                grid.insert(0, [black for _ in range(10)])

        screen.fill(black)
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                pygame.draw.rect(
                    screen,
                    cell,
                    pygame.Rect(x * 25, y * 25, 25, 25),
                )
        tetromino.draw(screen)
        pygame.display.update()
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()
