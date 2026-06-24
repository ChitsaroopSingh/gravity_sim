import pygame
from rendering.camera import Camera
from physics.body import Body

def draw_bodies(screen, bodies, camera):

    for body in bodies:

        screen_x, screen_y = camera.world_to_screen(body.position)

        if len(body.trail) > 1:

            trail_points = [camera.world_to_screen(p) for p in body.trail]

            pygame.draw.lines(screen,body.color,False,trail_points,2)

        radius = max(2,int(body.radius * camera.zoom))

        pygame.draw.circle(screen,body.color,(int(screen_x), int(screen_y)),radius)
