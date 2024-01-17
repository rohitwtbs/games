import taichi as ti
import random

ti.init(arch=ti.gpu)  # Use ti.cpu for a CPU implementation

# Constants
W, H = 800, 600
bird_size = 20
pipe_width = 50
pipe_height = 300
pipe_gap = 150
gravity = 0.2
jump_strength = 5
pipe_speed = 2

# Variables
bird_pos = ti.Vector.field(2, dtype=float, shape=())
bird_vel = ti.Vector.field(2, dtype=float, shape=())
pipes = ti.Vector.field(4, dtype=float, shape=(10, 2))  # 10 pipes, each represented by (x, y, top_height, bottom_height)
score = ti.field(dtype=int, shape=())

# Initialize variables
@ti.kernel
def init():
    bird_pos[None] = [W // 4, H // 2]
    bird_vel[None] = [0, 0]
    score[None] = 0

    for i in range(10):
        pipes[i, 0][0] = W + i * (W // 2)
        pipes[i, 0][1] = random.randint(pipe_gap, H - pipe_gap)
        pipes[i, 1][0] = pipe_width
        pipes[i, 1][1] = H - pipes[i, 0][1] - pipe_gap
        pipes[i, 1] = [pipe_width, H - pipes[i, 0][1] - pipe_gap]

# Update bird position and check collisions
@ti.kernel
def update():
    bird_pos[None] += bird_vel[None]
    bird_vel[None][1] -= gravity

    for i in range(10):
        pipes[i, 0][0] -= pipe_speed
        if pipes[i, 0][0] < -pipe_width:
            pipes[i, 0][0] += 10 * (W // 2)
            pipes[i, 1][0] = pipe_width
            pipes[i, 1][1] = H - pipes[i, 0][1] - pipe_gap

        # Check collision with pipes
        if bird_pos[None][0] < pipes[i, 0][0] + pipes[i, 1][0] and \
           bird_pos[None][0] + bird_size > pipes[i, 0][0] and \
           (bird_pos[None][1] < pipes[i, 0][1] or bird_pos[None][1] + bird_size > pipes[i, 0][1] + pipe_gap):
            init()

    # Check collision with top and bottom of the screen
    if bird_pos[None][1] < 0 or bird_pos[None][1] + bird_size > H:
        init()

    # Check if the bird passes through the pipes
    for i in range(10):
        if bird_pos[None][0] > pipes[i, 0][0] and bird_pos[None][0] < pipes[i, 0][0] + pipes[i, 1][0]:
            score[None] += 1


# Main game loop
gui = ti.GUI('Flappy Bird', res=(W, H))

init()

while gui.running:
    for e in gui.get_events(ti.GUI.PRESS):
        if e.key == ti.GUI.SPACE:
            bird_vel[None][1] = jump_strength

    update()

    # Rendering
    gui.circles([bird_pos[None]], radius=bird_size, color=0xFF0000)
    for i in range(10):
        gui.rect((pipes[i, 0][0], 0), pipes[i, 1], color=0x00FF00)
        gui.rect((pipes[i, 0][0], pipes[i, 0][1] + pipe_gap), pipes[i, 1], color=0x00FF00)

    gui.text(content=f'Score: {score[None]}', pos=(W - 100, 50), color=0xFFFFFF)

    gui.show()
