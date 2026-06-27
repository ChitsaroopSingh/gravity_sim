import pygame
import numpy as np
import math

from physics.body import Body
from physics.gravity import compute_acceleration
from physics.collisions import handle_collisions
from physics.simulation import update_bodies
from rendering.camera import Camera
from rendering.renderer import draw_bodies
from controls.camera_controls import update_camera_keyboard
from utils.constants import *
from ui.panel import Panel

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Gravity Simulator")

pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


dragging = False
last_mouse_pos = None
camera=Camera()
panel=Panel()

#pausing feature
paused=False

#time scaling
time_scale = 1

#custom body
creating_body = False
start_world_pos = None

#background
bg_image=pygame.image.load("assets/space.jpeg").convert()
bg_image = pygame.transform.scale(bg_image, (1280,720))

#initializing font
font = pygame.font.SysFont(None, 30)

#initializing states
state="setup"

current_mass = 100
# input_x = 400
# input_y = 300
# input_vx = 0
# input_vy = 0

bodies = []
#Format: Body(mass, (initial positions),(direction of velocity))
# bodies = [
#     Body(100, (400, 200), (100, 50),color="green"),
#     Body(400, (200, 300), (-50, 80),color="red"),
#     Body(200, (700, 400), (30, -100),color="blue")
# ]

body_colors = ["red", "green", "blue"]
while running:


    dt=0.002 * time_scale

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_x:
                running = False
            elif event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_COMMA:
                time_scale /= 2
            elif event.key == pygame.K_PERIOD:
                time_scale *= 2
            elif event.key == pygame.K_RETURN:
                if len(bodies)>=2:
                    state = "simulation"
        
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                dragging=True
                last_mouse_pos=pygame.mouse.get_pos()
            if event.button == 1 and len(bodies) < 3:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                world_x, world_y = camera.screen_to_world((mouse_x, mouse_y))
                creating_body = True
                start_world_pos = (world_x, world_y)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2:
                dragging=False
                last_mouse_pos=pygame.mouse.get_pos()
            if event.button == 1 and creating_body:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                end_world_x, end_world_y = camera.screen_to_world((mouse_x, mouse_y))

                vx = (end_world_x - start_world_pos[0]) * 2
                vy = (end_world_y - start_world_pos[1]) * 2
                
                color = body_colors[len(bodies)]
                bodies.append(Body(mass=current_mass,position=start_world_pos,velocity=(vx,vy),color=color))
                creating_body = False


        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x,mouse_y=pygame.mouse.get_pos()

                dx=mouse_x-last_mouse_pos[0]
                dy=mouse_y-last_mouse_pos[1]

                camera.x -= dx
                camera.y -= dy 

                last_mouse_pos = (mouse_x,mouse_y)
        elif event.type == pygame.MOUSEWHEEL:
            if state == "setup" :
                current_mass += event.y * 10
                current_mass = max(10, current_mass)
            
            else:
                mouse_x,mouse_y=pygame.mouse.get_pos()

                world_x, world_y = camera.screen_to_world((mouse_x, mouse_y))

                if event.y > 0:
                    camera.zoom *= 1.1
                elif event.y < 0:
                    camera.zoom /= 1.1
                
                camera.x = world_x - mouse_x / camera.zoom
                camera.y = world_y - mouse_y / camera.zoom
    # if state == "setup":
    #     screen.fill("black")

    #     text = font.render("SETUP SCREEN", True, "white")
    #     screen.blit(text, (500, 100))

    #     hint = font.render("Press ENTER to start simulation", True, "white")
    #     screen.blit(hint, (420, 200))

    #     pygame.display.flip()
    #     clock.tick(60)

    #     continue
    update_camera_keyboard(camera, dt)
 
    #setting the background
    screen.blit(bg_image, (0, 0))
    if paused:
        text = font.render("PAUSED",True,"yellow")
        rect = text.get_rect(center=(640,60))
        screen.blit(text,rect)
    if state == "simulation":
        if not paused:
            update_bodies(bodies, dt)

        bodies = handle_collisions(bodies)
    
    draw_bodies(screen,bodies,camera)
    
    stats = {
    "FPS": int(clock.get_fps()),
    "Bodies": len(bodies),
    "Time": f"x{time_scale}",
    "Zoom": round(camera.zoom, 2),
    "Paused": paused}

    panel.draw(screen,stats)
    if creating_body:
        mouse_x,mouse_y=pygame.mouse.get_pos()

        start_screen_x, start_screen_y = camera.world_to_screen(start_world_pos)

        pygame.draw.line(screen,"black",(start_screen_x,start_screen_y),(mouse_x,mouse_y),3)
    
    if state == "setup":

        text1 = font.render(
            f"Current Mass: {current_mass}",
            True,
            "white"
        )

        text2 = font.render(
            f"Bodies: {len(bodies)}/3",
            True,
            "white"
        )

        text3 = font.render(
            "Click + Drag = Create Body",
            True,
            "white"
        )

        text4 = font.render(
            "Mouse Wheel = Change Mass",
            True,
            "white"
        )

        text5 = font.render(
            "ENTER = Start Simulation",
            True,
            "yellow"
        )

        screen.blit(text1, (20,20))
        screen.blit(text2, (20,50))
        screen.blit(text3, (20,90))
        screen.blit(text4, (20,120))
        screen.blit(text5, (20,150))

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()