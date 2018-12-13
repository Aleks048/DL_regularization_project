
from simple_object import *

class Airplane(Simple_Object):
    def __init__(self, rot = 0, sc = 0.9, head = 0, body = 0, wing = 0):
        super(Airplane, self).__init__()
        self.name = "airplane"
        self.rotation = rot
        self.scale = sc
        self.head = head
        self.body = body
        self.wing = wing
        self.shape = self.shape()

    def shape(self):
        airplane = ShapeGroup({
            'root': Transform(translation = (0.5, 0.2), children = ShapeGroup({
                'head': Circle(-0.34, 0.3, 0.08 +self.head, fill = (0.8, 0.8, 0)),
                'body': Rectangle(-0.3, 0.22, 0.75 + self.body, 0.17, fill = (0, 0, 0.9)),
                'upper_wing': Transform(translation = (0.10,-0.1), rotation = 30, children = ShapeGroup({
                    'arm': Rectangle(-0.04, 0., 0.13 + self.wing, 0.5, fill = (0, 0, 0.9))
                })),

                'under_wings': Transform(translation = (-0.14, 0.35), rotation = -30, children = ShapeGroup({
                    'arm': Rectangle(-0.025, 0, 0.13 + self.wing, 0.5, fill = (0, 0, 0.9))
                })),

            }))
        })
        return airplane
