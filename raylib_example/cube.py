import raylibpy as raylib

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize window
raylib.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Raylib Cube Example")

# Main loop
while not raylib.window_should_close():
    # Start drawing
    raylib.begin_drawing()

    # Clear background
    # raylib.clear_background(raylib.RAYWHITE)

    # Draw cube
    raylib.draw_cube(raylib.Vector3(400, 300, 0), 10, 10, 10, raylib.RED)

    # End drawing
    raylib.end_drawing()

# Close window
raylib.close_window()
