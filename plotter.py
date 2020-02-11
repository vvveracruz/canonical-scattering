#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import os
import time


class Main():

    def __init__(self):
        print("Main")

    def run(self):
        print("doing stuff...")
        graph = Graphics()
        self.create_hankel_wave(graph)
        #graph.contour(plane_wave, title='Real part')
        
    def create_hankel_wave(self, graph):
        plane_wave = PlaneWave('imag')
        hankel_wave = ExampleBessel(200)
        graph.heat_map(hankel_wave)


#####################
#   Wave super class
        
class Wave():

    def __init__(self, length, delta):
        self.X, self.Y = self.get_xy_series(length,delta)
        self.name = "Default"
        #self.Z = self.create_z_series(length, delta)

    def get_xy_series(self, length, delta):
        x = np.linspace(-length, length, delta)
        y = x
        return np.meshgrid(x, y)

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

#####################
#   Concrete Wave Instantiations
        
    
class PlaneWave(Wave):
    def __init__(self, type, length=10 , delta=100):
        super(PlaneWave, self).__init__(length, delta)
        
        if type == 'real':
            print('nice one')
            self.Z = self.phi_real()
        else:
            print('bad choice')
            self.Z = self.phi_imag()

        print("New %s" % self.get_name())

    def phi(self):
        return np.exp(1j*(self.get_X() + self.get_Y()))

    def phi_real(self):
        return (self.phi()).real

    def phi_imag(self):
        return (self.phi()).imag



class ExampleBessel(Wave):
    def __init__(self, length=10, delta=100):
        super(ExampleBessel, self).__init__(length, delta)
        self.Z = self.phi_real()
        
        self.set_name("Example Bessel")
        print("New %s" % self.get_name())

    def phi(self):
        return sp.hankel1(1, self.get_X()+ self.get_Y())

    def phi_real(self):
        return (self.phi()).real

#####################
class Graphics():
    def __init__(self):
        print("graphics object created")

    def contour(self, wave, title="Title", xlabel='x', ylabel='y'):
        plot = plt.contour(wave.get_Z())
        plt.title(wave.get_name())
        plt.ylabel(xlabel)
        plt.xlabel(ylabel)
        plt.colorbar(plot)
        plt.show()

    def heat_map(self, wave, title="Title", xlabel='x', ylabel='y'):
        plot = plt.imshow(wave.get_Z())
        plt.title(wave.get_name())
        plt.ylabel(xlabel)
        plt.xlabel(ylabel)
        plt.colorbar(plot)
        plt.show()



########### Script

Main().run()