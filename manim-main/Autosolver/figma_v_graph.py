from numpy.lib.nanfunctions import _nanmedian1d
from manim import *
import numpy as np
import math
import random

from pyglet.com import pIUnknown

X1 = 1;

X3 = 5;

X5 = 2;



vv = X1 + X5*X3;


class T_labelExample(Scene):
    def construct(self):
        # axes
        axes = Axes(
            x_range=[0, int(X3+3),1],
            y_range=[0, int(vv+3), 2],
            x_length=12,
            y_length=6,
            
            ).set_stroke(WHITE).to_corner(DL, buff=1)
        axes.add_coordinates()
       
        #axes_lables = axes.get_axis_labels(x_label_tex="t(sec)", y_label_tex="v(m/s)",).set_color(WHITE)
        y_label = axes.get_y_axis_label("v(m/s)", edge=UP, direction=LEFT, buff=0.9)
        x_label = axes.get_x_axis_label("t(sec)", edge=RIGHT, direction=RIGHT, buff=0.3)
        axes_lables = VGroup(x_label.set_color(BLUE), y_label.set_color(BLUE))
        #self.play(
        #    Write(axes, run_time=3)    
        #)
        self.add(axes, axes_lables)
        i = 0;
        j = 0;
        while i < vv+3: 
            h1 = Line(start= (axes.c2p(0, i)), end= (axes.c2p(X3+3, i))).set_stroke(BLUE).set_opacity(0.2)
            self.add(h1)
            i = i+1;
        while j < X3+3: 
            h2 = Line(start= (axes.c2p(j, 0)), end= (axes.c2p(j, vv+3))).set_stroke(BLUE).set_opacity(0.2)
            self.add(h2)
            j = j+1;

        
        self.play(
            Write(axes, run_time=3)    
        )
        #initial velocity text
        eqn = VGroup(
            Tex(r"Given: initial velocity = ", str(X1), r"m/s").scale(0.9),
            Tex(r"So at t = 0 s, u = }", str(X1), r"m/s").scale(0.9),
            Tex(r"Hence co-ordinates of point on the axes :  (0,",str(X1),")").scale(0.9),
        )
        self.play(Write(eqn[0].to_edge(UP), runtime = 5))
        self.wait()
        self.play(Write(eqn[1].next_to(eqn[0],DOWN)))
        self.wait()
        self.play(Write(eqn[2].next_to(eqn[1],DOWN)))
        self.wait()
        self.play(FadeOut(eqn))
        #initial velocity graph
        dot = Dot(color=GREEN)
        h_line = always_redraw(lambda: axes.get_horizontal_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_vertical_line(dot.get_bottom()))

        self.play(
            FadeIn(h_line),
            FadeIn(v_line),
        )
        self.play(dot.animate.move_to(axes.c2p(0, X1)))
        self.wait()

        # accleration text
        eqn = VGroup(
            Tex(r"Given: acceleration = ", str(X5), r"$m/s^2$"),
            Tex(r"Slope of the velocity-time curve gives accleration"),
            Tex(r"Hence slope of the curve is ",str(X5),"=",str(X5),"/1"),
        )
        self.play(Write(eqn[0].move_to(UP), runtime = 5))
        self.wait()

        self.play(Write(eqn[1].scale(0.9).next_to(eqn[0],DOWN)))
        self.wait()
        self.play(Write(eqn[2].scale(0.9).next_to(eqn[1],DOWN)))
        self.wait()
        self.play(FadeOut(eqn))

        # accleration graph

        dot2 = Dot(color=GREY).move_to(axes.c2p(1, int(X1+X5)))
        dots = Dot(color=BLACK).move_to(axes.c2p(1, X1))
        sv_line = VGroup(Line(dots.get_center(), dot2.get_center()).set_stroke(WHITE))
        sh_line = VGroup(Line(dot.get_center(), dots.get_center()).set_stroke(WHITE))
        
        # updater
        braceh = Brace(sh_line)

        bracev = Brace(sv_line, direction = RIGHT)

        text = label = Text("1").set_stroke(YELLOW).scale(1/2)
        labelv = Tex(str(X5)).set_stroke(YELLOW)
        always(label.next_to, braceh, DOWN)
        self.add(sh_line, braceh, label)
        always(labelv.next_to, bracev, RIGHT)
        self.add(sh_line, bracev, labelv)
        

        self.play(
            FadeIn(sh_line),
            FadeIn(sv_line),
        )
        self.wait(3)
        refline = VGroup(DashedLine(dot.get_center(), dot2.get_center()).set_stroke(YELLOW_E))
        self.add(dot, dot2, refline)
        self.play(FadeIn(refline))
        self.wait(2)

        #time text
        eqn = VGroup(
            Tex(r"Given: time of motion = ", str(X3), r" s"),
        )
        self.play(Write(eqn[0].move_to(UP), runtime = 5))
        self.wait()
        self.play(FadeOut(eqn))

        #time graph
        dot3 = Dot(color=PINK)
        ddot = Dot(color=BLACK).move_to(axes.c2p(X3,vv+1))
        self.play(dot3.animate.move_to(axes.c2p(0, 0)))
        self.wait()
        self.play(dot3.animate.move_to(axes.c2p(X3, 0)))
        self.wait()

        
        v_line = VGroup(DashedLine(dot3.get_center(), ddot.get_center()).set_stroke(PINK))
        
        self.play(
            FadeIn(v_line.set_stroke(PINK))
        )
        self.add(v_line)


        # finding answer
        h_line = always_redraw(lambda: axes.get_horizontal_line(dot3.get_left()))
        h_line = h_line.set_stroke(LIGHT_PINK)
        
        dot4 = Dot(color=PINK).move_to(axes.c2p(X3, vv))
        dot5 = Dot(color=PINK).move_to(axes.c2p(0, vv))

        fline =  VGroup(Line(dot.get_center(), dot4.get_center()).set_stroke(BLUE_E))
        self.add(dot, dot4, fline)
        f2line =  VGroup(DashedLine(dot4.get_center(), dot5.get_center()).set_stroke(GREEN_A))
        #self.add(fline, v_line, dot5, f2line)
        self.play(
            FadeIn(fline),
            FadeIn(h_line),
            run_time = 5
        )
        #self.wait(2)

        self.play(
            FadeIn(f2line)
        )
        self.wait()
        
        self.add(fline, dot5, f2line, h_line)

        # concluding

        fdot = Dot(color=ORANGE).move_to(axes.c2p(0, vv)).scale(1.5)
        self.play(FadeIn(fdot))
        ftext = Tex(r"Final Velocity = ", str(vv), r"m/s" ).scale(1/2).move_to(fdot.get_center()+ 1.5*RIGHT + 0.5*DOWN).set_stroke(ORANGE)
        self.play(Write(ftext))


        