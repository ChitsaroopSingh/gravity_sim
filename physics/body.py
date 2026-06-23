import numpy as np

class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype = float)
        self.velocity = np.array(velocity, dtype = float)
        self.radius = max(15, int(self.mass ** 0.3))

        self.trail = []
        
        
    def update(self,dt):
        self.position += self.velocity * dt
        