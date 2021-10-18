from numpy.lib.nanfunctions import _nanmedian1d
from manimlib import *
import numpy as np
import math
import random
n1 = random. randint(0,1);
n2 = random. randint(0,4);
X1 = random. randint(1,20);
X2 = (random. randint(1,50))*10;
X3 = (random. randint(1,15))*2;
X4 = random. randint(1,20);
X5 = random. randint(1,10);

o = ["A car", "An object", "A ball", "A bike", "A truck"]
u = ["has initial velocity of "+ str(X1)+" m/s"]#not working properly
d = ["covers a distance of " + str(X2) + " meter "]
t = [str(X3)+" seconds"]
v = ["final velocity is"+str(X4)+" m/s" ]
a = ["has an acceleration of "+ str(X5) +r"$ m/s^2$" ]

master = [d, a]

def listToString(q): 
    str1 = "" 
    for ele in q: 
        str1 = ele  
    return str1

#uu = TexText(listToString(u[n1]))
#aa = Text(listToString(master[int(n1)]))
#ox = Text(o[n1])
#tx1 = Text("Q:")
#tx2 = Text(" is in uniform straight-line motion. if it ")
#tx3 = Text(" and ")
#tx4 = Text(". Find its final velocity")

l1 = TexText("Q:", str(o[n2])," is in uniform straight-line motion. if it ", str(listToString(u))," and ", str(listToString(a)),". Find its final velocity after ", str(listToString(t)) )
l1 = l1.scale(0.8)
#l1 = TexText("Q."+ o[n1] + " is in uniform straight-line motion. if it " + listToString(u) + " and " + listToString(master[int(n1)]) +" "+ listToString(t) + ". Find its final velocity");
'''print ("A. ")
print ("B. ")
print ("C. ")
print ("D. ")'''
l2 = TexText("Given: ", "u = " , str(X1)+" m/s, " , "a = ", str(X5) + r"$ m/s^2$,", " t = ", str(X3)+" seconds")

class firsteqation(Scene):
    def construct(self):

        self.play(Write(l1))
        self.wait(4)
        self.play(Transform(l1,l1.scale(0.9).to_edge(UP)))
        #u
        self.add(l2[0], l2[1].set_color(BLUE))
        self.wait(2)
        self.play(Transform(l1[3],l1[3].set_color(BLUE)))
        self.wait(2)
        self.add (l2[0], l2[1].set_color(BLUE), l2[2].set_color(BLUE))
        self.wait(2)
        #a
        self.add(l2[0], l2[1].set_color(BLUE), l2[2].set_color(BLUE),l2[3].set_color(GREEN))
        self.wait(2)
        self.play(Transform(l1[5],l1[5].set_color(GREEN)))
        self.wait(2)
        self.add(l2[0], l2[1].set_color(BLUE), l2[2].set_color(BLUE),l2[3].set_color(GREEN), l2[4].set_color(GREEN))
        self.wait(2)
        #t
        self.add(l2[0], l2[1].set_color(BLUE), l2[2].set_color(BLUE),l2[3].set_color(GREEN), l2[4].set_color(GREEN),l2[5].set_color(YELLOW))
        self.wait(2)
        self.play(Transform(l1[7],l1[7].set_color(YELLOW)))
        self.wait(2)
        self.add(l2[0], l2[1].set_color(BLUE), l2[2].set_color(BLUE),l2[3].set_color(GREEN), l2[4].set_color(GREEN),l2[5].set_color(YELLOW), l2[6].set_color(YELLOW))
        self.wait(2)
        #dock given
        self.play(Transform(l2,l2.scale(1/2).next_to(l1, DOWN)))
        self.wait(2)
        #equation of motion
        eqn = VGroup(
            Tex(r"From\ equations\ of\ motion:}"),
            Tex(r"v = u + at}"),
            Tex(r"s = ut + \frac{1}{2}at^{2}"),
            Tex(r"v^2 + u^2 = 2as"),
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

        self.play(Transform(eqn,(eqn[1].scale(0.7)).next_to(l2,DOWN).set_color(WHITE)))
        self.wait()

        #Steps
        v = X1 + X5*X3;
        to_isolate = ["v", "u", "=", "a", "t","s"]
        steps = VGroup(
            Tex(r"v =", str(X1), r"+", str(X5), r" \times", str(X3)),
            Tex(r"v= ", str(v), r"\ \frac{m}{s}")
        )
        self.play(Write(steps[0]))
        self.wait()
        self.play(Transform(steps[0],steps[0].scale(0.7).next_to(eqn[3],DOWN)))
        self.wait()
        self.play(Write(steps[1]))
        self.wait()
        self.play(Transform(steps[1],steps[1].scale(0.7).next_to(steps[0],DOWN)))
        self.wait()
    
