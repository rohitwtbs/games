import raylibpy as rl

# Initialization
screen_width, screen_height = 800, 600
rl.init_window(screen_width, screen_height, b"Raylib 3D Scene with Moving Character")

# Define camera
camera = rl.Camera()
camera.position = rl.Vector3(0.0, 10.0, 10.0)
camera.target = rl.Vector3(0.0, 0.0, 0.0)
camera.up = rl.Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.projection = rl.CAMERA_PERSPECTIVE

# Load 3D model from .glb file
model = rl.LoadModel(b"assets/mario/model.glb")

# Set model position
model.position = rl.Vector3(0.0, 0.0, 0.0)

# Set movement speed
move_speed = 5.0

# Main game loop
while not rl.window_should_close():
    # Update

    # Character movement
    if rl.is_key_down(rl.KEY_RIGHT):
        model.position.x += move_speed * rl.get_frame_time()
    elif rl.is_key_down(rl.KEY_LEFT):
        model.position.x -= move_speed * rl.get_frame_time()

    if rl.is_key_down(rl.KEY_UP):
        model.position.z -= move_speed * rl.get_frame_time()
    elif rl.is_key_down(rl.KEY_DOWN):
        model.position.z += move_speed * rl.get_frame_time()

    # Draw
    rl.begin_drawing()

    rl.clear_background(rl.RAYWHITE)

    # Begin 3D mode
    rl.begin_mode_3d(camera)

    # Draw the 3D model
    rl.draw_model(model, rl.Vector3(0.0, 0.0, 0.0), 1.0, rl.WHITE)

    # End 3D mode
    rl.end_mode_3d()

    rl.end_drawing()

# Unload model and close window
rl.unload_model(model)
rl.close_window()
