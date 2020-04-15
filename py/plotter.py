#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy.special as sp
import mpmath as mm
import time

from fields import *
from inputs import *
from graphics import *

def real(Z):
    '''
    Transforms an array with imaginary float elements into an
    array with real float elements.
    '''
    return [[n.real for n in z] for z in Z]
#--------------------------------------------------------------------
#                           main class
#--------------------------------------------------------------------

class Main(Inputs):
    def __init__(self):
        print("> running plotter ...")
        Inputs.__init__(self)
        self.graph = Graphics()

    def run(self):
        '''TODO: docstring'''
        if self.field_type in ['incident', 'Incident', 'IncidentField']:
            self.incident_plot(self.graph)

        elif self.field_type in ['scattered', 'Scattered', 'ScatteredField']:
            self.scattered_plot(self.graph)

        elif self.field_type in ['total', 'Total', 'TotalField']:
            self.total_plot(self.graph)

        elif self.field_type in ['none', 'None']:
            self.testing()

        else:
            raise TypeError('Invalid field type.')

    def testing(self):
        '''Function used to test code.'''
        self.integer_order_hankel1(self.graph)

    def incident_plot(self, graph):
        '''TODO: docstring'''
        field = IncidentField()
        graph.heat_map(field)

    def scattered_plot(self, graph):
        '''TODO: docstring'''
        field = ScatteredField()
        graph.heat_map(field)

    def total_plot(self,graph):
        '''TODO: docstring'''
        field = TotalField()
        graph.heat_map(field)

    def integer_order_bessel(self, graph):
        '''TODO'''
        x=np.linspace(0,5,100)

        fig=plt.figure()
        ax=fig.add_subplot(111)

        for n in range(6):
            ax.plot(x,sp.jv(n, x), label=str(n))

        plt.axhline(color='black',
                    linewidth = 0.5)

        plt.legend(loc=1)
        plt.title('Bessel function of order n.')
        plt.ylabel('$J_{n}(r)$')
        plt.xlabel('$r$')
        plt.show()

    def integer_order_hankel1(self, graph):
        '''TODO'''
        x=np.linspace(0,7,100)

        fig=plt.figure()
        ax=fig.add_subplot(111)

        axes = plt.gca()
        axes.set_ylim([0,4])

        for n in range(6):
            ax.plot(x,abs(sp.hankel1(n, x)), label=str(n))

        plt.legend(loc=1)
        plt.title('Absolute value of the Hankel function of the first type of order n.')
        plt.ylabel('$H_{n}^{(1)}(r)$')
        plt.xlabel('$r$')
        plt.show()

    def integer_order_neumann(self, graph):
        '''TODO'''
        x=np.linspace(0,10,100)

        fig=plt.figure()
        ax=fig.add_subplot(111)

        axes = plt.gca()
        axes.set_ylim([-2,1])

        for n in range(6):
            ax.plot(x,sp.yn(n, x), label=str(n))

        plt.axhline(color='black',
                    linewidth = 0.5)

        plt.legend(loc=4)
        plt.title('Neumann function of order n.')
        plt.ylabel('$Y_{n}(r)$')
        plt.xlabel('$r$')
        plt.show()


#--------------------------------------------------------------------
#                         wave super class
#--------------------------------------------------------------------
class Wave(Inputs):
    def __init__(self):
        print('>> wave started...')
        Inputs.__init__(self)

    def get_theta(self, x, y):
        return np.arctan2(x, y)

    def get_r(self, x, y):
        return np.sqrt( x*x + y*y )

    def get_array_Z(self):
        '''
        This will return the array to be plotted.
        '''
        array = []
        for x in self.get_X():
            lst = []
            for y in self.get_Y():
                lst.append(self.get_value_z(x, y))
            array.append(lst)
        return array

    def get_neumann_factor(self, n):
        '''Returns the neumann factor for a given n.'''
        if n==0:
            return 1
        elif n > 0:
            return 2
        else:
            print('ERROR: Invalid n for Neumann factor')

    def get_modified_neumann_factor(self, n):
        '''Returns the neumann factor multiplied by i^n for a given n.'''
        if n==0:
            return 1
        elif n > 0:
            return 2 * np.power(1j, n)
        else:
            print('ERROR: Invalid n for Neumann factor')

    def get_neumann_bc(self, n):
        '''TODO: docstring'''
        return sp.jvp(n, self.get_wavenumber() * self.get_cylinder_radius()) / sp.h1vp(n, self.get_wavenumber() * self.get_cylinder_radius())

    def get_dirichlet_bc(self, n):
        '''TODO: docstring'''
        return -(sp.jv(n, self.get_wavenumber() * self.get_cylinder_radius()) / sp.hankel1(n, self.get_wavenumber() * self.get_cylinder_radius()))


#--------------------------------------------------------------------
#                               SCRIPT
#--------------------------------------------------------------------

# Run code if compiled as python script from command line
# Otherwise import module.
if __name__ == '__main__':
    Main().run()
