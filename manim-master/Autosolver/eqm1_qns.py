from numpy.lib.nanfunctions import _nanmedian1d
from manimlib import *
import numpy as np
import math
import random
n1 = random. randint(0,1);
X1 = random. randint(1,20);
X2 = (random. randint(1,50))*10;
X3 = (random. randint(1,15))*2;
X4 = random. randint(1,20);
X5 = random. randint(1,10);

o = ["A car", "An object", "A ball"]
u = ["intially at rest","has initial velocity of "+ str(X1)+" m/s" ]#not working properly
d = ["covers a distance of " + str(X2) + " meter"]
t = ["in "+str(X3)+" seconds"]
v = ["final velocity is"+str(X4)+" m/s" ]
a = ["has an acceleration of "+ str(X5) +" m/s2" ]

master = [d, a]

def listToString(q): 
    str1 = "" 
    for ele in q: 
        str1 = ele  
    return str1

l1 = str("Q."+o[n1] + " is in uniform straight-line motion. if it " + listToString(u) + " and " + listToString(master[int(n1)]) +" "+ listToString(t) + ". Find its final velocity");
'''print ("A. ")
print ("B. ")
print ("C. ")
print ("D. ")'''

class firsteqation(Scene):
    def construct(self):

        line1 = Text(l1)
        #Text("Q."+ o[n1]+ " is in uniform straight-line motion. if it " + listToString(u[n1])+ " and " + listToString(master[int(n1)]) +" "+ listToString(t) + ". Find its final velocity")
        #Text("Q: Ram is started running with a constant acceleration 2 m/s2 What is the distace he will travel in 4 seconds")
        
        self.add(line1)
        self.wait(2)
        self.play(Transform(line1,line1.scale(1/2).to_corner(UL)))
        self.wait(4)