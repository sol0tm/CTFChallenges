import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
FPS = 10
STARTING_TIMER = 350  # Starting timer in seconds
FOOD_POINTS = 10  # Points for each food collected
CONGRATULATORY_SCORE = 50  # Score threshold for displaying a message

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                         random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Bomb class
class Bomb:
    def __init__(self):
        self.position = (0, 0)
        self.color = BLUE
        self.timer = random.randint(50, 200)  # Timer for explosion

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                         random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Timer class
class Timer:
    def __init__(self, seconds):
        self.seconds = seconds
        self.font = pygame.font.Font(None, 36)

    def update(self):
        self.seconds -= 1
        if self.seconds < 0:
            self.seconds = 0

    def render(self, surface):
        timer_text = self.font.render(f"Timer: {self.seconds}", True, WHITE)
        surface.blit(timer_text, (10, 10))

# Score class
class Score:
    def __init__(self):
        self.points = 0
        self.font = pygame.font.Font(None, 36)

    def update(self, delta_points):
        self.points += delta_points
#b_a_s_e_45
    def render(self, surface):
        score_text = self.font.render(f"Score: {self.points}", True, WHITE)
        surface.blit(score_text, (WIDTH - 150, 10))

# Congratulatory message class
class CongratulatoryMessage:
    def __init__(self):
        self.font = pygame.font.Font(None, 48)

    def render(self, surface):
        message_text = self.font.render("VQE*VD1N8/+8LTABM66Y91C9ST8", True, RED)
        text_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        surface.blit(message_text, text_rect)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def draw_grid(surface):
    for y in range(0, HEIGHT, GRID_SIZE):
        for x in range(0, WIDTH, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, WHITE, rect, 1)

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    food = Food()
    bombs = []
    timer = Timer(STARTING_TIMER)
    score = Score()
    congratulatory_message = CongratulatoryMessage()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    snake.direction = RIGHT

        # Update components
        snake.update()

        # Check if the snake eats food
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()
            score.update(FOOD_POINTS)

        # Check if the snake collides with a bomb
        for bomb in bombs:
            if snake.get_head_position() == bomb.position:
                snake.length = max(1, snake.length - 1)
                bombs.remove(bomb)

        # Generate new bombs periodically
        if random.randint(0, 100) < 5:  # 5% chance to spawn a bomb
            new_bomb = Bomb()
            new_bomb.randomize_position()
            bombs.append(new_bomb)

        # Update bomb timers and remove exploded bombs
        for bomb in bombs:
            bomb.timer -= 1
            if bomb.timer == 0:
                bombs.remove(bomb)

        # Update timer
        timer.update()

        # Check if the timer reached 0 and reset the snake
        if timer.seconds == 0:
            snake.reset()
            timer = Timer(STARTING_TIMER)
            score.update(-score.points)  # Reset score to 0

        # Draw on the surface
        surface.fill((0, 0, 0))
        draw_grid(surface)
        snake.render(surface)
        food.render(surface)
        for bomb in bombs:
            bomb.render(surface)
        timer.render(surface)
        score.render(surface)

        # Display congratulatory message if the score is more than 50
        if score.points > CONGRATULATORY_SCORE:
            congratulatory_message.render(surface)

        # Update the screen
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
