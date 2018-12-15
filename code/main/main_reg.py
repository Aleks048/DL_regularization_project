import importlib.util
import os
import sys
sys.path.insert(0, '../img-generator')
sys.path.insert(0, '../convNet')

import convNet_reg
import getDataGenerators
from dataFeeder import *
from myImage import *

# import generate_dataset
# generate_dataset.generate_dataset(N = 20000,datapath = "..\DataSet")
#param param param
img_x = 128 #reshaped the images, to reasonable size!!!!!!!
img_y = 128
batch  = 30
numClasses = 5
numOfChannels = 3

inputShape = (img_x,img_y,numOfChannels)

optimizer = keras.optimizers.SGD(0.001)
loss = keras.losses.cosine_proximity

epochs = 10

#model compiling training

training_generator,test_generator =getDataGenerators.getDataGenerators((img_x,img_y),batch,numClasses,numOfChannels,False,"../DataSet")

# for x,y in training_generator:
#     print(y)
#     break
convNet_reg.train(training_generator, test_generator, epochs, use_regularizer = False)