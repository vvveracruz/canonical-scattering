#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from plotter import *

class CylinderField(Wave, Inputs):
    def __init__(self):
        print('>>> cylinderField started...')
        Wave.__init__(self)
        Inputs.__init__(self)

    def get_constant_term(self, n, type='neumann'):
        if self.boundary_type in ['neumann', 'Neumann']:
            return self.get_neumann_factor(n) * np.power(1j,n) * self.get_neumann_bc(n)
        elif self.boundary_type in ['dirichlet', 'Dirichlet']:
            return self.get_neumann_factor(n) * np.power(1j,n) * self.get_dirichlet_bc(n)
        else:
            raise TypeError('Invalid boundary type.')

    def get_angular_term(self, n, theta):
        return np.cos(n * (theta - self.get_incident_angle()))

    def get_radial_term(self, n, r):
        return ( sp.hankel1(n, self.get_wavenumber() * r) + sp.jv(n, self.get_wavenumber() * r))

    def get_neumann_bc(self, n):
        return sp.jvp(n, self.get_wavenumber() * self.get_cylinder_radius()) / sp.h1vp(n, self.get_wavenumber() * self.get_cylinder_radius())

    def get_dirichlet_bc(self, n):
        return None

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
    def __init__(self):
        super(ScatteredField, self).__init__()
        print('Scattered Field created')

        #------ setting physical constants ------
        self.set_truncation(100)
        self.set_wavevector(1,10)
        self.separation_constant = -1


        self.set_name("Scattered field for N = "
            + str(self.truncation) + " and K ="
            + str(self.wavevector))

        self.Z = self.get_field()

    def get_field(self):
        return self.get_radial_dependence().real

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
        return sp.hankel1(self.separation_constant, self.get_wavenumber()*self.get_r())



#------------------ example bessel function wave --------------------
class ExampleBessel(Wave):
    def __init__(self):
        super(ExampleBessel, self).__init__()
        self.Z = self.phi_real()
        self.set_name("Example Bessel")
        self.set_axis_length(10)

    def phi(self):
        return sp.jv(0, self.get_r())

    def phi_real(self):
        return (self.phi()).real
