import cairo
import io
import numpy as np
from IPython.display import display, Image

from cairo_jupyter import *
from shapes import *
class airplane:
    def __init__(self):
        # mu, sigma = 0, 1 # mean and standard deviation
        #Rotation = np.random.normal(mu, sigma, 20)
        #Arm = np.random.normal(mu, sigma, 100)
        #Scale = np.random.normal(mu, sigma, 100)
        #Lleg = np.random.normal(mu, sigma, 100)
        #Rleg = np.random.normal(mu, sigma, 100)
        self.rotation = np.random.uniform(-20, 20, 5)
        self.scale = np.random.uniform(0.5,1,5)
        self.wing = np.random.uniform(-0.1,0.1, 5)
        self.head = np.random.uniform(-0.02, 0.02, 5)
        self.body = np.random.uniform(-0.2, 0.2, 5)

    def airplane_shape(self, head, body, wing, **kwargs):
        airplane = ShapeGroup({
            'root': Transform(translation = (0.5, 0.2), children = ShapeGroup({
                'head': Circle(-0.34, 0.3, 0.08+head, fill = (0.8, 0.8, 0)),
                'body': Rectangle(-0.3, 0.22, 0.75+body, 0.17, fill = (0, 0, 0.9)),
                'upper_wing': Transform(translation = (0.10,-0.1), rotation = 30, children = ShapeGroup({
                    'arm': Rectangle(-0.04, 0., 0.13+wing, 0.5, fill = (0, 0, 0.9))
                })),

                'under_wings': Transform(translation = (-0.14, 0.35), rotation = -30, children = ShapeGroup({
                    'arm': Rectangle(-0.025, 0, 0.13+wing, 0.5, fill = (0, 0, 0.9))
                })),

            }))
        })
        return airplane

    def draw_airplane(self,Rata = 0, sc = 0.9, head = 0, body = 0, wing = 0):
        scale = 512
        inv_scale = 1. / scale
        size = (scale, scale)
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, *size)
        ctx = cairo.Context(surface)
        ctx.scale(*size)
        a = self.airplane_shape(head, body, wing)
        t=Transform(children = a, rotation = Rata, scale = [0.2+sc,sc])
        t.draw(ctx)
    #     display(surface_to_image(surface))
        return surface
    def generate_airplane(self):
        i = 0

        for h in self.head:
            for b in self.body:
                for w in self.wing:
                    for r in self.rotation:
                        for s in self.scale:
                            surface = self.draw_airplane(r, s, h, b, w)
                            surface.write_to_png('airplane/airplane_{}.png'.format(i))
                            i = i+1
