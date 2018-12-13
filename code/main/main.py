import importlib.util
import os
import sys
sys.path.insert(0, '../img-generator')
sys.path.insert(0, '../convNet')
import generate_dataset
import convNet
import getDataGenerators
from dataFeeder import *
from myImage import *


#param param param
img_x = 128#reshaped the images, to reasonable size!!!!!!!
img_y = 128
batch  = 15
numClasses = 5
numOfChannels = 3

inputShape = (img_x,img_y,numOfChannels)

optimizer = keras.optimizers.Adam()
loss = keras.losses.categorical_crossentropy

epochs = 10


#model compiling training

training_generator,test_generator =getDataGenerators.getDataGenerators((img_x,img_y),batch,numClasses,numOfChannels,False,"../DataSet")

model = convNet.LeNet(numClasses,inputShape)

model.compile(loss=loss,
                   optimizer = optimizer
                   ,metrics=['accuracy'])

model.fit_generator(generator=training_generator,
                                    validation_data=test_generator,
                                    epochs=epochs,
                                    use_multiprocessing=False,
                                    workers=1,
                                    max_queue_size=1,
                                    verbose=1
                                    )   