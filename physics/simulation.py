from physics.gravity import compute_acceleration
import numpy as np

def update_bodies(bodies, dt):

    accelerations = []

    for body in bodies:
        acc = compute_acceleration(body, bodies)
        accelerations.append(np.array(acc))
    
    for body, acc in zip(bodies, accelerations):
        body.velocity += acc * dt
        body.position += body.velocity * dt

        body.trail.append((body.position[0],body.position[1]))

        if len(body.trail) > 500 :
            body.trail.pop(0)
            