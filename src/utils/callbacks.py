
import tensorflow as tf
import os

from utils.common import get_unique_filename

import numpy as np


def get_callbacks(config,X_train):

    logs = config["logs"]
    fname = get_unique_filename("tb_logs")

    TENSOROARD_ROOT_LOG_DIR = os.path.join(logs["logs_dir"],logs["tensorboard_logs"],fname)
    os.makedirs(TENSOROARD_ROOT_LOG_DIR,exist_ok=True)



    tensorboard_cb = tf.keras.callbacks.TensorBoard(log_dir=TENSOROARD_ROOT_LOG_DIR)
    file_writer = tf.summary.create_file_writer(logdir=TENSOROARD_ROOT_LOG_DIR)

    with file_writer.as_default():
        images = np.reshape(X_train[10:30], (-1, 28, 28, 1))  ### <<< 20, 28, 28, 1
        tf.summary.image("20 handritten digit samples", images, max_outputs=25, step=0)



    patience = config["params"]["patience"]
    restore_best_weights = config["params"]["restore_best_weights"]
    early_stop = tf.keras.callbacks.EarlyStopping(patience=patience, restore_best_weights=restore_best_weights)



    ckpt_dir = os.path.join(config["artifacts"]["artifacts_dir"],config["artifacts"]["checkpoint_dir"],fname)
    ckpt_path = os.path.join(ckpt_dir,"model_ckpt.h5")
    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(ckpt_path, save_best_only=True)


    CALLBACK_LIST = [tensorboard_cb, early_stop, checkpoint_callback]

    return CALLBACK_LIST


