#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import mpmath as mm

from fields import *
from class_inputs import *
from class_graphics import *

#--------------------------------------------------------------------
#                           main class
#--------------------------------------------------------------------

class Main():
    def __init__(self):
        print("⏳ running plotter ...")
        self.graph = Graphics()
        self.input = Inputs()

    def run(self):
        #print(self.input.get_Y())
        return None

    def create_field_around_cylinder(self, graph):
        field = CylinderField()
        print(field.get_Z())
        graph.heat_map(field)

#--------------------------------------------------------------------
#                         wave super class
#--------------------------------------------------------------------
class Wave():
    def __init__(self):
        print('wave started...')

    #           math functs
    #---------------------------------------------
    def get_neumann_factor(self, n):
        '''Returns the neumann factor for a given n.'''
        if n==0:
            return 1
        elif n > 0:
            return 2
        else:
            print('ERROR: Invalid n for Neumann factor')

    #           time dependence
    #---------------------------------------------
    def get_time_period(self):
        return (2*np.pi) / (self.get_wavenumber()
            * self.get_speed_of_sound())

    def set_time_series(self, delta):
        end = self.get_time_period()
        self.time_series = np.linspace(0, end, delta)

    def get_time_dependence(self, t):
        return np.exp(-1j*self.get_omega()*t)


#--------------------------------------------------------------------
#                               SCRIPT
#--------------------------------------------------------------------

# Run code if compiled as python script from command line
# Otherwise import module.
if __name__ == '__main__':
    Main().run()
