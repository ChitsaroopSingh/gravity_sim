from physics.body import Body


def sun_earth():

    return [

        Body(
            mass=10000,
            position=(490,360),
            velocity=(0,0),
            color="yellow"
        ),

        Body(
            mass=10,
            position=(750,360),
            velocity=(0,-1387),
            color="blue"
        )

    ]