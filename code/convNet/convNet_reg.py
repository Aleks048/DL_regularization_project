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
    reg = tf.reduce_max(tf.reduce_sum(tf.abs(log_softmax_x), axis=0))

    return KM.Model(input, output), reg

def DARC1_sparse_categorical_crossentropy(reg, alpha = 0.001):
    """
    alpha is the hyperparamter of the regularizer
    """
    def loss_fn(y_true, y_pred):
        original_loss = keras.losses.sparse_categorical_crossentropy(y_true, y_pred)
        return original_loss + alpha * reg

    return loss_fn

def train(use_regularizer = False):
    model, reg = CNN((512, 512, 3), 3)

    loss_fn = DARC1_sparse_categorical_crossentropy(reg) if use_regularizer else keras.losses.sparse_categorical_crossentropy
    model.compile(optimizer = 'adam', loss = loss_fn, metrics = ['acc'])
    
    # model.fit

if __name__ == "__main__":
    train()