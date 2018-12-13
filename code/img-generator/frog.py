
from simple_object import *

class Frog(Simple_Object):
    def __init__(self, rot = 0, sc = 0.9, eyes = 0, leg1 = 0, leg2 = 0):
        super(Frog, self).__init__()
        self.name = "frog"
        self.rotation = rot
        self.scale = sc
        self.eyes = eyes
        self.leg1 = leg1
        self.leg2 = leg2
        self.shape = self.shape()

    def shape(self):
        frog = ShapeGroup({
            'root': Transform(translation = (0.5, 0.2), children = ShapeGroup({
            'body': Circle(0, 0.25, 0.2, fill = (0.8, 0, 0)),
            'left_eye':Circle(-0.12, 0.1, 0.05 + self.eyes, fill = (0, 0, 0.9)),
            'right_eye':Circle(0.12, 0.1, 0.05 + self.eyes, fill = (0, 0, 0.9)),
            'right_leg1': Transform(translation = (0.22, 0.35), rotation = 45, children = ShapeGroup({
                'leg': Rectangle(-0.04, 0, 0.04, 0.13, fill = (0.8, 0, 0))
                })),
            'left_leg1': Transform(translation = (-0.12, 0.45), rotation = 135, children = ShapeGroup({
                'leg': Rectangle(-0.04, 0, 0.04, 0.13, fill = (0.8, 0, 0))
                })),
            'right_leg2': Transform(translation = (0.30, 0.40), rotation = 135-self.leg1, children = ShapeGroup({
                'leg': Rectangle(-0.04, 0, 0.05, 0.13, fill = (0.8, 0.8, 0))
                })),
            'left_leg2': Transform(translation = (-0.19, 0.35), rotation = 45+ self.leg2, children = ShapeGroup({
                'leg': Rectangle(-0.04, 0, 0.05, 0.13, fill = (0.8, 0.8, 0))
                })),
            }))
        })
        return frog
