import numpy as np
import sympy as sp

class Node():

    def __init__(self, **kwargs):
        self.velocity, self.mach, self.pressure, self.temperature = sp.symbols('v M p T')
        self.stag_pressure, self.stag_temperature = sp.symbols('p0 T0')
        self.gamma, self.Cp, self.Cv, self.R = sp.symbols('gamma Cp Cv R')
