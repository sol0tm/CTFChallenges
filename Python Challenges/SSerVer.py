import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (54, 57, 63)
SIDE_PANEL_WIDTH = 200
FONT_SIZE = 30
FONT_COLOR = (255, 255, 255)
SERVER_LIST_COLOR = (47, 49, 54)
CHAT_SECTION_COLOR = (64, 68, 75)
MESSAGE_SECTION_WIDTH = WIDTH - SIDE_PANEL_WIDTH

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LJsFwHFcPM4") #BSE_58

# Fonts
font = pygame.font.SysFont(None, FONT_SIZE)

# Server list data
server_list = ["bxKg9VHY", "39xEdC", "4A2NhYdJtW", "2ESbsA"]
selected_server = None

# Example messages data
example_messages = [
    {"user": "User1", "message": "Hello, how are you?"},
    {"user": "User2", "message": "I'm good, thanks!"},
    {"user": "User1", "message": "Any plans for today?"}
]

# Main loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    screen.fill(BACKGROUND_COLOR)

    # Draw server list
    pygame.draw.rect(screen, SERVER_LIST_COLOR, (0, 0, SIDE_PANEL_WIDTH, HEIGHT))
    for i, server in enumerate(server_list):
        server_rect = pygame.Rect(10, 10 + i * 40, SIDE_PANEL_WIDTH - 20, 30)
        pygame.draw.rect(screen, (65, 69, 77) if selected_server != i else (114, 118, 125), server_rect)
        text = font.render(server, True, FONT_COLOR)
        screen.blit(text, (15, 15 + i * 40))

    # Draw chat section
    pygame.draw.rect(screen, CHAT_SECTION_COLOR, (SIDE_PANEL_WIDTH, 0, MESSAGE_SECTION_WIDTH, HEIGHT))

    # Draw example messages
    message_y = 10
    for message in example_messages:
        user_text = font.render(f"{message['user']}: ", True, FONT_COLOR)
        message_text = font.render(message["message"], True, FONT_COLOR)

        screen.blit(user_text, (SIDE_PANEL_WIDTH + 15, message_y))
        screen.blit(message_text, (SIDE_PANEL_WIDTH + 15 + user_text.get_width(), message_y))
        message_y += 40

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
