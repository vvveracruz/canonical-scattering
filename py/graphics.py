import matplotlib.pyplot as plt
import numpy as np

from inputs import *
from fields import *
from plotter import *

class Graphics(Inputs):
    def __init__(self):
        print(">> graphics started...")
        Inputs.__init__(self)
        self.input = Inputs()

    def run(self):
        '''This function is used to test things within the graphics
        file. It is the function that is run when the file is compiled
        from the command line.'''

    def get_extent(self):
        '''
        Returns the axis labels in the format
            [xmin, xmax, ymin, ymax]
        '''
        label = self.input.get_axis_length()
        return [-label, label,
            -label, label]

    def contour(self, wave):
        plt.contour(real(Z), extent=self.get_extent())
        self.draw_plot()

    def heat_map(self, wave):
        plt.imshow(real(Z), extent=self.get_extent())
        self.draw_plot()

    def draw_plot(self):
        '''TODO: docstring'''

        plt.title(self.get_plot_name())
        plt.ylabel('y')
        plt.xlabel('x')

        #self.draw_disk_overlay(wave)
        try:
            plt.colorbar()
        except RuntimeError:
            pass

        plt.show()

    def draw_disk_overlay(self, wave):
        r = wave.get_cylinder_radius()
        #plt.gca().add_patch(plt.Circle((0,0),r, fc='#36859F'))

# Run code if compiled as python script from command line
# Otherwise import module.
if __name__ == '__main__':
    Graphics().run()
