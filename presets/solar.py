# from physics.body import Body


# def sun_earth():

#     return [

#         Body(
#             mass=10000,
#             position=(490,360),
#             velocity=(0,0),
#             color="yellow"
#         ),

#         Body(
#             mass=10,
#             position=(750,360),
#             velocity=(0,-1387),
#             color="blue"
#         )

#     ]

from physics.body import Body
from utils.constants import WORLD_CENTER_X, WORLD_CENTER_Y

def solar():

    return [

        Body(
            mass=25000,
            position=(WORLD_CENTER_X, WORLD_CENTER_Y),
            velocity=(0,0),
            color="yellow"
        ),

        Body(
            mass=3,
            position=(WORLD_CENTER_X+80, WORLD_CENTER_Y),
            velocity=(0,-3950),
            color="gray"
        ),

        Body(
            mass=8,
            position=(WORLD_CENTER_X+130, WORLD_CENTER_Y),
            velocity=(0,-3100),
            color="orange"
        ),

        Body(
            mass=10,
            position=(WORLD_CENTER_X+210, WORLD_CENTER_Y),
            velocity=(0,-2450),
            color="blue"
        ),

        Body(
            mass=6,
            position=(WORLD_CENTER_X+320, WORLD_CENTER_Y),
            velocity=(0,-1950),
            color="red"
        )

    ]