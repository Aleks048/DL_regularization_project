import tensorflow as tf

#import keras
import keras.layers as KL
import keras.models as KM
import keras


def CNN(input_shape, output_classes):
    input = KL.Input(shape =  (*input_shape, ))

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

def DARC1_categorical_crossentropy(reg, use_reg = False, alpha = 0.001):
    """
    alpha is the hyperparamter of the regularizer
    """
    if use_reg:
        def loss_fn(y_true, y_pred):
            original_loss = keras.losses.categorical_crossentropy(y_true, y_pred)
            return original_loss + alpha * reg
        return loss_fn
    else:
        return keras.losses.categorical_crossentropy

def train(training_generator, test_generator, epochs, use_multiprocessing=True, use_regularizer = False):
    
	model, reg = CNN((128, 128, 3), 5)
	loss_fn = DARC1_categorical_crossentropy(reg, use_regularizer)
	model.compile(optimizer = 'adam', loss = loss_fn, metrics = ['acc'])
	model.fit_generator(generator=training_generator,
                                    validation_data=test_generator,
                                    epochs=epochs,
                                    use_multiprocessing=False,
                                    workers=1,
                                    max_queue_size=1,
                                    verbose=1
                                    )

									
# if __name__ == "__main__":
#     train()