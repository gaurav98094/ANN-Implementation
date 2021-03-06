import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

from utils.common import get_unique_filename


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




def save_model(model, model_name,model_dr):
    unique_filename = get_unique_filename(model_name)+".h5"
    path = os.path.join(model_dr,unique_filename)
    model.save(path)

def save_plot(data,plot_name,plot_dr):
    unique_filename =get_unique_filename(plot_name)
    path = os.path.join(plot_dr,unique_filename)
    pd.DataFrame(data.history).plot(figsize=(10, 7))
    plt.grid(True)
    plt.savefig(path)