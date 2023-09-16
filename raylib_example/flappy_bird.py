import raylibpy as rl

# Set up the game window
screen_width = 800
screen_height = 600
rl.init_window(screen_width, screen_height, "Flappy Bird")

# Define game variables
gravity = 800
jump_force = 400
bird_position = rl.Vector2(100, screen_height // 2)
bird_radius = 20
bird_color = rl.RED

pipe_width = 80
pipe_spacing = 200
pipe_speed = 300
pipes = []

def update_bird():
    global bird_position, gravity, jump_force

    bird_position.y += gravity * rl.get_frame_time()

    if rl.is_key_pressed(rl.KEY_SPACE):
        bird_position.y -= jump_force * rl.get_frame_time()

def update_pipes():
    global pipes, pipe_width, pipe_spacing, pipe_speed, screen_width

    # Remove pipes that are off-screen
    pipes = [pipe for pipe in pipes if pipe.x + pipe_width > 0]

    # Create new pipes
    if len(pipes) == 0 or screen_width - pipes[-1].x >= pipe_spacing:
        top_pipe_height = rl.get_random_value(100, 400)
        bottom_pipe_height = screen_height - top_pipe_height - pipe_spacing
        pipes.append(rl.Rectangle(screen_width, 0, pipe_width, top_pipe_height))
        pipes.append(rl.Rectangle(screen_width, screen_height - bottom_pipe_height, pipe_width, bottom_pipe_height))

    # Move pipes to the left
    for i in range(0, len(pipes), 2):
        pipes[i].x -= pipe_speed * rl.get_frame_time()
        pipes[i + 1].x -= pipe_speed * rl.get_frame_time()

def check_collision():
    global bird_position, bird_radius, pipes, pipe_width, pipe_spacing

    bird_rect = rl.Rectangle(bird_position.x - bird_radius, bird_position.y - bird_radius, bird_radius * 2, bird_radius * 2)

    for i in range(0, len(pipes), 2):
        top_pipe = pipes[i]
        bottom_pipe = pipes[i + 1]
        
        if rl.check_collision_circle_rec(bird_position, bird_radius, top_pipe) or rl.check_collision_circle_rec(bird_position, bird_radius, bottom_pipe):
            return True

    return False

while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)

    # Update game logic
    update_bird()
    update_pipes()

    # Check for collisions
    if check_collision():
        rl.draw_text("Game Over!", screen_width // 2 - 100, screen_height // 2 - 50, 40, rl.RED)

    # Draw pipes
    for pipe in pipes:
        rl.draw_rectangle_rec(pipe, rl.GREEN)

    # Draw the bird
    rl.draw_circle_v(bird_position, bird_radius, bird_color)

    rl.end_drawing()

rl.close_window()
