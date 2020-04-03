from class_inputs import *

class Graphics():
    def __init__(self):
        print("graphics started...")
        self.input = Inputs()

    def get_extent():
        '''
        Returns the axis labels in the format
            [xmin, xmax, ymin, ymax]
        '''
        label = self.input.get_axis_length()
        return [-label, label,
            -label, label]

    def contour(self, wave, xlabel='x', ylabel='y'):
        plt.contour(wave.get_Z(), extent=self.get_extent())
        self.label_plot(wave, xlabel, ylabel)
        self.draw_plot()

    def heat_map(self, wave, xlabel='x', ylabel='y'):
        plt.imshow(wave.get_Z(), extent=self.get_extent())
        self.label_plot(wave, xlabel, ylabel)
        self.draw_plot(wave)

    def label_plot(self, wave = "title", xlabel='x', ylabel='y'):
        plt.title(wave.get_name())
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)

    def draw_plot(self, wave):
        self.draw_disk_overlay(wave)
        #self.draw_plane_wave_overlay(wave)
        #self.create_legend(wave)
        plt.colorbar()
        plt.show()

    def draw_disk_overlay(self, wave):
        r = wave.get_cylinder_radius()
        plt.gca().add_patch(plt.Circle((0,0),r, fc='#36859F'))

    '''def create_legend(self, wave):
        plt.legend('test')
        text =  'PARAMETERS \n\n' +\
                'K = ' + str(wave.get_wavevector()) +\
                'N = ' + str(wave.get_truncation())
        plt.gcf().text(0.87, 0.75, text, fontsize=10)'''


    '''def draw_plane_wave_overlay(self, wave):
        K = wave.get_wavevector()
        x = wave.get_axis_length()
        d = -5
        plt.gca().add_patch(plt.Arrow(x, x, d, d, fc='white'))'''
