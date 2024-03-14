import pyray as raylib

for i in dir(raylib):
    print(i)
    with open('pyray.txt', 'a') as file:
        file.write(i + "\n")




# for i in dir(raylib):
#     with open('raylib_commands.txt', 'a') as file:
#         file.write(i + "\n")

# Program main entry point
def main():
    # Initialization
    screenWidth = 800
    screenHeight = 450

    raylib.init_window(screenWidth, screenHeight, "raylib [models] example - first person maze")

    # Define the camera to look into our 3d world
    camera = raylib.Camera3D()
    camera.position = raylib.Vector3(0.2, 0.4, 0.2)   # Camera position
    camera.target = raylib.Vector3(0.185, 0.4, 0.0)   # Camera looking at point
    camera.up = raylib.Vector3(0.0, 1.0, 0.0)         # Camera up vector (rotation towards target)
    camera.fovy = 45.0                                # Camera field-of-view Y
    camera.projection = raylib.CAMERA_PERSPECTIVE     # Camera projection type

    imMap = raylib.load_image("cubicmap.png")     # Load cubicmap image (RAM)
    cubicmap = raylib.load_texture_from_image(imMap)        # Convert image to texture to display (VRAM)
    mesh = raylib.gen_mesh_cubicmap(imMap, raylib.Vector3(1.0, 1.0, 1.0))
    model = raylib.load_model_from_mesh(mesh)

    # Load map texture
    texture = raylib.load_texture("cubicmap_atlas.png")

    # Set map diffuse texture
    import pdb
    # pdb.set_trace()
    MATERIAL_MAP_DIFFUSE = raylib.MATERIAL_MAP_ALBEDO
    model.materials[0].maps[MATERIAL_MAP_DIFFUSE].texture = texture

    # Get map image data to be used for collision detection
    mapPixels = raylib.load_image_colors(imMap)
    raylib.unload_image(imMap)             # Unload image from RAM

    mapPosition = raylib.Vector3(-16.0, 0.0, -8.0)   # Set model position

    raylib.disable_cursor()                # Limit cursor to relative movement inside the window

    raylib.set_target_fps(60)              # Set our game to run at 60 frames-per-second

    # Main game loop
    while not raylib.window_should_close():    # Detect window close button or ESC key
        # Update
        oldCamPos = camera.position    # Store old camera position

        raylib.update_camera(camera, raylib.CAMERA_FIRST_PERSON)

        # Check player collision (we simplify to 2D collision detection)
        playerPos = raylib.Vector2(camera.position.x, camera.position.z)
        playerRadius = 0.1  # Collision radius (player is modeled as a cylinder for collision)

        playerCellX = int(playerPos.x - mapPosition.x + 0.5)
        playerCellY = int(playerPos.y - mapPosition.z + 0.5)

        # Out-of-limits security check
        if playerCellX < 0:
            playerCellX = 0
        elif playerCellX >= cubicmap.width:
            playerCellX = cubicmap.width - 1

        if playerCellY < 0:
            playerCellY = 0
        elif playerCellY >= cubicmap.height:
            playerCellY = cubicmap.height - 1

        # Check map collisions using image data and player position
        # TODO: Improvement: Just check player surrounding cells for collision
        for y in range(cubicmap.height):
            for x in range(cubicmap.width):
                # pass
                try:
                    if mapPixels[y * cubicmap.width + x].r == 255 and raylib.check_collision_circle_rec(playerPos, playerRadius,raylib.Rectangle(mapPosition.x - 0.5 + x * 1.0,mapPosition.z - 0.5 + y * 1.0,1.0, 1.0)):
                        # Collision detected, reset camera position
                        camera.position = oldCamPos
                except Exception as e:
                    print(e)
                    import pdb
                    pdb.set_trace()

        # Draw
        raylib.begin_drawing()

        raylib.clear_background(raylib.RAYWHITE)

        raylib.begin_mode_3d(camera)
        raylib.draw_model(model, mapPosition, 1.0, raylib.WHITE)  # Draw maze map
        raylib.end_mode_3d()

        raylib.draw_texture_ex(cubicmap, raylib.Vector2(raylib.get_screen_width() - cubicmap.width * 4.0 - 20, 20.0), 0.0,
                               4.0, raylib.WHITE)
        raylib.draw_rectangle_lines(raylib.get_screen_width() - cubicmap.width * 4 - 20, 20, cubicmap.width * 4,
                                    cubicmap.height * 4, raylib.GREEN)

        # Draw player position radar
        raylib.draw_rectangle(raylib.get_screen_width() - cubicmap.width * 4 - 20 + playerCellX * 4, 20 + playerCellY * 4,
                              4, 4, raylib.RED)

        raylib.draw_fps(10, 10)

        raylib.end_drawing()

    # De-Initialization
    raylib.unload_image_colors(mapPixels)  # Unload color array

    raylib.unload_texture(cubicmap)        # Unload cubicmap texture
    raylib.unload_texture(texture)         # Unload map texture
    raylib.unload_model(model)             # Unload map model

    raylib.close_window()                  # Close window and OpenGL context

    return 0


if __name__ == "__main__":
    main()
