import pygame
import numpy as np

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

#Format: Body(mass, (initial positions),(direction of velocity))
bodies = [
    Body(100, (100, 200), (100, 50)),
    Body(400, (500, 200), (-50, 80)),
    Body(200, (600, 400), (30, -100))
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
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2:
                dragging=False
                last_mouse_pos=pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x,mouse_y=pygame.mouse.get_pos()

                dx=mouse_x-last_mouse_pos[0]
                dy=mouse_y-last_mouse_pos[1]

                camera_x -= dx
                camera_y -= dy 

                last_mouse_pos = (mouse_x,mouse_y)
        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                zoom *= 1.1
            elif event.y < 0:
                zoom /= 1.1
    
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

    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE

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



    for body,color in zip(bodies,colors):
        screen_x=(body.position[0] - camera_x) * zoom
        screen_y=(body.position[1] - camera_y) * zoom
        if len(body.trail)>1:
            pygame.draw.lines(screen,color,False,[(int((p[0]-camera_x) * zoom), int((p[1]-camera_y) * zoom )) for p in body.trail],2)
        radius=max(2, int(40*zoom))
        pygame.draw.circle(screen,color,(int(screen_x), int(screen_y)),radius)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()