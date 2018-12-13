
from simple_object import *

class Dog(Simple_Object):
    def __init__(self, rot = 0, sc = 0.9, tail = 0, leg1 = 0, leg2 = 0):
        super(Dog, self).__init__()
        self.name = "dog"
        self.rotation = rot
        self.scale = sc
        self.tail = tail
        self.leg1 = leg1
        self.leg2 = leg2
        self.shape = self.shape()

    def shape(self):
        dog = ShapeGroup({
            'root': Transform(translation = (0.5, 0.2), children = ShapeGroup({
                'head': Circle(-0.24, 0.21, 0.07, fill = (0.8, 0, 0)),
                'mouth': Transform(translation = (-0.03, 0.52), rotation = 90, children = ShapeGroup({
                    'mouth': Circle(-0.26, 0.27, 0.037, fill = (0.8, 0, 0))
                })),
                'body': Rectangle(-0.2, 0.27, 0.35, 0.15, fill = (0, 0, 0.9)),
                'tail': Transform(translation = (0.17, 0.30), rotation = 135 + self.tail, children = ShapeGroup({
                    'tail': Rectangle(-0.025, 0, 0.06, 0.25, fill = (0, 0.0, 0.9))
                })),
                'front_leg1': Transform(translation = (-0.15, 0.42), rotation = 30 + self.leg1, children = ShapeGroup({
                    'leg': Rectangle(-0.025, 0, 0.05, 0.2, fill = (0.8, 0.8, 0))
                })),
                'front_leg2': Transform(translation = (-0.15, 0.42), rotation = -10 - self.leg2, children = ShapeGroup({
                    'leg': Rectangle(-0.025, 0, 0.05, 0.2, fill = (0.8, 0.8, 0))
                })),
                'back_leg1': Transform(translation = (0.1, 0.42), rotation = 30 + self.leg1, children = ShapeGroup({
                    'leg': Rectangle(-0.025, 0, 0.05, 0.2, fill = (0.8, 0.8, 0))
                })),
                'back_leg2': Transform(translation = (0.1, 0.42), rotation = -10 - self.leg2, children = ShapeGroup({
                    'leg': Rectangle(-0.025, 0, 0.05, 0.2, fill = (0.8, 0.8, 0))
                })),
            }))
        })
        return dog
