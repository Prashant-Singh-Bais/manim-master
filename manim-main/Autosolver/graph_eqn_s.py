from pickle import FALSE, TRUE
from manim.utils.color import DARK_BLUE, LIGHT_GRAY
from numpy.lib.nanfunctions import _nanmedian1d
from manim import *
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

A2 = X3*X1;
A1 = 0.5*X3*(vv-X1);


def listToString(q): 
    str1 = "" 
    for ele in q: 
        str1 = ele  
    return str1

l1 = Tex("Q:", str(o[n2])," is in uniform straight-line motion. if it ", str(listToString(u))," and ", str(listToString(a)),". Find the displacement covered in next ", str(listToString(t)) )
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
        braceh = Brace(sh_line)

        bracev = Brace(sv_line, direction = RIGHT)

        text = label = Text("1").set_stroke(YELLOW).scale(1/2)
        labelv = Tex(str(X5)).set_stroke(YELLOW)
        always(label.next_to, braceh, DOWN)
        self.add(sh_line, braceh, label)
        always(labelv.next_to, bracev, RIGHT)
        gg = self.add(sh_line, bracev, labelv)
        
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
        self.play(Write(eqn[0][0].next_to(l1, DOWN)))
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
            FadeIn(v_line.set_stroke(PINK))
        )
        self.add(v_line)


        # final point
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


        #area
        self.play(FadeOut(braceh, bracev, labelv, label))
        curve1 = axes.get_graph(lambda x: (X1) + (X5)*x , x_range=[0, X3+2], color=BLUE_C)
        curve2 = axes.get_graph(lambda x: (X1)  , x_range=[0, X3+2], color=BLUE_C)
        area = axes.get_area(curve1, [0, X3], color=GREEN, opacity=0.5)
        area1 = axes.get_area(curve1, [0, X3], bounded_graph=curve2, color=LIGHT_BROWN, opacity=0.6)
        area2 = axes.get_area(curve2, [0, X3], color=YELLOW_E, opacity=0.6)

        
        self.wait(2)
        self.play(FadeIn(area1), FadeIn(area1))
        self.play(FadeOut(h_line))


        #self.play(Create(area1))
        #self.play(Create(area2))

        #area braces

        brace_a11 = Brace(area1, direction = RIGHT).set_color(BLUE)
        brace_a12 = Brace(area1, direction = UP).set_color(BLUE)
        brace_a21 = Brace(area2, direction = RIGHT).set_color(BLUE)
        brace_a22 = Brace(area2, direction = UP).set_color(BLUE)

        label_a11 = brace_a11.get_text(str(vv-X1)).set_color(BLUE)
        label_a12 = brace_a12.get_text(str(X3)).set_color(BLUE)
        label_a21 = brace_a21.get_text(str(X1)).set_color(BLUE)
        label_a22 = brace_a22.get_text(str(X3)).set_color(BLUE)

        #area text1
        eqn = VGroup(
            Tex(r"Area under", r" v-t", r" curve gives displacemet covered in the given time interval").scale(0.6),
            Tex(r"lets highlight the region for which area needs to be found").scale(0.6),
            Tex(r"Total area =", r"$a_{1}$", " + ",  r"$a_{2}$").scale(0.6),
            Tex(r"$a_{1}$",r"$ = \frac{1}{2} \times base \times height $", ).scale(0.6),
            Tex(r"$a_{1}$",r"$ = \frac{1}{2} \times$",str(vv-X1), r"$\times$", str(X3), r" =  ", str(A1)).scale(0.6),

            Tex(r"$a_{2}$",r"$= length \times breadth$", ).scale(0.6),
            Tex(r"$a_{1}$",r" = ", str(X1), r"$\times $", str(X3), r" =  ", str(A2)).scale(0.6),

            Tex(r"Total area = ", str(A1+A2)).scale(0.6),
            Tex(r"Hence, displacemet covered = ", str(A1+A2), r" m").scale(0.6),

            #Tex(r"Total area =", str(A1), r" + ",   str(A1)).scale(0.6)
    
        )
        # calcuation animation
        #Area shading
        self.play(Write(eqn[0].next_to(l1, DOWN)))
        self.wait(2)
        self.play(FadeOut(eqn[0]))
        self.play(Write(eqn[1].next_to(l1, DOWN)))
        self.play(FadeOut(eqn[1]))
        self.play(Create(area))
        self.wait(2)
        #Breaking into two
        eqn[2][1].set_color(GREEN)
        eqn[2][3].set_color(YELLOW_E)
        self.play(Write(eqn[2].next_to(l1, DOWN)))
        self.play(FadeIn(area1), FadeIn(area2))
        self.add(eqn[2], area1, area2)
        #garea = self.add(area1, area2)
        #a1
        #self.play(Transform(area1, area1.set_color(GREEN).set_opacity(0.5)) )
        #self.play(Transform(area2, area2.set_opacity(0.2)) )
#############
        self.add(area1, brace_a11, brace_a12, label_a11,label_a12 )
        self.play(Write(eqn[3].next_to(eqn[2], DOWN)))
        self.wait(2)
        self.play(Write(eqn[4].next_to(eqn[3], DOWN)))
        self.wait(2)
        self.play(FadeOut(eqn[3], eqn[4]))
        self.play(FadeOut(area1, brace_a11, label_a11, brace_a12, label_a12))
        #self.play(Transform(area1, area1.set_color(LIGHT_BROWN)) )
        self.wait()
        #a2
        #self.play(Transform(area2, area2.set_color(GREEN).set_opacity(0.5)) )
        #self.play(Transform(area1, area1.set_opacity(0.2)) )
#################        
        self.add(area2, brace_a21, brace_a22,label_a21, label_a22)
        self.play(Write(eqn[5].next_to(eqn[2], DOWN)))
        self.wait()
        self.play(Write(eqn[6].next_to(eqn[5], DOWN)))
        self.wait()
        self.play(FadeOut(eqn[5], eqn[6]))
        self.play(FadeOut(area2, brace_a21, label_a21, brace_a22, label_a22))
        #self.play(Transform(area2, area2.set_color(YELLOW_E)) )
        self.wait()
        #total
        #self.play(Transform(eqn[2], eqn[9]))
        #self.play(Transform(eqn[2][3], Tex(str(A2)).scale(0.6)))
        self.play(FadeOut(area1, area2))
        self.play(FadeIn(area))
        self.play(Write(eqn[7].next_to(eqn[2], DOWN)))
        self.wait()
        self.play(Write(eqn[8].next_to(eqn[7], DOWN)))
        self.wait()
