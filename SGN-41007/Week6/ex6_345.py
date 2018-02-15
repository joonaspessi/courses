import numpy as np
from utils import absolute_file_paths
from skimage import io
from sklearn.model_selection import train_test_split
from os.path import join, dirname, realpath

from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import to_categorical

dir_path = dirname(realpath(__file__))


def get_data():
    X = []
    y = []

    basePath = join(dir_path, "..", "common", "data", "GTSRB_subset_2")
    imageFileNamesClass1 = absolute_file_paths([join(basePath, "class1")])
    for imgPath in imageFileNamesClass1:
        X.append(io.imread(imgPath))
        y.append(0)

    imageFileNamesClass2 = absolute_file_paths([join(basePath, "class2")])
    for imgPath in imageFileNamesClass2:
        X.append(io.imread(imgPath))
        y.append(1)

    X = (X - np.min(X)) / np.max(X)
    y = to_categorical(y,2)

    return X, y


if __name__ == "__main__":
    X ,y = get_data()

    X_train, X_cv, y_train, y_cv = train_test_split(X, y, train_size=0.8)

    model = Sequential()

    N = 32  # Number of feature maps
    w, h = 5, 5  # Conv. window size

    model.add(Conv2D(N, (w, h), input_shape=(64, 64, 3), activation="relu", padding="same"))
    model.add(MaxPooling2D(pool_size=(4, 4)))
    model.add(Conv2D(N, (w, h), activation="relu", padding="same"))
    model.add(MaxPooling2D((4, 4)))
    model.add(Flatten())
    model.add(Dense(100, activation="sigmoid"))
    model.add(Dense(2, activation="sigmoid"))

    model.summary()

    model.compile(optimizer="SGD", loss="categorical_crossentropy", metrics=["accuracy"])

    model.fit(X_train, y_train, batch_size=32, epochs=20)

    scores = model.evaluate(X_cv, y_cv)

    print("Cross validation %s: %.2f%%" % (model.metrics_names[1], scores[1]*100))