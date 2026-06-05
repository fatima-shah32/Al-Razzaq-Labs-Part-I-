import tensorflow as tf
from tensorflow import keras
import numpy as np

# TensorFlow & Keras Versions
print("TensorFlow version:", tf.__version__)
print("Keras version:", keras.__version__)

# Create Model
model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1])
])

# Compile Model
model.compile(
    optimizer='sgd',
    loss='mean_squared_error'
)

# Training Data
xs = np.array(
    [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0],
    dtype=float
)

ys = np.array(
    [-3.0, -1.0, 1.0, 3.0, 5.0, 7.0],
    dtype=float
)

# Train Model
model.fit(xs, ys, epochs=500, verbose=0)

# Prediction
prediction = model.predict(
    np.array([10.0]),
    verbose=0
)

print("Prediction for 10.0:", prediction)
