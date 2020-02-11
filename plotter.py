#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import os
import time
#-----------------------------------------------------------------------------
#                           main class
#-----------------------------------------------------------------------------
class Main():
    def __init__(self):
        print("Main") 

    def run(self):
        print("doing stuff...")
        graph = Graphics()
        self.create_hankel_wave(graph)
        #self.create_plane_wave(graph)

    def create_hankel_wave(self, graph):
        hankel_wave = ExampleBessel(5)
        graph.heat_map(hankel_wave)

    def create_plane_wave(self, graph):
        plane_wave = PlaneWave('real')
        graph.heat_map(plane_wave)


#-----------------------------------------------------------------------------
#                           wave super class
#-----------------------------------------------------------------------------
class Wave():
    def __init__(self, length, delta):
        self.X, self.Y = self.get_xy_series(length, delta)
        self.length = length
        self.name = "Default"
        #self.Z = self.create_z_series(length, delta)

    def get_xy_series(self, length, delta):
        x = np.linspace(-length, length, delta)
        y = x
        return np.meshgrid(x, y)

    def get_extent(self):
        '''
        Returns the axis labels in the format [xmin, xmax, ymin, ymax].
        '''
        l = self.get_length()
        print(l)
        return [-l, l, -l, l]

    def create_z_series(self, length, delta):
        # put code here .... loopy stuff... infinite summmation
        return None

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

#-----------------------------------------------------------------------------
#                       concrete wave instantiations
#-----------------------------------------------------------------------------
#------------------------------ plane wave -----------------------------------
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


#--------------------- example bessel function wave ---------------------------
class ExampleBessel(Wave):
    def __init__(self, length=10, delta=100):
        super(ExampleBessel, self).__init__(length, delta)
        self.Z = self.phi_real()

        self.set_name("Example Bessel")
        print("New %s" % self.get_name())

    def phi(self):
        return sp.hankel1(0, self.get_X()*self.get_X()+ self.get_Y()*self.get_Y())

    def phi_real(self):
        return (self.phi()).real

#-----------------------------------------------------------------------------
#                               graphics class
#-----------------------------------------------------------------------------
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



#-----------------------------------------------------------------------------
#                               SCRIPT
#-----------------------------------------------------------------------------
<<<<<<< HEAD
Main().run()
=======
Main().run()
>>>>>>> b80cd708ef4f9ea7e271df7119fd32451f7ff235
