import raylibpy as rl
from Box2D import b2

# Constants for converting between Box2D coordinates and raylib coordinates
PPM = 20.0  # Pixels per meter
MPP = 1 / PPM  # Meters per pixel

# Box2D world setup
world = b2.world(gravity=(0, -10), doSleep=True)

# Create ground body
ground_body = world.CreateStaticBody(
    position=(0, -10),
    shapes=b2.polygonShape(box=(50, 1)),
)

# Create dynamic body (a box)
dynamic_body = world.CreateDynamicBody(
    position=(0, 10),
    shapes=b2.polygonShape(box=(1, 1)),
)

def draw_box(body):
    for fixture in body.fixtures:
        shape = fixture.shape
        vertices = [(body.transform * v) * PPM for v in shape.vertices]
        rl.draw_rectangle_lines(int(vertices[0][0]), int(vertices[0][1]),
                                int(vertices[2][0] - vertices[0][0]),
                                int(vertices[2][1] - vertices[0][1]),
                                rl.RAYWHITE)

# Initialize raylib
rl.init_window(800, 600, b"Box2D with raylib")
rl.set_target_fps(60)

# Main loop
while not rl.window_should_close():
    # Step the Box2D world
    time_step = 1.0 / 60.0
    velocity_iterations = 6
    position_iterations = 2
    world.Step(time_step, velocity_iterations, position_iterations)

    # Draw
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)

    # Draw ground
    draw_box(ground_body)

    # Draw dynamic body
    draw_box(dynamic_body)

    rl.end_drawing()

# Close raylib window
rl.close_window()
