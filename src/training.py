from yaml.parser import Parser
from utils.common import read_config

from utils.data_mgmt import get_data
from utils.model import create_model


import argparse

def training(config_path):
    config = read_config(config_path)
    
    valid_data_size = config["params"]["validation_datasize"]
    (X_train,y_train),(X_val,y_val),(X_test,y_test) = get_data(valid_data_size)

    LOSS_FUNC = config["params"]["loss_function"]
    OPTIMIZER = config["params"]["optimizer"]
    metrics = [config["params"]["metrics"]]
    input_shape = config["params"]["input_shape"]


    model = create_model(input_shape,LOSS_FUNC,OPTIMIZER,metrics)


    EPOCHS = config["params"]["epochs"]
    VALIDATION = (X_val,y_val)

    history = model.fit(X_train,y_train,epochs=EPOCHS,validation_data=VALIDATION)


    return model
 




if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config.yaml")

    parsed_args = args.parse_args()

    training(config_path=parsed_args.config)