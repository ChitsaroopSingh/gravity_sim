import math
import numpy as np

G=50000

def compute_acceleration(body,bodies):
    acc_x=0
    acc_y=0

    for other in bodies:
        if other is body:
            continue #body doesn't exerts force on itself
        dx=other.position[0]-body.position[0]
        dy=other.position[1]-body.position[1]

        dist_sq=dx**2+dy**2
        dist=math.sqrt(dist_sq)

        if dist==0:
            continue #prevents division by zero

        #Newton's Law of Gravitation F=G*m1*m2/r^2
        #Since F=m1*a , we get
        # a = G*m2/r^2

        magnitude=(G*other.mass)/dist_sq

        acc_x += magnitude * (dx/dist)
        acc_y += magnitude * (dy/dist)

    return np.array([acc_x,acc_y])

