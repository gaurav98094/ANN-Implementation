import tensorflow as tf



def get_data(valid_data_size):
    mnist = tf.keras.datasets.mnist
    (X_train_full,y_train_full),(X_test,y_test) = mnist.load_data()

    # Train Set
    X_train = X_train_full[valid_data_size:]/255.
    y_train = y_train_full[valid_data_size:]

    # Validation Set
    X_val = X_train_full[:valid_data_size]/255. 
    y_val = y_train_full[:valid_data_size]

    # Test Set
    X_test = X_test/255.
    y_test = y_test


    return (X_train,y_train),(X_val,y_val),(X_test,y_test)
