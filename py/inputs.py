#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json
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
        print(self.wavevector)

    def read_json(self):
        '''
        Returns a dictionary containing the data in data.txt.
        '''
        file = open(r"data.txt", "r")
        return json.load(file)
        file.close()

    def set_params(self):
        '''
        TODO: docstring
        '''
        dict = self.read_json()

        ## NAME OF PLOT
        self.plot_name = dict['plot_name']

        ##  AXIS LENGTH
        try:
            self.axis_length = float(dict['axis_length'])
        except ValueError:
            self.axis_length = 5
            print('ERROR: input for axis length must be a float. Has been set to default.')

        ##  AXIS DELTA
        try:
            self.axis_delta = int(dict['axis_delta'])
        except ValueError:
            self.axis_delta = 100
            print('ERROR: input for axis delta must be a int. Has been set to default.')

        ##  TRUNCATION
        try:
            self.truncation = int(dict['truncation'])
        except ValueError:
            self.truncation = 50
            print('ERROR: input for truncation must be an integer. Has been set to default.')

        ##  WAVEVECTOR
        try:
            self.wavevector = [float(x) for x in dict['wavevector']]
        except ValueError:
            self.wavevector = [-1, -1]
            print('ERROR: inputs for wavevector must be two floats. Has been set to default.')

        ##  CYLINDER RADIUS
        try:
            self.cylinder_radius = float(dict['cylinder_radius'])
        except ValueError:
            self.cylinder_radius = 1
            print('ERROR: input for cylinder radius must be a float. Has been set to default.')

        ##  SPEED OF SOUND
        try:
            self.speed_of_sound = float('speed_of_sound')
        except ValueError:
            self.speed_of_sound = 343
            print('ERROR: input for speed of sound must be a float. Has been set to default.')

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