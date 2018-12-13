import numpy as np
from dog import Dog
from truck import Truck
from airplane import Airplane
from person import Person
from frog import Frog

def generate_dataset(N = 100,
    sigma = 0.1, mu = 0,
    balanced_sample = True, # equal number of each class
    p = [1./5]*5, # for multinomial distribution of classes
    datapath = "/home/joel/datasets/csi5138-img/dataset1"): # do not add trailing /

    for i in range(N):
        if balanced_sample:
            c = i % 5
        else:
            c = np.random.multinomial(1, p) # choose class from distribution p
            c = np.argmax(c)
        # construct vector of N(mu, sigma**2)
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
