#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import os
import time

#   NOTE: please try to keep all lines under 70 characters
#           so that it looks nice when i typeset it in latex

#--------------------------------------------------------------------
#                           main class
#--------------------------------------------------------------------
class Main():
    def __init__(self):
        print("Main")

    def run(self):
        print("doing stuff...")
        graph = Graphics()
        #self.create_hankel_wave(graph)
        #self.create_plane_wave(graph)
        self.create_incident_field(graph)

    def create_hankel_wave(self, graph):
        hankel_wave = ExampleBessel(5)
        graph.heat_map(hankel_wave)

    def create_plane_wave(self, graph):
        plane_wave = PlaneWave('real')
        graph.heat_map(plane_wave)

    def create_incident_field(self, graph):
        incident_field = IncidentField()
        graph.heat_map(incident_field)

    def create_scattered_field(self, graph):
        scattered_field = ScatteredField()
        graph.heat_map(scattered_field)

#--------------------------------------------------------------------
#                         wave super class
#--------------------------------------------------------------------
class Wave():
    def __init__(self, length, delta):
        print('New wave created')
        self.X, self.Y = self.get_xy_series(length, delta)
        self.length = length
        self.name = "Default"

    def get_xy_series(self, length, delta):
        x = np.linspace(-length, length, delta)
        y = x
        return np.meshgrid(x, y)

    def get_time_dependence(self, t, omega):
        return np.exp(-1j*omega*t)

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

    def get_length(self):
        return self.length

    def get_extent(self):
        '''
        Returns the axis labels in the format
            [xmin, xmax, ymin, ymax]
        '''
        return [-self.get_length(), self.get_length(),
            -self.get_length(), self.get_length()]
#--------------------------------------------------------------------
#                         domain class
#--------------------------------------------------------------------
class Domain():
    def __init__(self):
        print('New domain created')

        #------ setting defaults -----
        self.wavevector = (1,1)
        self.truncation = 100
        self.time_series = [1, 2, 3]
        self.omega = 1

    def set_wavevector(self, x, y):
        self.wavevector = (x, y)

    def get_wavevector(self):
        return self.wavevector

    def set_truncation(self, N):
        self.truncation = N

    def get_truncation(self):
        return self.truncation

    def set_omega(self, omega):
        self.omega = omega

    def get_omega(self):
        return self.omega

    def get_time_period(self):
        K = self.wavevector
        k = np.sqrt(K[0]*K[0] + K[1]*K[1])
                    #this is the wave number
        c = 343     #c is the speed of sound in air in ms^-1
        return (2*np.pi)/(k*c)

    def set_time_series(self, delta):
        end = self.get_time_period()
        self.time_series = np.linspace(0, end, delta)

    def get_time_series(self):
        return self.time_series
#--------------------------------------------------------------------
#                       concrete wave instantiations
#--------------------------------------------------------------------
#-------------------------- plane wave ------------------------------
class PlaneWave(Wave):
    def __init__(self, type, length=10 , delta=100):
        super(PlaneWave, self).__init__(length, delta)

        if type == 'real':
            self.set_name("Plane wave real part")
            self.Z = self.phi_real()
        else:
            self.set_name("Plane wave imaginary part")
            self.Z = self.phi_imag()
        print("New %s" % self.get_name())

    def phi(self):
        return np.exp(1j*(self.get_X() + self.get_Y()))

    def phi_real(self):
        return (self.phi()).real

    def phi_imag(self):
        return (self.phi()).imag
#-------------------------- incident field --------------------------
class IncidentField(Domain, Wave):
    def __init__(self, length=5, delta=100):
        print('Enter IncidentField()')

        Domain.__init__(self)
        Wave.__init__(self, length, delta)

        graph = Graphics()

        for t in (1, 2):
            self.Z = self.get_field(t)
            self.set_name("Incident Field at t="+str(t))

    def get_x_dependence(self):
        k = self.get_wavevector()
        print(k)
        return np.exp(-1j*(k[0]*self.get_X() + k[1]*self.get_Y()))

    def get_field(self, t=2):
        omega = self.get_omega()
        return (self.get_x_dependence()*
            self.get_time_dependence(t, omega)).real


#------------------------- scattered field --------------------------
class ScatteredField(Wave):
    def __init__(self, length=5, delta=100):
        super(ScatteredField, self).__init__(length, delta)

    def radial_dependence():
        return None

    def theta_dependence():
        return None

#------------------ example bessel function wave --------------------
class ExampleBessel(Wave):
    def __init__(self, length=5, delta=100):
        super(ExampleBessel, self).__init__(length, delta)
        self.Z = self.phi_real()
        self.set_name("Example Bessel")
        print("New %s" % self.get_name())

    def phi(self):
        return sp.hankel1(0, self.get_X()*self.get_X()
            + self.get_Y()*self.get_Y())

    def phi_real(self):
        return (self.phi()).real

#−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−-
#                        graphics class
#--------------------------------------------------------------------
class Graphics():
    def __init__(self):
        print("graphics object created")

    def contour(self, wave, title="Title", xlabel='x', ylabel='y'):
        plot = plt.contour(wave.get_Z(), extent=wave.get_extent())
        plt.title(wave.get_name())
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.colorbar(plot)
        plt.show()

    def heat_map(self, wave, title="Title", xlabel='x', ylabel='y'):
        plot = plt.imshow(wave.get_Z(), extent=wave.get_extent())
        plt.title(wave.get_name())
        plt.ylabel(xlabel)
        plt.xlabel(ylabel)
        plt.colorbar(plot)
        plt.show()



#--------------------------------------------------------------------
#                               SCRIPT
#--------------------------------------------------------------------
Main().run()
