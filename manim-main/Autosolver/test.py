from manim import *

class GraphAreaPlot(Scene):
    def construct(self):
        X5 = 3
        X1 = 1
        X3 = 2
        A1 = 10
        A2 =11
        eqn = VGroup(
            Tex(r"Area under", "//v-//t", r" curve gives displacemet covered in the given time interval"),
            Tex(r"lets highlight the region for which area needs to be found"),
            Tex(r"Total area =", r"a1", " + ",  r"a2"),
            Tex(r"$a1 = \frac{1}{2} \times base \times height $", ),
    
    
        )
        self.play(Write(eqn[3]))
        self.wait()
        