#import keras
from keras.models import Sequential
import keras.layers as l
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
import keras

#model itself
def LeNet(numOfClasses:int,inputSh):
    convNet = Sequential()
    convNet.add(l.Conv2D(32,3,input_shape = inputSh, activation="relu"))
    convNet.add(l.Conv2D(256,3,activation="relu"))
    convNet.add(l.MaxPooling2D())
    convNet.add(l.Flatten())
    convNet.add(l.Dense(1024,activation="relu"))
    convNet.add(l.Dense(numOfClasses,activation="softmax"))
    return convNet

def alexNetModel(num_classes,input_shape):
    model = Sequential()

    model.add(Conv2D(96,kernel_size=11,strides=4,input_shape=input_shape,activation="elu",padding='valid'))
    model.add(MaxPooling2D(pool_size=3,strides=2))

    model.add(keras.layers.BatchNormalization())
    model.add(Conv2D(256,kernel_size=5,strides=1,padding="same",activation="elu"))
    model.add(MaxPooling2D(pool_size=3,strides=2))


    model.add(keras.layers.BatchNormalization())

    model.add(Conv2D(384,kernel_size=3,strides=1,padding="same",activation="relu"))
                

    model.add(Conv2D(384,kernel_size=3,strides=1,padding="same",activation="relu"))
    model.add(Conv2D(256,kernel_size=3,strides=1,padding="same",activation="elu"))



    model.add(MaxPooling2D(pool_size=3,strides=2))


    model.add(Flatten())
    #model.add(keras.layers.Dropout(0.85))
    model.add(Dense(4096, activation='elu',kernel_regularizer=keras.regularizers.l2()))
    model.add(keras.layers.Dropout(0.5))
    model.add(Dense(4096, activation='elu'))
    model.add(keras.layers.Dropout(0.5))
    model.add(Dense(1000, activation='relu'))

    model.add(Dense(num_classes, activation='softmax'))

    return model