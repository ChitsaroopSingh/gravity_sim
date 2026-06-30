import random
from physics.body import Body
from utils.constants import WORLD_CENTER_X, WORLD_CENTER_Y

def random_system():

    colors = ["red", "green", "blue"]

    bodies = []

    for color in colors:

        mass = random.randint(300,5000)

        x = random.randint(
            WORLD_CENTER_X-300,
            WORLD_CENTER_X+300
        )

        y = random.randint(
            WORLD_CENTER_Y-220,
            WORLD_CENTER_Y+220
        )

        vx = random.randint(-1800,1800)
        vy = random.randint(-1800,1800)

        bodies.append(
            Body(
                mass=mass,
                position=(x,y),
                velocity=(vx,vy),
                color=color
            )
        )

    return bodies