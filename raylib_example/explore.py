# import raylibpy as rl

# screen_width = 800
# screen_height = 600
# rl.init_window(screen_width, screen_height, "A window")
# bird_position = 400
# bird_radius = 7
# bird_color = "RED"

# while not rl.window_should_close():
#     rl.begin_drawing()
#     rl.draw_circle_v(bird_position, bird_radius, bird_color)

# rl.close_window()



import raylibpy as rl

import pdb
pdb.set_trace()
# Initialization
screen_width, screen_height = 800, 600
rl.init_window(screen_width, screen_height, b"Raylib Circle Example")
circle_x, circle_y = screen_width // 2, screen_height // 2
rl.set_target_fps(60)
move_speed = 4
circle_radius=20

# Main game loop
while not rl.window_should_close():
    # Draw
    rl.begin_drawing()

    rl.clear_background(rl.RAYWHITE)
    if rl.is_key_down(rl.KEY_SPACE):
        circle_x += move_speed
    if rl.is_key_down(rl.KEY_UP):
        circle_x += move_speed
    if rl.is_key_down(rl.KEY_DOWN):
        circle_x += move_speed

    # Draw a circle in the center of the window
    rl.draw_circle(circle_x, circle_x,circle_radius, rl.RED)

    rl.end_drawing()

# Close window and OpenGL context
rl.close_window()






