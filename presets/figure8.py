from physics.body import Body
from utils.constants import WORLD_CENTER_X, WORLD_CENTER_Y

def figure8():

    s = 140      # scale
    v = 1050     # velocity scale

    return [

        Body(
            mass=1000,
            position=(WORLD_CENTER_X-s, WORLD_CENTER_Y),
            velocity=(v*0.347, v*0.533),
            color="red"
        ),

        Body(
            mass=1000,
            position=(WORLD_CENTER_X+s, WORLD_CENTER_Y),
            velocity=(v*0.347, v*0.533),
            color="green"
        ),

        Body(
            mass=1000,
            position=(WORLD_CENTER_X, WORLD_CENTER_Y),
            velocity=(-2*v*0.347, -2*v*0.533),
            color="blue"
        )

    ]