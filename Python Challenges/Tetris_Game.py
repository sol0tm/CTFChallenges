import pygame
import random

def generate_random_color():
    return random.choice([RED, CYAN, MAGENTA, YELLOW, GREEN, BLUE, ORANGE])


# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [1]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
]

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))
        

def draw_tetromino(tetromino, position):
    color = generate_random_color()
    for row in range(len(tetromino)):
        for col in range(len(tetromino[row])):
            if tetromino[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    color,
                    (
                        (position[0] + col) * GRID_SIZE,
                        (position[1] + row) * GRID_SIZE,
                        GRID_SIZE,
                        GRID_SIZE,
                    ),
                )

def check_collision(tetromino, position, board):
    for row in range(len(tetromino)):
        for col in range(len(tetromino[row])):
            if (
                tetromino[row][col] == 1
                and (
                    position[0] + col < 0
                    or position[0] + col >= GRID_WIDTH
                    or position[1] + row >= GRID_HEIGHT
                    or board[position[1] + row][position[0] + col] is not None
                )
            ):
                return True
    return False

def merge_tetromino(tetromino, position, board):
    for row in range(len(tetromino)):
        for col in range(len(tetromino[row])):
            if tetromino[row][col] == 1:
                board[position[1] + row][position[0] + col] = tetromino[0][0]

def remove_completed_rows(board):
    completed_rows = [row for row in range(GRID_HEIGHT) if all(cell is not None for cell in board[row])]
    for row in completed_rows:
        del board[row]
        board.insert(0, [None] * GRID_WIDTH)

def main():
    board = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    current_tetromino = random.choice(SHAPES)
    current_position = [GRID_WIDTH // 2 - len(current_tetromino[0]) // 2, 0]

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not check_collision(current_tetromino, [current_position[0] - 1, current_position[1]], board):
            current_position[0] -= 1
        if keys[pygame.K_RIGHT] and not check_collision(current_tetromino, [current_position[0] + 1, current_position[1]], board):
            current_position[0] += 1
        if keys[pygame.K_DOWN] and not check_collision(current_tetromino, [current_position[0], current_position[1] + 1], board):
            current_position[1] += 1

        if not check_collision(current_tetromino, [current_position[0], current_position[1] + 1], board):
            current_position[1] += 1
        else:
            merge_tetromino(current_tetromino, current_position, board)
            remove_completed_rows(board)
            current_tetromino = random.choice(SHAPES)
            current_position = [GRID_WIDTH // 2 - len(current_tetromino[0]) // 2, 0]

            if check_collision(current_tetromino, current_position, board):
                game_over = True

        screen.fill(BLACK) #¢ÃãÆÀÓððÒmÖäãâñÄÅmãÈÅmÂðçÐ
        draw_grid() #IBM_INT(500)
        draw_tetromino(current_tetromino, current_position)

        for row_index, row in enumerate(board):
            for col_index, cell in enumerate(row):
                if cell is not None:
                    pygame.draw.rect(
                        screen,
                        cell,
                        (
                            col_index * GRID_SIZE,
                            row_index * GRID_SIZE,
                            GRID_SIZE,
                            GRID_SIZE,
                        ),
                    )

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()