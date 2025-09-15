import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image, ImageOps   # pillow for image ops

# load mnist data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0

# make model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# train model
model.fit(x_train, y_train, epochs=5)

# test acc
test_loss, test_acc = model.evaluate(x_test, y_test)
print("model acc is:", test_acc)

# ======== user input image =========
file = input("pls write image file name: ")

# open img
img = Image.open(file).convert("L")   # gray
img = ImageOps.invert(img)            # make white bg, black digit
img = img.resize((28,28))             # resize
img_array = np.array(img)

# normalize
img_array = img_array / 255.0

# reshape to 28x28 coz model want
img_array = img_array.reshape(1,28,28)

# predict
pred = model.predict(img_array)
num = np.argmax(pred)
print("number in img is:", num)
