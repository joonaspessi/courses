from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.layers import Dense, Flatten

# Disable annoying tensorflow cpu support warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == "__main__":

    base_model = VGG16(include_top=False, weights="imagenet", input_shape=(64, 64, 3))
    w = base_model.output
    w = Flatten()(w)
    w = Dense(100, activation="relu")(w)
    output = Dense(2, activation="sigmoid")(w)
    model = Model(inputs=[base_model.input], outputs=[output])
    model.summary()
