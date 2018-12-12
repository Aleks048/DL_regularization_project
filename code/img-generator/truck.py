import cairo
import io
import numpy as np
from IPython.display import display, Image

from cairo_jupyter import *
from shapes import *
class truck:
    def __init__(self):
        # mu, sigma = 0, 1 # mean and standard deviation
        #Rotation = np.random.normal(mu, sigma, 20)
        #Arm = np.random.normal(mu, sigma, 100)
        #Scale = np.random.normal(mu, sigma, 100)
        #Lleg = np.random.normal(mu, sigma, 100)
        #Rleg = np.random.normal(mu, sigma, 100)
        self.rotation = np.random.uniform(-20, 20, 5)
        self.scale = np.random.uniform(0.5,1,5)
        self.head = np.random.uniform(-0.2, 0.2, 5)
        self.body = np.random.uniform(-0.2, 0.2, 5)
        self.wheel = np.random.uniform(-0.02,0.02, 5)

    def truck_shape(self,head, body, wheel, **kwargs):
        truck = ShapeGroup({
            'root': Transform(translation = (0.5, 0.2), children = ShapeGroup({
            'head1': Rectangle(-0.3, 0.17, 0.1, 0.2, fill = (0, 0, 0.9)),
            'head2': Rectangle(-0.2, 0.1, 0.25+head, 0.2, fill = (0, 0, 0.9)),
            'body': Rectangle(-0.3, 0.27, 0.7+body, 0.2, fill = (0.8, 0, 0)),
            'front_wheels': Circle(-0.15, 0.5, 0.07+wheel, fill = (0.8, 0.8, 0)),
            'back_wheels': Circle(0.2, 0.5, 0.07+wheel, fill = (0.8, 0.8, 0)),

            }))
        })
        return truck

    def draw_truck(self, Rata = 0, sc = 0.9, head = 0, body = 0, wheel = 0):
        scale = 512
        inv_scale = 1. / scale
        size = (scale, scale)
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, *size)
        ctx = cairo.Context(surface)
        ctx.scale(*size)
        tk = self.truck_shape(head, body, wheel)
        t=Transform(children = tk, rotation = Rata, scale = [sc,sc])
        t.draw(ctx)
    #     display(surface_to_image(surface))
        return surface

    def generate_truck(self):
        i = 0
        for r in self.rotation:
            for h in self.head:
                for b in self.body:
                    for w in self.wheel:
                        for s in self.scale:
                            surface = self.draw_truck(r, s, h, b, w)
                            surface.write_to_png('truck/truck_{}.png'.format(i))
                            i = i+1
