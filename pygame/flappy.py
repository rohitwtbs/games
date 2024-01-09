import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 900
FPS = 60
GRAVITY = 0.1
BIRD_JUMP = 10
PIPE_SPEED = 5
PIPE_GAP = 150

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_image = pygame.image.load("bird.png")  # Replace with your bird image
pipe_image = pygame.image.load("pipe.png")  # Replace with your pipe image

# Resize images
bird_image = pygame.transform.scale(bird_image, (50, 50))
pipe_image = pygame.transform.scale(pipe_image, (50, 300))

# Create bird
bird_rect = bird_image.get_rect()
bird_rect.center = (WIDTH // 4, HEIGHT // 2)
bird_y_speed = 50

# Create pipes
pipes = []

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_speed = -BIRD_JUMP

    # Update bird position and speed
    bird_y_speed += GRAVITY
    bird_rect.y += bird_y_speed

    # Generate pipes
    if len(pipes) == 0 or pipes[-1]["x"] < WIDTH - 200:
        pipe_height = random.randint(50, HEIGHT - PIPE_GAP - 50)
        pipes.append({"x": WIDTH, "top_height": pipe_height, "bottom_height": HEIGHT - pipe_height - PIPE_GAP})

    # Update pipe positions
    for pipe in pipes:
        pipe["x"] -= PIPE_SPEED

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe["x"] + pipe_image.get_width() > 0]

    # Check for collisions with pipes
    for pipe in pipes:
        if bird_rect.colliderect(pygame.Rect(pipe["x"], 0, pipe_image.get_width(), pipe["top_height"])) or \
           bird_rect.colliderect(pygame.Rect(pipe["x"], pipe["bottom_height"], pipe_image.get_width(), HEIGHT - pipe["bottom_height"])):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(WHITE)

    for pipe in pipes:
        screen.blit(pipe_image, (pipe["x"], 0))
        screen.blit(pygame.transform.flip(pipe_image, False, True), (pipe["x"], pipe["bottom_height"]))

    screen.blit(bird_image, bird_rect)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
