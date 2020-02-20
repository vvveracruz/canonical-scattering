#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import mpmath as mm


#   NOTE: please try to keep all lines under 70 characters
#           so that it looks nice when i typeset it in latex



#--------------------------------------------------------------------
#                           main class
#--------------------------------------------------------------------

class Main():
    def __init__(self):
        print("Running plotter ...")
        self.graph = Graphics()

    def run(self):

        print("doing stuff...")
        graph = Graphics()

        #self.create_hankel_wave(graph)

        self.create_hankel_wave(self.graph)

        #self.create_plane_wave(graph)
        #self.create_incident_field(graph)
        self.create_scattered_field(graph)

    def create_hankel_wave(self, graph):
        hankel_wave = ExampleBessel(10)
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
        self.X, self.Y = self.get_xy_series(length, delta)
        self.length = length
        self.name = "Default"

    def get_xy_series(self, length, delta):
        x = np.linspace(-length, length, delta)
        y = x
        return np.meshgrid(x, y)

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    #              coordinate axis
    #---------------------------------------------
    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_Z(self):
        return self.Z

    def get_theta(self):
        return np.arctan2(self.get_X(), self.get_Y())

    def get_r(self):
        return np.sqrt( self.get_X()*self.get_X() + self.get_Y()*self.get_Y() )

    def get_length(self):
        return self.length

    def get_extent(self):
        '''
        Returns the axis labels in the format
            [xmin, xmax, ymin, ymax]
        '''
        return [-self.get_length(), self.get_length(),
            -self.get_length(), self.get_length()]

    #           physical constants
    #---------------------------------------------
    def get_speed_of_sound(self):           # speed of sound
        return 343

    def set_wavevector(self, x, y):         # wavevector
        self.wavevector = (x, y)

    def get_wavevector(self):
        return self.wavevector

    def get_wavenumber(self):
        return np.sqrt(self.wavevector[0]*self.wavevector[0]
            + self.wavevector[1]*self.wavevector[1])

    def set_truncation(self, N):            # truncation number
        self.truncation = N

    def get_truncation(self):
        return self.truncation

    def get_omega(self):                    # omega
        return self.get_speed_of_sound()*self.get_wavenumber()

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

    def phi(self):
        return np.exp(1j*(self.get_X() + self.get_Y()))

    def phi_real(self):
        return (self.phi()).real

    def phi_imag(self):
        return (self.phi()).imag
#-------------------------- incident field --------------------------

class IncidentField( Wave):
    def __init__(self, length=5, delta=100):
        print('Enter IncidentField()')
        Wave.__init__(self, length, delta)

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
        print('Scattered Field created')

        self.truncation = 50
        self.wavevector = (5,2)
        self.separation_constant = -1


        self.set_name("Scattered field for N = "
            + str(self.truncation) + " and K ="
            + str(self.wavevector))

        self.Z = self.get_field()

    def get_field(self):
        return None

    def get_angular_dependence(theta, N):
        '''
        theta   |   angular component
        N       |   truncation number
        '''
        #----- Initialisation ----
        z = 0
        for n in range(self.truncation):
            z += (self.get_angular_dependence(n)
                *self.get_radial_dependence()).real

        return z

    def get_angular_dependence(self, n):
        '''
        TODO: missing A_n and B_n coeffs
        '''
        return np.cos(n * self.get_theta()) + np.sin(self.get_theta())

    def get_radial_dependence(self):
        k = np.sqrt(self.wavevector[0]*self.wavevector[0]
            + self.wavevector[1]*self.wavevector[1])
        return sp.hankel1(self.separation_constant, k*self.get_r())

    def get_radial_dependence():
        return 1


#------------------ example bessel function wave --------------------
class ExampleBessel(Wave):
    def __init__(self, length=5, delta=100):
        super(ExampleBessel, self).__init__(length, delta)
        self.Z = self.phi_real()
        self.set_name("Example Bessel")

    def phi(self):
        return sp.hankel1(0, self.get_r())

    def phi_real(self):
        return (self.phi()).real

#−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−-
#                        graphics class
#--------------------------------------------------------------------
class Graphics():
    def __init__(self):
        print("graphics started")

    def contour(self, wave, xlabel='x', ylabel='y'):
        #TODO (no difference from heat map)
        return None

    def heat_map(self, wave, xlabel='x', ylabel='y'):
        self.create_generic_plot(wave)
        self.label_generic_plot(wave, xlabel, ylabel)
        self.draw_plot()

    def create_generic_plot(self, wave):
        return plt.imshow(wave.get_Z(), extent=wave.get_extent())

    def label_generic_plot(self, wave = "title", xlabel='x', ylabel='y'):
        plt.title(wave.get_name())
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)

    def draw_plot(self):
        plt.colorbar()
        plt.show()


#--------------------------------------------------------------------
#                               SCRIPT
#--------------------------------------------------------------------

# Run code if compiled as python script from command line
# Otherwise import module.
if __name__ == '__main__':
    Main().run()
