import datetime
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, AveragePooling2D, MaxPooling2D
from tensorflow.keras import Model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.losses import categorical_crossentropy
import datetime

def create_model():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(kernel_regularizer=tf.keras.regularizers.l2(0.01), filters=6, kernel_size=(5, 5), strides=(1,1), activation='tanh', input_shape=X_train.shape[1:4], padding="same"))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(5, activation='softmax'))

    return model

def create_transfer_learning_model(X_train):
    base_model = tf.keras.applications.MobileNet(input_shape=X_train.shape[1:4],
                                                   include_top=False,
                                                   weights='imagenet')
    base_model.trainable = True
    
    model = tf.keras.models.Sequential()
    model.add(base_model)
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(5, activation='softmax'))
    
    return model

def train_model(X_train, y_train):
    model = create_transfer_learning_model(X_train)
    model.summary()
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    model.fit(x=X_train, 
              y=y_train,
              batch_size=140, #140
              epochs=6) #100 (for my own network)
    #           validation_data=(X_val, y_val)) 
    
    return model
