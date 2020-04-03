#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy.special as sp
import mpmath as mm

from fields import *
from inputs import *
from graphics import *

#--------------------------------------------------------------------
#                           main class
#--------------------------------------------------------------------

class Main():
    def __init__(self):
        print("running plotter ...")
        self.graph = Graphics()

    def run(self):
        self.cylinder_field(self.graph)
        return None

    def cylinder_field(self, graph):
        field = CylinderField()
        graph.heat_map(field)

#--------------------------------------------------------------------
#                         wave super class
#--------------------------------------------------------------------
class Wave(Inputs):
    def __init__(self):
        print('>> wave started...')
        Inputs.__init__(self)

    def get_theta(self, x, y):
        return np.arctan2(x, y)

    def get_r(self, x, y):
        return np.sqrt( x*x
            + y*y )

    def get_array_Z(self):
        '''
        This will return the array to be plotted.
        '''
        array = []
        for x in self.get_X():
            lst = []
            for y in self.get_Y():
                lst.append(self.get_value_z(x, y))
            array.append(lst)
        return array

    def get_value_z(self, x, y):
        '''
        Returns the value of Z at a given (x, y).
        '''
        r = self.get_r(x, y)
        theta = self.get_theta(x, y)

        if r >= self.get_cylinder_radius():
            return self.get_sum(r, theta)
        else:
            return 0

    def get_sum(self, r, theta):
        '''Actions the summation up to the truncation number and
        returns the approximate value for z for a given point.'''
        z = 0   #Initialising
        for n in range(self.truncation):
            z += self.get_constant_term(n) * self.get_angular_term(n, theta) * self.get_radial_term(n, r)
        return z.real

    def get_neumann_factor(self, n):
        '''Returns the neumann factor for a given n.'''
        if n==0:
            return 1
        elif n > 0:
            return 2
        else:
            print('ERROR: Invalid n for Neumann factor')

#--------------------------------------------------------------------
#                               SCRIPT
#--------------------------------------------------------------------

# Run code if compiled as python script from command line
# Otherwise import module.
if __name__ == '__main__':
    Main().run()
