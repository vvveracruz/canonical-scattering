#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import mpmath as mm
from fields import *
from class_inputs import *

#--------------------------------------------------------------------
#                           main class
#--------------------------------------------------------------------

class Main():
    def __init__(self):
        print("⏳ running plotter ...")
        self.graph = Graphics()
        self.input = Inputs()

    def run(self):
        print(Wave().get_theta())

    def create_field_around_cylinder(self, graph):
        field = CylinderField()
        print(field.get_Z())
        graph.heat_map(field)

#--------------------------------------------------------------------
#                         wave super class
#--------------------------------------------------------------------
class Wave():
    def __init__(self):
        self.input = Inputs()

        self.X = self.input.get_coord_series()
        self.Y = self.input.get_coord_series()

    #              plot information
    #---------------------------------------------

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_Z(self):
        return self.Z

    def get_theta(self):
        return np.arctan2(self.get_X(), self.get_Y())

    def get_r(self):
        return np.sqrt( self.get_X()*self.get_X()
            + self.get_Y()*self.get_Y() )

    def set_axis_length(self, length):
        self.axis_length = length

    def get_axis_length(self):
        return self.axis_length

    def set_axis_delta(self, delta):
        self.axis_delta = delta

    def get_axis_delta(self):
        return self.axis_delta

    def get_extent(self):
        '''
        Returns the axis labels in the format
            [xmin, xmax, ymin, ymax]
        '''
        return [-self.get_axis_length(), self.get_axis_length(),
            -self.get_axis_length(), self.get_axis_length()]

    def get_xy_series(self):
        return np.linspace(-self.get_axis_length(),
            self.get_axis_length(), self.get_axis_delta())
        '''
        x = np.linspace(-self.get_axis_length(),
            self.get_axis_length(), self.get_axis_delta())
        y = x
        return np.meshgrid(x, y)
        '''

    #           physical constants
    #---------------------------------------------
    def get_speed_of_sound(self):           # speed of sound
        return 343

    def set_wavevector(self, x, y):         # wavevector
        self.wavevector = (x, y)

    def get_wavevector(self):
        return self.wavevector

    def get_wavenumber(self):               # wavenumber
        return np.sqrt(self.wavevector[0]*self.wavevector[0]
            + self.wavevector[1]*self.wavevector[1])

    def get_incident_angle(self):
        return np.arctan2(self.wavevector[0], self.wavevector[1])

    def set_truncation(self, N):            # truncation number
        self.truncation = N

    def get_truncation(self):
        return self.truncation

    def get_omega(self):                    # omega
        return self.get_speed_of_sound()*self.get_wavenumber()

    def set_cylinder_radius(self, r):       # cylinder radius
        self.cylinder_radius = r

    def get_cylinder_radius(self):
        return self.cylinder_radius


    #           math functs
    #---------------------------------------------
    def get_neumann_factor(self, n):
        '''Returns the neumann factor for a given n.'''
        if n==0:
            return 1
        elif n > 0:
            return 2
        else:
            print('🙀 ERROR: Invalid n for Neumann factor')

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
