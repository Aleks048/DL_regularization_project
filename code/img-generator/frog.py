import cairo
import io
import numpy as np
from IPython.display import display, Image

from cairo_jupyter import *
from shapes import *

class frog:
    def __init__(self):
        self.rotation = np.random.uniform(-20, 20, 5)
        self.eyes = np.random.uniform(-0.05, 0.05, 5)
        self.scale = np.random.uniform(0.5, 1.2, 5)
        self.leg1 = np.random.uniform(-10, 100, 5)
        self.leg2 = np.random.uniform(-10, 100, 5)
    def frog_shape(self, eyes, rleg, lleg):
        frog = ShapeGroup({
            'root': Transform(translation = (0.5, 0.2), children = ShapeGroup({
            'body': Circle(0, 0.25, 0.2, fill = (0.8, 0, 0)),
            'left_eye':Circle(-0.12, 0.1, 0.05+eyes, fill = (0, 0, 0.9)),
            'right_eye':Circle(0.12, 0.1, 0.05+eyes, fill = (0, 0, 0.9)),
            'right_leg1': Transform(translation = (0.22, 0.35), rotation = 45, children = ShapeGroup({
                'leg': Rectangle(-0.04, 0, 0.04, 0.13, fill = (0.8, 0, 0))
                })),
            'left_leg1': Transform(translation = (-0.12, 0.45), rotation = 135, children = ShapeGroup({
                'leg': Rectangle(-0.04, 0, 0.04, 0.13, fill = (0.8, 0, 0))
                })),
            'right_leg2': Transform(translation = (0.30, 0.40), rotation = 135-rleg, children = ShapeGroup({
                'leg': Rectangle(-0.04, 0, 0.05, 0.13, fill = (0.8, 0.8, 0))
                })),
            'left_leg2': Transform(translation = (-0.19, 0.35), rotation = 45+lleg, children = ShapeGroup({
                'leg': Rectangle(-0.04, 0, 0.05, 0.13, fill = (0.8, 0.8, 0))
                })),
            }))
        })
        return frog

    def draw_frog(self, Rata = 0, sc = 1, eyes = 0, leg1 = 0, leg2 = 0):
        scale = 512
        inv_scale = 1. / scale
        size = (scale, scale)
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, *size)
        ctx = cairo.Context(surface)
        ctx.scale(*size)
        f = self.frog_shape(eyes, leg1, leg2)
        t=Transform(children = f, rotation = Rata, scale = [sc,1])
        t.draw(ctx)
#         display(surface_to_image(surface))
        return surface

    def generate_frog(self):
        i = 0
        for a in self.eyes:
            for ll in self.leg1:
                for rl in self.leg2:
                    for r in self.rotation:
                        for s in self.scale:
                            surface = self.draw_frog(r, s, a, ll, rl)
                            surface.write_to_png('frog/frog{}.png'.format(i))
                            i = i+1
