import raylibpy as raylib

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 200

# Game state
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'
game_over = False
winner = None

# Function to draw the Tic Tac Toe board in 3D
def draw_board():
    # Draw the board plane
    raylib.draw_cube(raylib.Vector3(0, -0.1, 0), 3, 0.1, 3, raylib.BLACK)
    
    # Draw grid lines
    for i in range(1, 3):
        raylib.draw_cube(raylib.Vector3(i, 0, 0), 0.02, 0.2, 3, raylib.BLACK)
        raylib.draw_cube(raylib.Vector3(0, 0, i), 3, 0.2, 0.02, raylib.BLACK)

    # Draw X and O pieces
    for row in range(3):
        for col in range(3):
            cell_value = board[row][col]
            if cell_value == 'X':
                raylib.draw_cube(raylib.Vector3(col + 0.5, 0, row + 0.5), 0.8, 0.1, 0.8, raylib.RED)
            elif cell_value == 'O':
                raylib.draw_sphere(raylib.Vector3(col + 0.5, 0.1, row + 0.5), 0.4, raylib.GREEN)

# Function to check if there is a winner
def check_winner():
    global game_over, winner

    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            winner = board[row][0]
            game_over = True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            winner = board[0][col]
            game_over = True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = board[0][0]
        game_over = True
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = board[0][2]
        game_over = True

# Main game loop
raylib.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tic Tac Toe 3D")

while not raylib.window_should_close():
    raylib.begin_drawing()
    raylib.clear_background(raylib.RAYWHITE)

    if not game_over:
        pass
        # Handle player input
        # if raylib.is_mouse_button_pressed(raylib.MOUSE_LEFT_BUTTON):
        #     mouseX, mouseY = raylib.get_mouse_position()
        #     clicked_row = int(mouseY // CELL_SIZE)
        #     clicked_col = int(mouseX // CELL_SIZE)
            
            # if board[clicked_row][clicked_col] == ' ':
            #     board[clicked_row][clicked_col] = current_player
            #     current_player = 'O' if current_player == 'X' else 'X'
            #     check_winner()

    # Draw the board
    draw_board()

    # Display winner if game over
    if game_over:
        raylib.draw_text(f"Winner: {winner}", 10, SCREEN_HEIGHT // 2 - 20, 30, raylib.BLACK)

    raylib.end_drawing()

raylib.close_window()
