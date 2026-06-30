from physics.body import Body

def earth_moon():
    return [

        Body(
            mass=1000,
            position=(490, 360),
            velocity=(0, 0),
            color="blue"
        ),

        Body(
            mass=12,
            position=(560, 360),
            velocity=(0, -845.154),
            color="white"
        )

    ]