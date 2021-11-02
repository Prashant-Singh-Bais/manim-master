from pickle import FALSE, TRUE
from manim.utils.color import DARK_BLUE, LIGHT_GRAY
from numpy.lib.nanfunctions import _nanmedian1d
from manim import *
import numpy as np
import math
import random

from pyglet.com import pIUnknown

X1 = 1;   #intial velocity
#X2 =     #displacement
X3 = 5;   #time
#X4 =     #final velocity
X5 = 2;   #acceleration
s = 30;
# (X1*X3) + 0.5*(X5)*((X3)^2);

class figma_s_eqn(Scene):
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
        self.play(Transform(eqn[1],(eqn[1].set_color(GREY))))
        self.play(Transform(eqn[2],(eqn[2].set_color(GREEN))))
        self.play(Transform(eqn[3],(eqn[3].set_color(GREY))))
        self.wait()

        self.play(Transform(eqn,(eqn[2].scale(0.7)).next_to(l2,DOWN).set_color(WHITE)), runtime=3)

        #Steps
        steps = VGroup(
            Tex(r"s = ", str(X1), r"$\times$",str(X3), r" + ", r"0.5", r"$ \times $", str(X5),r"$ \times $", str(X3), r"$^2$"),
            Tex(r"s= ", str(s), r" meter")
        )
        self.play(Write(steps[0]),runtime=2)
        self.wait()
        self.play(Transform(steps[0],steps[0].scale(0.7).next_to(eqn[3],DOWN)),runtime=3)
        self.wait()
        self.play(Write(steps[1]),runtime=2)
        self.wait()
        self.play(Transform(steps[1],steps[1].scale(0.7).next_to(steps[0],DOWN)),runtime=3)
        self.wait()
    
