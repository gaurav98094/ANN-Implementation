import tensorflow as tf

def create_model(input_shape,LOSS_FUNC,OPTIMIZER,metrics):
    LAYERS = [
          tf.keras.layers.Flatten(input_shape=input_shape,name="input"),
          tf.keras.layers.Dense(300,activation='sigmoid',name="hidden1"),
          tf.keras.layers.Dense(100,activation='sigmoid',name="hidden2"),
          tf.keras.layers.Dense(10,activation='softmax',name="output")
    ]
    model = tf.keras.models.Sequential(LAYERS)

    print(model.summary())


    model.compile(loss=LOSS_FUNC,optimizer=OPTIMIZER,metrics=metrics)

 
    return model
     