import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and grid settings
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 8
CELL_SIZE = WIDTH // GRID_SIZE
SPHERE_RADIUS = CELL_SIZE // 4

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font settings
font = pygame.font.SysFont("Arial", 24)

# Game variables
grid = [[[] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = 1  # Player 1 starts
game_over = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chain Reaction")

class Sphere:
    def __init__(self, player):
        self.player = player
        self.color = RED if player == 1 else BLUE

def draw_grid():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

            # Draw spheres in cells
            for i, sphere in enumerate(grid[x][y]):
                pygame.draw.circle(
                    screen,
                    sphere.color,
                    (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2),
                    SPHERE_RADIUS + i * 5
                )

def add_sphere(x, y):
    global current_player
    if not game_over and (len(grid[x][y]) == 0 or grid[x][y][0].player == current_player):
        grid[x][y].append(Sphere(current_player))
        check_for_chain_reaction(x, y)
        current_player = 2 if current_player == 1 else 1

def check_for_chain_reaction(x, y):
    global game_over
    if len(grid[x][y]) >= 4:
        overflow_sphere = grid[x][y].pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                grid[nx][ny].append(overflow_sphere)

        if len(grid[x][y]) > 0:
            check_for_chain_reaction(x, y)

def check_for_winner():
    global game_over
    player_spheres = {1: 0, 2: 0}
    for row in grid:
        for cell in row:
            if cell:
                player_spheres[cell[0].player] += len(cell)

    if player_spheres[1] == 0 or player_spheres[2] == 0:
        game_over = True

def main():
    global game_over
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                add_sphere(x // CELL_SIZE, y // CELL_SIZE)
                check_for_winner()

        # Draw player turn
        turn_text = font.render(f"Player {current_player}'s Turn", True, BLACK)
        screen.blit(turn_text, (10, 10))

        # Draw game over text
        if game_over:
            winner = 2 if current_player == 1 else 1
            game_over_text = font.render(f"Player {winner} Wins!", True, BLACK)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
