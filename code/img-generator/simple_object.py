import cairo
import io
import os
import numpy as np
from IPython.display import display, Image

from cairo_jupyter import *
from shapes import *

class Simple_Object:
    def __init__(self):
        self.pixels = 512
        self.inv_scale = 1./ self.pixels
        self.size = (self.pixels, self.pixels)
        self.rotation = 0
        self.scale = 0

    def draw(self):
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, *self.size)
        ctx = cairo.Context(surface)
        ctx.scale(*self.size)
        t=Transform(children = self.shape, rotation = 15 * self.rotation,
            scale = [1+self.scale, 1+self.scale])
        t.draw(ctx)
    #     display(surface_to_image(surface))
        return surface

    def generate(self, path, i):
        surface = self.draw()
        path = path + "/" + self.name + "/"
        filename = path + self.name + "_{}.png".format(i)
        if not os.path.exists(path):
            os.makedirs(path)
        surface.write_to_png(filename)
