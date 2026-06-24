import pygame

def update_camera_keyboard(camera, dt):

    keys = pygame.key.get_pressed()

    camera_speed = 500 * dt

    if keys[pygame.K_a]:
        camera.x -= camera_speed

    if keys[pygame.K_d]:
        camera.x += camera_speed

    if keys[pygame.K_w]:
        camera.y -= camera_speed

    if keys[pygame.K_s]:
        camera.y += camera_speed