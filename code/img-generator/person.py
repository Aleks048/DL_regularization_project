
from simple_object import *

class Person(Simple_Object):
    def __init__(self, rot = 0, sc = 0.9, arm = 0, Lleg = 0, Rleg = 0):
        super(Person, self).__init__()
        self.name = "person"
        self.rotation = rot
        self.scale = sc
        self.arm = arm
        self.Lleg = Lleg
        self.Rleg = Rleg
        self.shape = self.shape()

    def shape(self):
        person = ShapeGroup({
            'root': Transform(translation = (0.5, 0.2), children = ShapeGroup({
            'head': Circle(0, 0, 0.1, fill = (0.8, 0, 0)),
            'body': Rectangle(-0.1, 0.1, 0.2, 0.38, fill = (0, 0, 0.9)),
            #'body': Rectangle(-0.05, 0.1, 0.1, 0.4, fill = (0, 0, 0.9)),
            'left_arm': Transform(translation = (-0.05, 0.15), rotation = 135-self.arm, children = ShapeGroup({
                'arm': Rectangle(-0.025, 0.04, 0.05, 0.3, fill = (0, 0.8, 0))
            })),
            'right_arm': Transform(translation = (0.05, 0.15), rotation = -135+self.arm, children = ShapeGroup({
                'arm': Rectangle(-0.025, 0.04, 0.05, 0.3, fill = (0, 0.8, 0))
            })),
            'left_leg': Transform(translation = (-0.06, 0.50), rotation = 45-self.Lleg, children = ShapeGroup({
                'leg': Rectangle(-0.05, -0.045, 0.07, 0.33, fill = (0.8, 0.8, 0))
            })),
            'right_left': Transform(translation = (0.06, 0.48), rotation = -45+self.Rleg, children = ShapeGroup({
                'arm': Rectangle(-0.025, -0.025, 0.07, 0.33, fill = (0.8, 0.8, 0))
            })),
        }))
        })
        return person
