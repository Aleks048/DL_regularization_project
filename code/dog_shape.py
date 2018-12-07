import cairo
import io
import numpy as np
from IPython.display import display, Image

from cairo_jupyter import *
from shapes import *

dog = ShapeGroup({
    'root': Transform(translation = (0.5, 0.2), children = ShapeGroup({
        'head': Circle(0, 0, 0.1, fill = (0.8, 0, 0)),
        'body': Rectangle(-0.05, 0.1, 0.1, 0.4, fill = (0, 0, 0.9)),
        'left_leg': Transform(translation = (-0.05, 0.5), rotation = 30, children = ShapeGroup({
            'leg': Rectangle(-0.025, 0, 0.05, 0.3, fill = (0, 0.8, 0))
        })),
        'right_left': Transform(translation = (0.05, 0.5), rotation = -30, children = ShapeGroup({
            'arm': Rectangle(-0.025, 0, 0.05, 0.3, fill = (0.8, 0.8, 0))
        })),
    }))
})

def draw_dog():
scale = 512
inv_scale = 1. / scale
size = (scale, scale)
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, *size)
ctx = cairo.Context(surface)
ctx.scale(*size)

    dog.draw(ctx)

    display(surface_to_image(surface))

draw_dog()
