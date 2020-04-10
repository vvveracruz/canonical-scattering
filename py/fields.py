#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from plotter import *

#--------------------------------------------------------------------
#       TOTAL FIELD
#--------------------------------------------------------------------
class TotalField(Wave, Inputs):
    '''
    TODO: docstring
    '''
    def __init__(self):
        print('>>> TotalField started...')
        Wave.__init__(self)
        Inputs.__init__(self)

        self.incident = IncidentField()
        self.scattered = ScatteredField()

    def get_value_z(self, x, y):
        '''
        Returns the value of Z at a given (x, y).
        '''
        r = self.get_r(x, y)
        theta = self.get_theta(x, y)
        return self.incident.get_value_z(x, y) + self.scattered.get_value_z(x,y)

#--------------------------------------------------------------------
#           INCIDENT FIELD
#--------------------------------------------------------------------
class IncidentField(Wave, Inputs):
    '''
    TODO: docstring
    '''
    def __init__(self):
        print('>>> IncidentField started...')
        Wave.__init__(self)
        Inputs.__init__(self)

    def get_value_z(self, x, y):
        '''
        Returns the value of Z at a given (x, y).
        '''

        if self.get_r(x, y) >= self.get_cylinder_radius():
            return (np.exp(1j*(self.get_wavevector()[0]*x + self.get_wavevector()[1]*y)))
        else:
            return 0


#--------------------------------------------------------------------
#           SCATTERED FIELD
#--------------------------------------------------------------------
class ScatteredField(Wave, Inputs):
    '''
    TODO: docstring
    '''
    def __init__(self):
        print('>>> ScatteredField started...')
        Wave.__init__(self)
        Inputs.__init__(self)

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
        return z

    def get_constant_term(self, n):
        '''TODO: docstring'''
        if self.boundary_type in ['neumann', 'Neumann']:
            return self.get_modified_neumann_factor(n) * self.get_neumann_bc(n)

        elif self.boundary_type in ['dirichlet', 'Dirichlet']:
            return self.get_modified_neumann_factor(n) * self.get_dirichlet_bc(n)


        else:
            raise TypeError('Invalid boundary type.')

    def get_angular_term(self, n, theta):
        return np.cos(n*(theta - self.get_incident_angle()))

    def get_radial_term(self, n, r):
        return sp.hankel1(n, self.get_wavenumber()*r)

##----------- T E M P L A T E ---------------
"""
class #####(Wave, Inputs):
    '''
    TODO: docstring
    '''
    def __init__(self):
        print('>>> ##### started...')
        Wave.__init__(self)
        Inputs.__init__(self)

    def get_constant_term(self, n):
        return None

    def get_angular_term(self, n, theta):
        return None

    def get_radial_term(self, n, r):
        return None
"""
