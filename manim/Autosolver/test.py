
from manimlib import *
import numpy as np

class GraphExample(Scene):
    def construct(self):
        ax = Axes((-3, 10), (-1, 8))
        ax.add_coordinate_labels()


        curve1 = ax.get_graph(lambda x: 2 * np.sin(x))

        self.add(ax,curve1)

        area = ax.get_area_under_graph(curve1, x_range = (0,2), fill_color=BLUE, fill_opacity=1)
        
        #ax.get_area_under_graph(graph=curve, x_range= (0,2))

        self.add(curve1, area)
        self.wait(1)
        
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