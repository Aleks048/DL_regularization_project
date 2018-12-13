
from simple_object import *

class Truck(Simple_Object):
    def __init__(self, rot = 0, sc = 0.9, head = 0, body = 0, wheel = 0):
        super(Truck, self).__init__()
        self.name = "truck"
        self.rotation = rot
        self.scale = sc
        self.head = head
        self.body = body
        self.wheel = wheel
        self.shape = self.shape()

    def shape(self):
        truck = ShapeGroup({
            'root': Transform(translation = (0.5, 0.2), children = ShapeGroup({
            'head1': Rectangle(-0.3, 0.17, 0.1, 0.2, fill = (0, 0, 0.9)),
            'head2': Rectangle(-0.2, 0.1, 0.25 + self.head, 0.2, fill = (0, 0, 0.9)),
            'body': Rectangle(-0.3, 0.27, 0.7 + self.body, 0.2, fill = (0.8, 0, 0)),
            'front_wheels': Circle(-0.15, 0.5, 0.07 + self.wheel, fill = (0.8, 0.8, 0)),
            'back_wheels': Circle(0.2, 0.5, 0.07 + self.wheel, fill = (0.8, 0.8, 0)),
            }))
        })
        return truck
