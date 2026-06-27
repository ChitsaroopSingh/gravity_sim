from physics.gravity import compute_acceleration
import numpy as np

#using leapfrog velocity verlet integration instead of euler integration to conserve more energy
def update_bodies(bodies, dt):

    accelerations = []

    for body in bodies:
        accelerations.append(np.array(compute_acceleration(body,bodies)))

    
    for body, acc in zip(bodies, accelerations):
        body.velocity += 0.5 * acc * dt

    for body in bodies:
        body.position += body.velocity * dt

        body.trail.append(tuple(body.position))

        if len(body.trail) > 500 :
            body.trail.pop(0)

    new_accelerations = []

    for body in bodies:
        new_accelerations.append(np.array(compute_acceleration(body,bodies)))

    for body,acc in zip(bodies, new_accelerations):
        body.velocity += 0.5 * acc * dt