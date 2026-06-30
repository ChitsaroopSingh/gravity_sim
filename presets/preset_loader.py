from presets.random import random_system
from presets.solar import solar
from presets.earthmoon import earth_moon
from presets.binary import binary_stars
from presets.figure8 import figure8
from presets.infinity import infinity_orbit
from physics.body import Body


def load_preset(name):
    print(name)
    if name == "Random":
        return random_system()

    elif name == "Solar-System":
        return solar()

    elif name == "Earth-Moon":
         return earth_moon()

    elif name == "Binary Stars":
        return binary_stars()

    elif name == "Figure-8":
        return figure8()

    elif name == "Infinity":
        return infinity_orbit()

    return []