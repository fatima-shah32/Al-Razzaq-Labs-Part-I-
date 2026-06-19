# Lab 43: Working with Neural Networks using Keras

## Objective

Understand how to build, train, and evaluate a simple neural network using Keras.

## Task 1: Build a Simple Sequential Model

### Import Libraries

```python
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
Create Sequential Model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
Key Concepts
Input Layer

The model uses 8 input features.

Hidden Layers

Dense layers are used with ReLU activation.

Output Layer

The output layer uses sigmoid activation for binary classification.

Task 2: Compile the Model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
Task 3: Train the Model
X = np.random.rand(100, 8)
Y = np.random.randint(2, size=(100, 1))

model.fit(X, Y, epochs=150, batch_size=10, verbose=0)
Task 4: Evaluate Model Performance
loss, accuracy = model.evaluate(X, Y, verbose=0)
Test Performance
X_test = np.random.rand(20, 8)
Y_test = np.random.randint(2, size=(20, 1))

test_loss, test_accuracy = model.evaluate(X_test, Y_test, verbose=0)
Evaluation Metrics
Loss

Loss shows how far the model prediction is from the actual result.

Accuracy

Accuracy shows how many predictions were correct.

Conclusion

In this lab, I learned how to create a simple neural network using Keras Sequential model. I trained the model on a synthetic dataset and evaluated its performance using loss and accuracy on training and test data.
