# Physics 91SI
# Spring 2015
# Lab 7

import numpy as np

class Particle:
    """Stores information about a particle with mass, position, and velocity."""
    
    def __init__(self, Position, M):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.pos = Position   # Sets x position
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,))
        self.acc = np.zeros((2,))
        
   class Molecule:
    def __init__(self, pos1, pos2, m1, m2, k, L0):
        self.p1 = Particle(pos1,m1)
        self.p2 = Particle(pos2,m2)

    def get_displ(self):
        return tuple(np.subtract(self.p2,self.p1))


