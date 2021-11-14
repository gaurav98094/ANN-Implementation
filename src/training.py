
import argparse
import os

from utils.callbacks import get_callbacks

from utils.common import read_config
from utils.data_mgmt import get_data
from utils.model import create_model, save_model, save_plot


def training(config_path):
    config = read_config(config_path)

    valid_data_size = config["params"]["validation_datasize"]
    (X_train, y_train), (X_val, y_val), (X_test, y_test) = get_data(valid_data_size)

    LOSS_FUNC = config["params"]["loss_function"]
    OPTIMIZER = config["params"]["optimizer"]
    metrics = [config["params"]["metrics"]]
    input_shape = config["params"]["input_shape"]

    model = create_model(input_shape, LOSS_FUNC, OPTIMIZER, metrics)

    EPOCHS = config["params"]["epochs"]
    VALIDATION = (X_val, y_val)

    CALLBACK_LIST = get_callbacks(config,X_train)

    history = model.fit(X_train, y_train, epochs=EPOCHS, validation_data=VALIDATION, callbacks= CALLBACK_LIST)


    model_name = config["artifacts"]["model_name"]
    model_dir = config["artifacts"]["model_dir"]
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    model_dir_path = os.path.join(artifacts_dir, model_dir)
    os.makedirs(model_dir_path, exist_ok=True)

    save_model(model, model_name, model_dir_path)

    plot_name = config["artifacts"]["plot_name"]
    plot_dir = config["artifacts"]["plots_dir"]
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    plot_dir_path = os.path.join(artifacts_dir, plot_dir)
    os.makedirs(plot_dir_path, exist_ok=True)
    save_plot(history, plot_name,plot_dir_path)





if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config.yaml")

    parsed_args = args.parse_args()

    training(config_path=parsed_args.config)
