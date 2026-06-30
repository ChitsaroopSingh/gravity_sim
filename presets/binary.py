from physics.body import Body
from utils.constants import WORLD_CENTER_X, WORLD_CENTER_Y

def binary_stars():
    return [
        Body(
            mass=5000,
            position=(WORLD_CENTER_X - 100, WORLD_CENTER_Y),
            velocity=(0, 790),
            color="orange"
        ),
        Body(
            mass=5000,
            position=(WORLD_CENTER_X + 100, WORLD_CENTER_Y),
            velocity=(0, -790),
            color="yellow"
        )
    ]