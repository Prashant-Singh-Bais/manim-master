
from pickle import FALSE, TRUE
from manim.utils.color import DARK_BLUE, LIGHT_GRAY
from matplotlib.pyplot import axes, pink
from numpy.lib.nanfunctions import _nanmedian1d
from manimlib import *
#from manim import *
import numpy as np
import math
import random

from pyglet.com import pIUnknown

class GraphExample(Scene):
    def construct(self):
        #ax = Axes((-3, 10), (-1, 8))
        #ax.add_coordinate_labels()
        ax = NumberPlane(x_range=[-3,10], y_range=[-1,8])
        ax.add_coordinate_labels()
        curve1 = ax.get_graph(lambda x: 2 * np.sin(x))

        self.add(ax,curve1)

        #area = ax.get_area_under_graph(graph = curve1, x_range = (0.0,2.0))

        area = ax.get_area_under_graph(
                        curve1,
                        (PI / 2, 3 * PI / 2),
                        
                    )
        
        self.add(ax, curve1, area)
        #ax.get_area_under_graph(graph=curve, x_range= (0,2))

        #self.add(curve1, area)
        #self.wait(1)
        
        '''sin_graph = axes.get_graph(
            lambda x: 2 * math.sin(x),
            color=BLUE,
        )
        
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")

        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)

        
        #adding rectangles
        def rect(x):
            return(x)
        recta = self.get_graph(rect, x_min = -1, x_max = 5)


        kwargs = {
            "x_min": 2,
            "x_max" : 8,
            "fil_opacity": 0.75,
            "stroke_width": 0.25,
        }
        self.graph = graph
        iteraciones = 6
        flat_rect = self.get_riemann_rectangle(
            self.get_graph(lambda x : 0), dx = 0.5, start_color = PURPLE_A, end_color = 
        )'''