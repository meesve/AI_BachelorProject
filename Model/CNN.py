import numpy as np 
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from sklearn.utils import class_weight

from tensorflow import keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Activation
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
from sklearn.model_selection import train_test_split
from keras import callbacks

import pickle
import time

NAME = "facade-classifier-3classes-4conv-48x2-128x1-64x1{}".format(int(time.time()))

tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))

X = np.array(pickle.load(open("/Users/meesveldt/Documents/uni/bachelor_project/Model_testing/X.pickle_IMG_BIGWO3final", "rb")))
y = np.array(pickle.load(open("/Users/meesveldt/Documents/uni/bachelor_project/Model_testing/y.pickle_IMG_BIGWO3final", "rb")))

X = X/255.0
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

class_weights = class_weight.compute_class_weight(class_weight = "balanced", classes= np.unique(y), y= y)
class_weights = dict(enumerate(class_weights))

def build_model():
    model = Sequential()
    model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:], activation='relu'))
    model.add(MaxPooling2D(2,2))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(2,2))

    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D(2,2))

    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D(2,2))

    model.add(Flatten())
    model.add(Dense(3, activation='softmax'))

    model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  optimizer='adam',
                  metrics=['accuracy'])
    return model

model = build_model()
model.fit(X_train, y_train, batch_size=64, epochs=40, validation_data=(X_test, y_test), class_weight=class_weights, callbacks =[tensorboard])
model.summary()