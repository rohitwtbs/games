import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5
jump_height = 15
gravity = 1

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
is_jumping = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    # Player movement
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Jumping
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        player_y -= jump_height
        jump_height -= gravity
        if jump_height <= -15:
            is_jumping = False
            jump_height = 15

    # Apply gravity
    if player_y < HEIGHT - player_size:
        player_y += gravity
        gravity += 1
    else:
        player_y = HEIGHT - player_size
        gravity = 1

    # Draw background
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
