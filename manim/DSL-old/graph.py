from manimlib import *

class T_labelExample(Scene):
    def construct(self):
        # defines the axes and linear function
        axes = Axes(x_range=[-1, 10], y_range=[-1, 10], x_length=9, y_length=6)
        func = axes.get_graph(lambda x: x, color=BLUE)
        # creates the T_label
        #t_label = axes.get_axis_labels(self, x_label_tex="x", y_label_tex="y")
        self.add(axes, func)