from manimlib import *



class SquareToCircle(Scene):
    def construct(self):
        text=TexText("\\justifying {First we conceptualize an undirected graph  ${G}$  as a union of a finite number of line segments residing in  ${\\mathbb{{{C}}}}$ . By taking our earlier parametrization, we can create an almost trivial extension to  ${\\mathbb{{{R}}}}^{{{3}}}$ . In the following notation, we write a bicomplex number of a 2-tuple of complex numbers, the latter of which is multiplied by the constant  ${j}$ .  ${z}_{{0}}\\in{\\mathbb{{{C}}}}_{{>={0}}}$  is an arbitrary point in the upper half plane from which the contour integral begins. The function  ${\\tan{{\\left(\\frac{{{\\theta}-{\\pi}}}{{z}}\\right)}}}:{\\left[{0},{2}{\\pi}\\right)}\\to{\\left[-\\infty,\\infty\\right)}$  ensures that the vertices at  $\\infty$  for the Schwarz-Christoffel transform correspond to points along the branch cut at  ${\\mathbb{{{R}}}}_{{+}}$ .}")
        text.scale(0.8)
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))