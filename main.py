import pygame
import numpy as np
import math

from physics.body import Body
from physics.gravity import compute_acceleration

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Gravity Simulator")

pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#camera offset
camera_x=0
camera_y=0
dragging = False
last_mouse_pos = None
zoom = 1.0

#custom body
creating_body = False
start_world_pos = None

#background
bg_image=pygame.image.load("assets/space.jpeg").convert()
bg_image = pygame.transform.scale(bg_image, (1280,720))



#Format: Body(mass, (initial positions),(direction of velocity))
bodies = [
    Body(100, (400, 200), (100, 50)),
    Body(400, (200, 300), (-50, 80)),
    Body(200, (700, 400), (30, -100))
]
colors=["green","red","blue"]

while running:
    # dt = clock.tick(60) / 1000  # seconds
    dt=0.01
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_x:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                dragging=True
                last_mouse_pos=pygame.mouse.get_pos()
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                world_x = camera_x + mouse_x / zoom
                world_y = camera_y + mouse_y / zoom
                creating_body = True
                start_world_pos = (world_x, world_y)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2:
                dragging=False
                last_mouse_pos=pygame.mouse.get_pos()
            if event.button == 1 and creating_body:
                mouse_x,mouse_y = pygame.mouse.get_pos()

                end_world_x = camera_x + mouse_x / zoom
                end_world_y = camera_y + mouse_y / zoom

                vx = (end_world_x - start_world_pos[0]) * 2
                vy = (end_world_y - start_world_pos[1]) * 2

                bodies.append(Body(mass=100,
                                   position=start_world_pos,
                                   velocity=(vx,vy)
                                )
                            )
                colors.append("black")
                creating_body = False


        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x,mouse_y=pygame.mouse.get_pos()

                dx=mouse_x-last_mouse_pos[0]
                dy=mouse_y-last_mouse_pos[1]

                camera_x -= dx
                camera_y -= dy 

                last_mouse_pos = (mouse_x,mouse_y)
        elif event.type == pygame.MOUSEWHEEL:
            mouse_x,mouse_y=pygame.mouse.get_pos()

            world_x = camera_x + mouse_x/zoom
            world_y = camera_y + mouse_y/zoom

            if event.y > 0:
                zoom *= 1.1
            elif event.y < 0:
                zoom /= 1.1
            
            camera_x = world_x - mouse_x / zoom
            camera_y = world_y - mouse_y / zoom


    
    #camera panning
    keys = pygame.key.get_pressed()

    camera_speed = 500 * dt

    if keys[pygame.K_a]:
        camera_x -= camera_speed
    if keys[pygame.K_d]:
        camera_x += camera_speed
    if keys[pygame.K_w]:
        camera_y -= camera_speed
    if keys[pygame.K_s]:
        camera_y += camera_speed

    
    #setting the background
    screen.blit(bg_image, (0, 0))


    accelerations=[]

    #Computing all accelerations first
    for body in bodies:
        acc=compute_acceleration(body,bodies)
        accelerations.append(np.array(acc))
        # print(compute_acceleration(body,bodies))
    
    #Updating velocities and postions
    for body,acc in zip(bodies,accelerations):
        body.velocity += acc*dt
        body.position += body.velocity*dt

        body.trail.append((body.position[0], body.position[1]))
        if len(body.trail)>500:
            body.trail.pop(0)
    #collisions
    for i in range(len(bodies)):
        for j in range(i+1,len(bodies)):
            body1=bodies[i]
            body2=bodies[j]

            dx=body2.position[0]-body1.position[0]
            dy=body2.position[1]-body1.position[1]

            distance=math.sqrt(dx**2 + dy**2) 
            if distance < body1.radius + body2.radius :
                print("collision")
                break

    
    
        
   



    for body,color in zip(bodies,colors):
        screen_x=(body.position[0] - camera_x) * zoom
        screen_y=(body.position[1] - camera_y) * zoom
        if len(body.trail)>1:
            pygame.draw.lines(screen,color,False,[(int((p[0]-camera_x) * zoom), int((p[1]-camera_y) * zoom )) for p in body.trail],2)
        # radius=max(2, int(40*zoom))
        pygame.draw.circle(screen,color,(int(screen_x), int(screen_y)),body.radius)

    if creating_body:
        mouse_x,mouse_y=pygame.mouse.get_pos()

        start_screen_x = int((start_world_pos[0]- camera_x) * zoom )
        start_screen_y = int((start_world_pos[1]- camera_y) * zoom )

        pygame.draw.line(screen,"black",(start_screen_x,start_screen_y),(mouse_x,mouse_y),3)



    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()