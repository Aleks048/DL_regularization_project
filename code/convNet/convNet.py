#import keras
from keras.models import Sequential
import keras.layers as l

#inputShape???
#need the format of the data shape of the images to create data generator and other stuff
def LeNet(imgX:int,imgY:int,numOfClasses:int,inputShape):
    convNet = Sequential()
    convNet.add(l.Conv2D(32,3,activation="relu",inputShape=inputShape))
    convNet.add(l.Conv2D(64,3,activation="relu"))
    convNet.add(l.MaxPooling2D())
    convNet.add(l.Flatten())
    convNet.add(l.Dense(128,activation="relu"))
    convNet.add(l.Dense(numOfClasses,activation="softmax"))
    return convNet