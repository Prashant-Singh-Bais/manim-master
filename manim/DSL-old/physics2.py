from manimlib import *
import numpy as np

class firsteqation(Scene):
    def construct(self):
        line1 = Text("Q: Ram is started running with a constant acceleration 2 m/s2 What is the distace he will travel in 4 seconds")
        second_line = Text("Q: Ram is started running with a constant acceleration 2 m/s2 What is the distace he will travel in 4 seconds",font_size=20)
        #lineb = Tex(r"2 ms^{-2}}")
        #linec = Text("\n What is the distace he will travel in 4 seconds")
        #Tex(r"Q:\ Ram\ is\ started\ running\ with\ a\ constant\ acceleration\ 2 ms^{-2}\newline \ What\ is\ the\ distace\ he\ will\ travel\ in\ 4\ seconds.}")
        #line1 = self.add(linea, lineb, linec)
        #(r"Q:\ Ram\ is\ started\ running\ with\ a\ constant\ acceleration}", r"\ 2 ms^{-2}\\}", r"What\ is\ the\ distace\ he\ will\ travel\ in\ 4\ seconds.}")
        #Tex('Q: Ram is started running with a constant acceleration', r"\2frac{m}{s^{2}}\n",'What is the distace he will travel in 4 seconds.')
        #second_line = Tex("a")
        #(r"Q:\ Ram\ is\ started\ running\ with\ a\ constant\ acceleration}", r"\ 2 ms^{-2}\\}", r"What\ is\ the\ distace\ he\ will\ travel\ in\ 4\ seconds.}")
        #Tex(r"\text{Q: Ram is started running with a constant acceleration } 2 ms^{-2}} \text{ What is the distace he will travel in 4 seconds.}")
        #Tex(r'Q: Ram is started running with a constant acceleration', r"\2frac{m}{s^{2}}\n",'What is the distace he will travel in 4 seconds.',font_size=20)
        #second_line.next_to(my_first_text,DOWN)
        #third_line=Text("for me and you!")
        #third_line.next_to(my_first_text,DOWN)
 
        self.add(line1)
        self.wait(2)
        self.play(Transform(line1,second_line.to_corner(UL)))
        self.wait()
        #self.add(second_line)
        #second_line.shift(3*UP)
        self.wait()
        #self.play(ApplyMethod(second_line.shift(3*UP)))
        
