#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import numpy as np

class Inputs():
    '''
    This class is used to retrieve the parameters for the problem from
    the `data.csv` file.

    Structure of the file
    ---------------------
    0   name of plot        str
    1   axis length         float
    2   axis delta          int
    3   truncation          int
    4   wavevector          float   float
    5   cylinder radius     float
    6   speed of sound      float
    '''

    def __init__(self):
        print("inputs started...")
        self.set_params()

    def get_data(self):
        '''
        Returns an array containing every row of the file as a list.
        '''
        data = []
        with open("data.csv", 'rt') as file:
            reader = csv.reader(file)
            for row in reader: # each row is a list
                data.append(row)
        return data

    def set_params(self):
        '''
        This function retrieves the parameters for the problem for the
        csv filed opened in get_data. It sets the params to default when
        the type entered is not correct.

        Defaults
        --------
        name of plot        No default, it is a string
        axis length         5           float
        axis delta          100         int
        truncation          50          int
        wavevector          (-1,-1)     floats
        cylinder radius     1           int
        speed of sound      343         float
        '''
        ## NAME OF PLOT
        self.plot_name = self.get_data()[0][1]

        ##  AXIS LENGTH
        try:
            self.axis_length = float(self.get_data()[1][1])
        except ValueError:
            self.axis_length = 5
            print('⚠️ Error: input for axis length must be a float. Has been set to default.')

        ##  AXIS DELTA
        try:
            self.axis_delta = int(self.get_data()[2][1])
        except ValueError:
            self.axis_delta = 100
            print('⚠️ Error: input for axis delta must be a int. Has been set to default.')

        ##  TRUNCATION
        try:
            self.truncation = int(self.get_data()[3][1])
        except ValueError:
            self.truncation = 50
            print('⚠️ Error: input for truncation must be an integer. Has been set to default.')

        ##  WAVEVECTOR
        try:
            self.wavevector = (float(self.get_data()[4][1]),
                    float(self.get_data()[4][2]))
        except ValueError:
            self.wavevector = (-1, -1)
            print('⚠️ Error: inputs for wavevector must be two floats. Has been set to default.')

        ##  CYLINDER RADIUS
        try:
            self.cylinder_radius = float(self.get_data()[5][1])
        except ValueError:
            self.cylinder_radius = 1
            print('⚠️ Error: input for cylinder radius must be a float. Has been set to default.')

        ##  SPEED OF SOUND
        try:
            self.speed_of_sound = float(self.get_data()[6][1])
        except ValueError:
            self.speed_of_sound = 343
            print('⚠️ Error: input for speed of sound must be a float. Has been set to default.')

    ##  PARAMS FOR THE COORDINATES
    def get_axis_length(self):
        return self.axis_length

    def get_axis_delta(self):
        return self.axis_delta

    def get_coord_series(self):
        '''
        Returns a list for the x and y values of the problem from
        -`axis length` to `axis length` with granularity set by `axis delta`
        in `data.csv`
        '''
        return np.linspace(-self.get_axis_length(),
            self.get_axis_length(), self.get_axis_delta())

    def get_X(self):
        return self.get_coord_series()

    def get_Y(self):
        return self.get_coord_series()

    def get_theta(self):
        return np.arctan2(self.get_X(), self.get_Y())

    def get_r(self):
        return np.sqrt( self.get_X()*self.get_X()
            + self.get_Y()*self.get_Y() )

    ##  PLOT NAME
    def get_plot_name(self):
        return self.plot_name

    ##  TRUNCATION
    def get_truncation(self):
        return self.truncation

    ##  PARAMS THAT DETERMINE THE PLANE WAVE
    def get_wavevector(self):
        return self.wavevector

    def get_wavenumber(self):
        '''
        The wavenumber is the magnitude of the wavevector.
        '''
        return np.sqrt(self.wavevector[0]*self.wavevector[0]
            + self.wavevector[1]*self.wavevector[1])

    def get_incident_angle(self):
        return np.arctan2(self.wavevector[0], self.wavevector[1])

    def get_omega(self):
        return self.get_speed_of_sound()*self.get_wavenumber()

    ##  PARAMS FOR THE CYLINDER
    def get_cylinder_radius(self):
        return self.cylinder_radius

    ##  PHYSICAL CONSTANTS
    def get_speed_of_sound(self):
        return self.speed_of_sound
