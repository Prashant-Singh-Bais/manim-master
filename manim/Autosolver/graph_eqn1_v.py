from pickle import FALSE, TRUE
from manim.utils.color import DARK_BLUE, LIGHT_GRAY
from matplotlib.pyplot import axes, pink
from numpy.lib.nanfunctions import _nanmedian1d
from manimlib import *
import numpy as np
import math
import random

from pyglet.com import pIUnknown
n1 = random. randint(0,1);
n2 = random. randint(0,4);
X1 = random. randint(1,5);
X2 = (random. randint(1,50))*10;
X3 = (random. randint(1,5))*2;
X4 = random. randint(1,20);
X5 = random. randint(1,5);

o = ["A car", "An object", "A ball", "A bike", "A truck"]
u = ["has initial velocity of "+ str(X1)+" m/s"]#not working properly
d = ["covers a distance of " + str(X2) + " meter "]
t = [str(X3)+" seconds"]
v = ["final velocity is"+str(X4)+" m/s" ]
a = ["has an acceleration of "+ str(X5) +r"$ m/s^2$" ]

vv = X1 + X5*X3;

master = [d, a]

def listToString(q): 
    str1 = "" 
    for ele in q: 
        str1 = ele  
    return str1

l1 = TexText("Q:", str(o[n2])," is in uniform straight-line motion. if it ", str(listToString(u))," and ", str(listToString(a)),". Find its final velocity after ", str(listToString(t)) )
l1 = l1.scale(0.8)
class T_labelExample(Scene):
    def construct(self):
        #qns_statement
        self.play(Write(l1))
        self.wait(4)
        self.play(Transform(l1,l1.scale(0.6).to_edge(UP)))

        # axes
        
        axes = Axes(
            x_range=[0, int(X3+3),1],
            y_range=[0, int(vv+3), 2],
            x_length=2,
            y_length=2,
            y_axis_config={"coordinate_labels_config": {"font_size": 5}},
            x_axis_config={"coordinate_labels_config": {"font_size": 5}},
            axis_config={
                        "font_size": 10,
                    },
            
            ).set_stroke(WHITE).to_corner(DL, buff=1)
        axes.add_coordinate_labels()
        #axes_lables = axes.get_axis_labels(x_label_tex="t(sec)", y_label_tex="v(m/s)",).set_color(WHITE)
        y_label = axes.get_y_axis_label("v(m/s)", edge=UP, direction=LEFT, buff=0.9)
        x_label = axes.get_x_axis_label("t(sec)", edge=RIGHT, direction=RIGHT, buff=0.3)
        axes_lables = VGroup(x_label.set_stroke(BLUE), y_label.set_stroke(BLUE))
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
            TexText(r"Given: initial velocity = ", str(X1), r"m/s").scale(0.9),
            TexText(r"So at t = 0 s, u = }", str(X1), r"m/s").scale(0.9),
            TexText(r"Hence co-ordinates of point on the axes :  (0,",str(X1),")").scale(0.9),
        )
        self.play(Write(eqn[0][0]))
        self.play(Transform(l1[3],l1[3].set_color(GREEN)))
        self.play(Write(eqn[0][1].set_color(GREEN).next_to(eqn[0][0],RIGHT)))
        self.play(Write(eqn[0][2].next_to(eqn[0][1],RIGHT)))
        self.wait()

        self.play(Write(eqn[1].next_to(eqn[0],DOWN)))
        self.wait()
        self.play(Write(eqn[2].next_to(eqn[1],DOWN)))
        self.wait()
        self.play(FadeOut(eqn))
        #initial velocity graph
        dot = Dot(color=GREEN)
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )
        self.play(dot.animate.move_to(axes.c2p(0, X1)))
        self.wait()

        # accleration text
        eqn = VGroup(
            TexText(r"Given: acceleration = ", str(X5), r"$m/s^2$"),
            TexText(r"Slope of the velocity-time curve gives accleration"),
            TexText(r"Hence slope of the curve is ",str(X5),"=",str(X5),"/1"),
        )
        self.play(Write(eqn[0][0]))
        self.play(Transform(l1[5],l1[5].set_color(YELLOW)))
        self.play(Write(eqn[0][1].set_color(YELLOW).next_to(eqn[0][0],RIGHT)))
        self.play(Write(eqn[0][2].next_to(eqn[0][1],RIGHT)))
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
        braceh = always_redraw(Brace, sh_line, DOWN)

        bracev = always_redraw(Brace, sv_line, RIGHT)

        text = label = Text("1").set_stroke(YELLOW).scale(1/2)
        labelv = TexText(str(X5)).set_stroke(YELLOW)
        always(label.next_to, braceh, DOWN)
        self.add(sh_line, braceh, label)
        always(labelv.next_to, bracev, RIGHT)
        self.add(sh_line, bracev, labelv)
        

        self.play(
            ShowCreation(sh_line),
            ShowCreation(sv_line),
        )
        self.wait(3)
        refline = VGroup(DashedLine(dot.get_center(), dot2.get_center()).set_stroke(YELLOW_E))
        self.add(dot, dot2, refline)
        self.play(ShowCreation(refline))
        self.wait(2)

        #time text
        eqn = VGroup(
            TexText(r"Given: time of motion = ", str(X3), r" s"),
        )
        self.play(Write(eqn[0][0]))
        self.play(Transform(l1[7],l1[7].set_color(PINK)))
        self.play(Write(eqn[0][1].set_color(PINK).next_to(eqn[0][0],RIGHT)))
        self.play(Write(eqn[0][2].next_to(eqn[0][1],RIGHT)))
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
            ShowCreation(v_line.set_stroke(PINK))
        )
        self.add(v_line)


        # finding answer
        h_line = always_redraw(lambda: axes.get_h_line(dot3.get_left()))
        h_line = h_line.set_stroke(LIGHT_PINK)
        
        dot4 = Dot(color=PINK).move_to(axes.c2p(X3, vv))
        dot5 = Dot(color=PINK).move_to(axes.c2p(0, vv))

        fline =  VGroup(Line(dot.get_center(), dot4.get_center()).set_stroke(BLUE_E))
        self.add(dot, dot4, fline)
        f2line =  VGroup(DashedLine(dot4.get_center(), dot5.get_center()).set_stroke(GREEN_A))
        #self.add(fline, v_line, dot5, f2line)
        self.play(
            ShowCreation(fline),
            ShowCreation(h_line),
            run_time = 5
        )
        #self.wait(2)

        self.play(
            ShowCreation(f2line)
        )
        self.wait()
        
        self.add(fline, dot5, f2line, h_line)

        # concluding

        fdot = Dot(color=ORANGE).move_to(axes.c2p(0, vv)).scale(1.5)
        self.play(ShowCreation(fdot))
        ftext = TexText(r"Final Velocity = ", str(vv), r"m/s" ).scale(1/2).move_to(fdot.get_center()+ 1.5*RIGHT + 0.5*DOWN).set_stroke(ORANGE)
        self.play(Write(ftext))


        