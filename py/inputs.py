#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import numpy as np

class Inputs():
    '''
    This class is used to retrieve the parameters for the problem from
    the `data.txt` file.
    '''
    def __init__(self):
        print(">> inputs started...")
        self.file_params = self.read_file("data.txt")
        self.set_params()

    def read_file(self, file_name):
        '''
        Returns a dictionary containing the data in data.txt.
        '''
        file = open(file_name, "r")
        return_value = json.load(file)
        file.close()
        return return_value
        
    def set_params(self):
        '''
        TODO: docstring
        '''
        self.boundary_type = self.file_params['boundary_type'] ## TYPE OF BCS
        self.field_type = self.file_params['field_type']  ## FIELD TYPE
       
        try:
            self.axis_length = float(self.file_params['axis_length'])   ##  AXIS LENGTH
        except ValueError:
            self.axis_length = 5
            print('ERROR: input for axis length must be a float. Has been set to default.')

        try:
            self.axis_delta = int(self.file_params['axis_delta'])  ##  AXIS DELTA
        except ValueError:
            self.axis_delta = 100
            print('ERROR: input for axis delta must be a int. Has been set to default.')
  
        try:
            self.truncation = int(self.file_params['truncation']) ##  TRUNCATION
        except ValueError:
            self.truncation = 50
            print('ERROR: input for truncation must be an integer. Has been set to default.')

        try:
            self.wavevector = [float(x) for x in self.file_params['wavevector']]  ##  WAVEVECTOR
        except ValueError:
            self.wavevector = [-1, -1]
            print('ERROR: inputs for wavevector must be two floats. Has been set to default.')
   
        try:
            self.cylinder_radius = float(self.file_params['cylinder_radius'])  ##  CYLINDER RADIUS
        except ValueError:
            self.cylinder_radius = 1
            print('ERROR: input for cylinder radius must be a float. Has been set to default.')

        try:
            self.speed_of_sound = float(self.file_params['speed_of_sound'])  ##  SPEED OF SOUND
        except ValueError:
            self.speed_of_sound = 343
            print('ERROR: input for speed of sound must be a float. Has been set to default.')

    ##  COORDINATE PARAMS
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
        return np.linspace(-self.get_axis_length(), self.get_axis_length(), self.get_axis_delta())

    def get_X(self):
        return self.get_coord_series()

    def get_Y(self):
        return self.get_coord_series()

    ##  PLOT NAME
    def get_plot_name(self):
        return self.field_type + ' ' + self.boundary_type + ', N = ' + str(self.truncation) + ', k = ' + str(round(self.get_wavenumber(), 2))+ ', inc angle = ' + str(round(self.get_incident_angle(), 2))

    def get_field_type(self):
        return self.field_type

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
        return np.sqrt(self.wavevector[0]*self.wavevector[0] + self.wavevector[1]*self.wavevector[1])

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
        