from manimlib import *
import numpy as np

class firsteqation(Scene):
    def construct(self):
        line1 = Text("Q: Ram is started running with a constant acceleration 2 m/s2 What is the distace he will travel in 4 seconds")
        second_line = Text("Q: Ram is started running with a constant acceleration 2 m/s2 What is the distace he will travel in 4 seconds \n \n \n Solution:",font_size=20)
        
        self.add(line1)
        self.wait(2)
        self.play(Transform(line1,second_line.to_corner(UL)))
        self.wait()

        to_isolate = ["v", "u", "=", "a", "t","s"]
        lines = VGroup(
            Tex(r"Given:\ a = 2 \frac{m}{s^{2}}, u = 0\frac{m}{s},t = 4s, s = ?}"),
            Tex(r"From\ equation\ of\ motion:}"),
            Tex(r"s = ut + \frac{1}{2}at^{2}"),
            Tex(r"s = 0\times t + \frac{1}{2}\times 2 \times 4^{2}"),
            Tex(r"s= 16 meters",)
        )
        
        self.add(lines[0])
        self.wait(2)
    
        self.play(Transform(lines[0],(lines[0].scale(1/3)).next_to(second_line,DOWN)))
        self.wait(2)

        self.add(lines[1])
        self.wait(2)
    
        self.play(Transform(lines[1],(lines[1].scale(1/3)).next_to(lines[0],DOWN)))
        self.wait(2)

        self.add(lines[2])
        self.wait(2)
    
        self.play(Transform(lines[2],(lines[2].scale(1/3)).next_to(lines[1],DOWN)))
        self.wait(2)

        self.add(lines[3])
        self.wait(2)
    
        self.play(Transform(lines[3],(lines[3].scale(1/3)).next_to(lines[2],DOWN)))
        self.wait(2)

        self.add(lines[4])
        self.wait(2)
    
        self.play(Transform(lines[4],(lines[4].scale(1/3)).next_to(lines[3],DOWN)))
        self.wait(2)






        
