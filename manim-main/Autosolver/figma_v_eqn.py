from numpy.lib.nanfunctions import _nanmedian1d
from manim import *
import numpy as np
import math
import random

X1 = 1;
X3 = 5;
X5 = 2;


class firsteqation(Scene):
    def construct(self):
        l2 = Tex("Given: ", "u = " , str(X1)+" m/s, " , "a = ", str(X5) + r"$ m/s^2$,", " t = ", str(X3)+" seconds")
        
        #given
        self.play(Write(l2, runtime=5))
        self.wait(3)
        
        #dock given
        #self.play(Transform(l2,l2))
        self.play(Transform(l2,l2.scale(0.7).to_edge(UP)), runtime=3)
        self.wait(2)
        #equation of motion
        eqn = VGroup(
            Text("From equations of motion:"),
            Tex(r"$ v = u + at $"),
            Tex(r"$ s = ut + \frac{1}{2}at^{2} $"),
            Tex(r"$ v^2 + u^2 = 2as $"),
        )

        self.play(Write(eqn[0]))
        self.wait()
        self.play(Write(eqn[1].next_to(eqn[0],DOWN)))
        self.wait()
        self.play(Write(eqn[2].next_to(eqn[1],DOWN)))
        self.wait()
        self.play(Write(eqn[3].next_to(eqn[2],DOWN)))
        self.wait()
        #colour change
        self.play(Transform(eqn[1],(eqn[1].set_color(GREEN))))
        self.play(Transform(eqn[2],(eqn[2].set_color(GREY))))
        self.play(Transform(eqn[3],(eqn[3].set_color(GREY))))
        self.wait()

        self.play(Transform(eqn,(eqn[1].scale(0.7)).next_to(l2,DOWN).set_color(WHITE)), runtime=3)

        #Steps
        v = X1 + X5*X3;
        to_isolate = ["v", "u", "=", "a", "t","s"]
        steps = VGroup(
            Tex(r"v =", str(X1), r"+", str(X5), r"$ \times$", str(X3)),
            Tex(r"v= ", str(v), r"$\ \frac{m}{s}$")
        )
        self.play(Write(steps[0]),runtime=2)
        self.wait()
        self.play(Transform(steps[0],steps[0].scale(0.7).next_to(eqn[3],DOWN)),runtime=3)
        self.wait()
        self.play(Write(steps[1]),runtime=2)
        self.wait()
        self.play(Transform(steps[1],steps[1].scale(0.7).next_to(steps[0],DOWN)),runtime=3)
        self.wait()