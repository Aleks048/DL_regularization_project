#import keras
from keras.models import Sequential
import keras.layers as l

#model itself
def LeNet(numOfClasses:int,inputSh):
    convNet = Sequential()
    convNet.add(l.Conv2D(32,3,input_shape = inputSh, activation="relu"))
    convNet.add(l.Conv2D(64,3,activation="relu"))
    convNet.add(l.MaxPooling2D())
    convNet.add(l.Flatten())
    convNet.add(l.Dense(128,activation="relu"))
    convNet.add(l.Dense(numOfClasses,activation="softmax"))
    return convNet