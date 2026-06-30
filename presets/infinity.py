from physics.body import Body
from utils.constants import WORLD_CENTER_X, WORLD_CENTER_Y

def infinity_orbit():

    return [

        Body(
            mass=3500,
            position=(WORLD_CENTER_X-180, WORLD_CENTER_Y),
            velocity=(0,650),
            color="red"
        ),

        Body(
            mass=3500,
            position=(WORLD_CENTER_X+180, WORLD_CENTER_Y),
            velocity=(0,-650),
            color="green"
        ),

        Body(
            mass=1000,
            position=(WORLD_CENTER_X, WORLD_CENTER_Y),
            velocity=(900,0),
            color="blue"
        )

    ]