import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.models as KM
import tensorflow.keras.layers as KL

def CNN(input_shape, output_classes):
    input = KL.Input(shape = (*input_shape, ))

    x = input
    x = KL.Conv2D(32, 5, activation = 'relu')(x)
    x = KL.MaxPooling2D()(x)

    x = KL.Conv2D(32, 5, activation = 'relu')(x)
    x = KL.MaxPooling2D()(x)

    x = KL.Flatten()(x)
    x = KL.Dense(1024, activation = 'relu')(x)
    x = KL.Dense(output_classes, activation = 'softmax')(x)

    output = x

    # compute DARC1 regularization term
    log_softmax_x = tf.log(x)
    regularizer = tf.reduce_max(tf.reduce_sum(tf.abs(log_softmax_x), axis=0))

    return KM.Model(input, output), regularizer

def DARC1_sparse_categorical_crossentropy(regularizer, alpha = 0.001):
    """
    alpha is the hyperparamter of the regularizer
    """
    def loss_fn(y_true, y_pred):
        original_loss = keras.losses.sparse_categorical_crossentropy(y_true, y_pred)
        return original_loss + alpha * regularizer

    return loss_fn

def train():
    model, regularizer = CNN((512, 512, 3), 3)

    model.compile(optimizer = 'adam', loss = DARC1_sparse_categorical_crossentropy(regularizer), metrics = ['acc'])
    
    # model.fit

if __name__ == "__main__":
    train()