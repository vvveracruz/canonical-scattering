import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import plotly.graph_objects as pltgo
import numpy as np

from inputs import *
from fields import *
from plotter import *

class Graphics(Inputs):
    def __init__(self):
        print(">> graphics started...")
        Inputs.__init__(self)
        self.input = Inputs()
        self.fig = pltgo.Figure()


    def run(self):
        '''This function is used to test things within the graphics
        file. It is the function that is run when the file is compiled
        from the command line.'''
        self.time_slider(TotalField())

    def get_extent(self):
        '''
        Returns the axis labels in the format
            [xmin, xmax, ymin, ymax]
        '''
        label = self.input.get_axis_length()
        return [-label, label,
            -label, label]

    def time_slider(self, wave):
        '''TODO: docstring'''

        def time_dependence(t):
            return np.exp(-1j*self.get_omega()*t)

        def field(t):
            return [[n * time_dependence(t) for n in z] for z in wave.get_array_Z()]

        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.25)

        '''t = np.arange(0.0, 1.0, 0.001)
        s = np.sin(2 * np.pi * t)
        l, = plt.plot(t, s, lw=2)'''
        plot = plt.imshow(real(field(0)), extent = self.get_extent())
        ax.margins(x=0)

        axcolor = 'lightgoldenrodyellow'
        axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

        time_slider = Slider( axfreq,
                        'Time',
                        valmin = self.time_period[0],
                        valmax = self.time_period[1],
                        valinit = 0.5*(self.time_period[0] + self.time_period[1]),
                        valstep = self.time_step)


        '''def update(val):
            freq = time_slider.val
            l.set_ydata(np.sin(2*np.pi*freq*t))
            fig.canvas.draw_idle()'''

        def update(val):
            t = time_slider.val
            plot = plt.imshow(  real(field(t)),
                                extent = self.get_extent())
            fig.canvas.draw_idle()

        time_slider.on_changed(update)

        plt.show()

    """def time_slider(self, wave):
        '''TODO: docstring'''

        def time_dependence(t):
            return np.exp(-1j*self.get_omega()*t)

        def field(t):
            return [[n * time_dependence(t) for n in z] for z in wave.get_array_Z()]

        #specifying the plot
        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.subplots_adjust(bottom=0.25)

        plot = self.heat_map(wave)

        time_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03])
        time_slider = Slider(   time_slider_ax,
                                'Time',
                                self.time_period[0],
                                self.time_period[1],
                                0.5* (self.time_period[0] + self.time_period[1]),
                                valstep = self.time_step,
                                    )

        def val_update(val):
            plot.set_ydata(signal(time_slider.val))
            fig.canvas.draw_idle()
        time_slider.on_changed(val_update)

        plt.show()"""

    def contour(self, wave):
        Z = [[n.real for n in z] for z in wave.get_array_Z()]
        plt.contour(Z, extent=self.get_extent())
        self.draw_plot()

    def heat_map(self, wave):
        Z = [[n.real for n in z] for z in wave.get_array_Z()]
        plt.imshow(Z, extent=self.get_extent())
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
