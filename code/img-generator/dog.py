import cairo
import io
import numpy as np
from IPython.display import display, Image

from cairo_jupyter import *
from shapes import *

class dog:
    def __init__(self):
        self.rotation = np.random.uniform(-20, 20, 5)
        self.tail = np.random.uniform(-20, 100, 5)
        self.scale = np.random.uniform(0.5, 1, 5)
        self.leg1 = np.random.uniform(0, 50, 5)
        self.leg2 = np.random.uniform(0, 50, 5)
    def dog_shape(self, tail, leg1, leg2, **kwargs):
        dog = ShapeGroup({
            'root': Transform(translation = (0.5, 0.2), children = ShapeGroup({
                'head': Circle(-0.24, 0.21, 0.07, fill = (0.8, 0, 0)),
                'mouth': Transform(translation = (-0.03, 0.52), rotation = 90, children = ShapeGroup({
                    'mouth': Circle(-0.26, 0.27, 0.037, fill = (0.8, 0, 0))
                })),
                'body': Rectangle(-0.2, 0.27, 0.35, 0.15, fill = (0, 0, 0.9)),
                'tail': Transform(translation = (0.17, 0.30), rotation = 135+tail, children = ShapeGroup({
                    'tail': Rectangle(-0.025, 0, 0.06, 0.25, fill = (0, 0.0, 0.9))
                })),
                'front_leg1': Transform(translation = (-0.15, 0.42), rotation = 30+leg1, children = ShapeGroup({
                    'leg': Rectangle(-0.025, 0, 0.05, 0.2, fill = (0.8, 0.8, 0))
                })),
                'front_leg2': Transform(translation = (-0.15, 0.42), rotation = -10-leg2, children = ShapeGroup({
                    'leg': Rectangle(-0.025, 0, 0.05, 0.2, fill = (0.8, 0.8, 0))
                })),
                'back_leg1': Transform(translation = (0.1, 0.42), rotation = 30+leg1, children = ShapeGroup({
                    'leg': Rectangle(-0.025, 0, 0.05, 0.2, fill = (0.8, 0.8, 0))
                })),
                'back_leg2': Transform(translation = (0.1, 0.42), rotation = -10-leg2, children = ShapeGroup({
                    'leg': Rectangle(-0.025, 0, 0.05, 0.2, fill = (0.8, 0.8, 0))
                })),
            }))
        })
        return dog

    def draw_dog(self, Rata = 0, sc = 1, tail = 0, leg1 = 0, leg2 = 0):
        scale = 512
        inv_scale = 1. / scale
        size = (scale, scale)
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, *size)
        ctx = cairo.Context(surface)
        ctx.scale(*size)
        d = self.dog_shape(tail, leg1, leg2)
        t=Transform(children = d, rotation = Rata, scale = [sc,sc])
        t.draw(ctx)
#         display(surface_to_image(surface))
        return surface
    def generate_dog(self):
        i = 0
        for t in self.tail:
            for l1 in self.leg1:
                for l2 in self.leg2:
                     for r in self.rotation:
                        for s in self.scale:
                            surface = self.draw_dog(r, s, t, l1, l2)
                            surface.write_to_png('dog/dog_{}.png'.format(i))
                            i = i+1
