import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
import time
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping

# Based on tutorial
# https://dashee87.github.io/data%20science/deep%20learning/python/another-keras-tutorial-for-neural-network-beginners/

# fix random seed for reproducibility
seed = 88
np.random.seed(seed)

# load pima indians dataset
dataset_path = os.path.join("data", "pima-indians-diabetes.csv")
dataset = pd.read_csv(dataset_path, header=None).values

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, 0:8], dataset[:, 8],
                                                    test_size=0.25, random_state=seed)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(5, input_dim=8, activation='relu')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

filepath = "nn_weights-{epoch:02d}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=0,
                                             save_weights_only=False, save_best_only=False, mode='max')

my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=1000, verbose=0, batch_size=X_train.shape[0],
                                     callbacks=[checkpoint], initial_epoch=0)

temp_test_model = Sequential()
temp_test_model.add(Dense(5, input_dim=8, activation='relu')) # hidden layer
temp_test_model.add(Dense(1, activation='sigmoid')) # output layer
temp_test_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

test_over_time = []
for i in range(len(my_first_nn_fitted.history['acc'])):
    temp_test_model.load_weights("nn_weights-%02d.hdf5" % i)
    scores = temp_test_model.evaluate(X_test, Y_test, verbose=0)
    # 0 is loss; 1 is accuracy
    test_over_time.append(scores)
