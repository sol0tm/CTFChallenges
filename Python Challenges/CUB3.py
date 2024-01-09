import pygame
import sys
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("?_?")
clock = pygame.time.Clock()

# Cube parameters
cube_size = 100
angle = 0

# Define cube vertices
vertices = [
    [-cube_size, -cube_size, -cube_size],
    [cube_size, -cube_size, -cube_size],
    [cube_size, cube_size, -cube_size],
    [-cube_size, cube_size, -cube_size],
    [-cube_size, -cube_size, cube_size],
    [cube_size, -cube_size, cube_size],
    [cube_size, cube_size, cube_size],
    [-cube_size, cube_size, cube_size]
]

# Define cube edges
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (255, 255, 0), (255, 0, 255), (0, 255, 255),
          (255, 255, 255), (128, 128, 128)]

# Initial color index
color_index = 0

# Font
font = pygame.font.Font(None, 36)

# Some text_b85
encrypted_text = font.render("F)Pl56W?O%<F83O:K:.X?VN>))", True, (255, 255, 255))
text_rect = encrypted_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
text_speed = 8  # Adjust the speed

# Main game loop
running = True
start_time = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Rotate cube
    angle += 0.02
    rotated_vertices = []
    for vertex in vertices:
        x, y, z = vertex
        new_x = x * math.cos(angle) - z * math.sin(angle)
        new_z = x * math.sin(angle) + z * math.cos(angle)
        rotated_vertices.append([new_x, y, new_z])

    # Project 3D points to 2D screen
    projected_points = []
    for vertex in rotated_vertices:
        x, y, z = vertex
        f = 200  # focal length
        scale = f / (f + z)
        screen_x = int(WIDTH / 2 + x * scale)
        screen_y = int(HEIGHT / 2 + y * scale)
        projected_points.append((screen_x, screen_y))

    # Draw edges with changing colors
    color = colors[color_index]
    for edge in edges:
        start = projected_points[edge[0]]
        end = projected_points[edge[1]]
        pygame.draw.line(screen, color, start, end, 2)

    # Check if 50 seconds have passed, then display encrypted text and move it across the screen
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) / 1000  # convert to seconds
    if elapsed_time >= 50:
        text_rect.x += text_speed
        if text_rect.right > WIDTH:
            text_rect.x = 0 - text_rect.width

    
    # Check if 1 second has passed, then change the color
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) / 1000  # convert to seconds
    if elapsed_time >= 0.6:
        color_index = (color_index + 1) % len(colors)
        start_time = current_time

        screen.blit(encrypted_text, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
