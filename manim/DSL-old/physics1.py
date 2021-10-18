from manimlib import *
import numpy as np

class firsteqation(Scene):
    def construct(self):
        #text = Text("Here is a text", font="Consolas", font_size=90)
        difference = Tex("Q: Ram is started running with a constant acceleration 2, r"\frac{m}{s^{2}}}","What is the distace he will travel in 4 seconds.")
        #VGroup(text, difference).arrange(DOWN, buff=1)
        #self.play(Write(text))
        difference.to_corner(UL)
        self.play(FadeIn(difference, UP))
        self.wait(1)
        

        to_isolate = ["v", "u", "=", "a", "t","s"]
        lines = VGroup(
            Tex(r"Given: a = 2 \frac{m}{s^{2}}, u = 0\frac{m}{s},t = 4s, s = ?}"),
            Tex(r"From\ equation\ of\ motion:}"),
            Tex(r"s = ut + \frac{1}{2}at^{2}"),
            Tex(r"s = 0\times t + \frac{1}{2}\times 2 \times 4^{2}"),
            Tex(r"s= 16 meters",)
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "t": YELLOW,
                "u": TEAL,
                "a": GREEN,
                "s": RED,
            })
        
        play_kw = {"run_time": 4}
        self.add(difference)
        self.play(Transform(lines[0],(lines[0].scale(1/3)).next_to(difference,DOWN)))
        self.wait(2)

        lines[0].move_to(difference,DOWN)
        self.wait()


        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()


        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()

        self.play(
            TransformMatchingTex(lines[2].copy(), lines[3]),
            **play_kw
        )
        self.wait()

        self.play(
            TransformMatchingTex(lines[3].copy(), lines[4]),
            **play_kw
        )
        self.wait()

        
