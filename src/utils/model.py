import tensorflow as tf
import time
import os

def create_model(input_shape, LOSS_FUNC, OPTIMIZER, metrics):
    LAYERS = [
        tf.keras.layers.Flatten(input_shape=input_shape, name="input"),
        tf.keras.layers.Dense(300, activation='sigmoid', name="hidden1"),
        tf.keras.layers.Dense(100, activation='sigmoid', name="hidden2"),
        tf.keras.layers.Dense(10, activation='softmax', name="output")
    ]
    model = tf.keras.models.Sequential(LAYERS)

    print(model.summary())

    model.compile(loss=LOSS_FUNC, optimizer=OPTIMIZER, metrics=metrics)

    return model


def get_unique_filename(filename):
    unique_filename = time.strftime(f"{filename}_%Y-%m-%d_T_%H_%M_%S.h5")
    return unique_filename


def save_model(model, model_name,model_dr):
    unique_filename = get_unique_filename(model_name)
    path = os.path.join(model_dr,unique_filename)
    model.save(path)
