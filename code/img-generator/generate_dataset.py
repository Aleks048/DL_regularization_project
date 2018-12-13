import numpy as np
from dog import Dog
from truck import Truck
from airplane import Airplane
from person import Person
from frog import Frog

def generate_dataset(datapath = "/home/joel/datasets/csi5138-img/dataset1"): # do not add trailing /


    sigma = 0.01 # variance for generation
    mu = 0 # mean for generation

    N = 20 # number of images to generate

    #p = np.full((5), 0.2) # probability of drawing each class

    for i in range(N):
        c = np.random.randint(5)
        var = sigma * np.random.randn(5) + mu
        # no switch statement in Python?#yes noswitch statement in python
        if c == 0:
            obj = Dog(*var)
        elif c == 1:
            obj = Truck(*var)
        elif c == 2:
            obj = Airplane(*var)
        elif c == 3:
            obj = Person(*var)
        else:
            obj = Frog(*var)

        obj.generate(datapath, i)
