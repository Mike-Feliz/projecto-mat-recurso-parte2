# Import pygame into our program
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *

# Define a main function, just to keep things nice and tidy
def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("FPScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,-1,0)

    #create a cube
    cube1 = Object3d("Cubo")
    cube1.scale = vector3(2, 2, 2)
    cube1.position = vector3(-2, 1,12)
    cube1.mesh = Mesh.create_cube((1, 1, 1))
    cube1.material = Material(color(1,0,0,1), "CuboMaterial1")
    
    #create a cube
    cube3 = Object3d("Cubo2")
    cube3.scale = vector3(3, 3, 3)
    cube3.position += vector3(8, 1, 14)
    cube3.mesh = Mesh.create_cube((1, 1, 1))
    cube3.material = Material(color(1,0,1,0), "CuboMaterial2")
    #create a cube
    cube2 = Object3d("Cubo3")
    cube2.scale = vector3(6, 6, 6)
    cube2.position += vector3(-4, 4, 16)
    cube2.mesh = Mesh.create_Cube((1, 1, 1))
    cube2.material = Material(color(1,1,0,1), "CuboMaterial3")
    
    
    
    #create a cube
    cube4 = Object3d("Cubo4")
    cube4.scale = vector3(10, 10, 10)
    cube4.position += vector3(10, 6, 18)
    cube4.mesh = Mesh.create_cube((1, 1, 1))
    cube4.material = Material(color(1,1,1,0), "CuboMaterial4")
    
    objList = [cube1, cube2, cube3, cube4]

    
    angle = 15
    axis = vector3(0,0,0)
    

    # Timer
    delta_time = 0
    prev_time = time.time()

    wKey = False
    aKey = False
    sKey = False
    dKey = False
   
    keys = [wKey, aKey, sKey, dKey]

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return
                if (event.key ==pygame.K_w):
                    wKey = True
                if (event.key ==pygame.K_a):
                    waKey = True
                if (event.key ==pygame.K_s):
                    sKey = True
                if (event.key ==pygame.K_d):
                    wdKey = True
            elif event.type == pygame.KEYUP:
                if (event.key ==pygame.K_w):
                    wKey = False
                if (event.key ==pygame.K_a):
                    aKey = False
                if (event.key ==pygame.K_s):
                    sKey = False
                if (event.key ==pygame.K_d):
                    dKey = False
                    
        for obj in objList:
            objM = obj.forward() - scene.camera.position  
            objM.normalize()
            cameraVec = scene.camera.forward()
            
            if dot_product(objM,cameraVec) > 0:
                if obj not in scene.objects:
                    scene.add_object(obj)
                    
                    for obj2 in scene.objects:
                        if obj2.position.magnitude() - scene.camera.position.magnitude() < obj.position.magnitude() - scene.camera.position.magnitude():
                            scene.remove_object(obj2)
                            
            else:
                if obj in scene.objects:
                    scene.remove_object(obj)
        
        if scene.camera.position.y != 1:
            scene.camera.position.y = 1
        if wKey:
            scene.camera.position += scene.camera.forward() * 0.1
        if aKey:
            scene.camera.position += scene.camera.left() * 0.1
        if sKey:
            scene.camera.position += scene.camera.back() * 0.1
        if dKey:
            scene.camera.position += scene.camera.right() * 0.1
        
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        mp = pygame.mouse.get_rel()
        
        if (mp[0]) > 0:
            axis = vector3(0,-1,0)
            scene.camera.rotation = q * scene.camera.rotation
        if (mp[0]) < 0:
            axis = vector3(0,1,0)
            scene.camera.rotation = q * scene.camera.rotation
        if (mp[1]) > 0:
            axis = vector3(-1,0,0)
            scene.camera.rotation = q * scene.camera.rotation
        if (mp[1]) < 0:
            axis = vector3(1,0,0)
            scene.camera.rotation = q * scene.camera.rotation
        
        if (mp[0]) > 0 and (mp[1]) > 0:
            axis = vector3(-1,-1,0)
            scene.camera.rotation = q * scene.camera.rotation
        if (mp[0]) < 0 and (mp[1]) < 0:
            axis = vector3(1,1,0)
            scene.camera.rotation = q * scene.camera.rotation
        if (mp[0]) > 0 and (mp[1]) < 0:
            axis = vector3(1,-1,0)
            scene.camera.rotation = q * scene.camera.rotation
        if (mp[0]) < 0 and (mp[1]) > 0:
            axis = vector3(-1,1,0)
            scene.camera.rotation = q * scene.camera.rotation
            
                    
        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        # Rotates the object, considering the time passed (not linked to frame rate)
        q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
    

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()

# Run the main function
main()
