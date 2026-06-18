# Lab 46: Implementing a Simple Recurrent Neural Network

## Objective

Understand the architecture and implementation of a simple Recurrent Neural Network (RNN) using TensorFlow/Keras.

---

## Task 1: Build RNN Model

### Import Libraries

```python
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.optimizers import Adam
```

### Create Model

```python
model = Sequential()

model.add(SimpleRNN(units=10, input_shape=(5,1)))
model.add(Dense(units=1))
```

---

## Task 2: Train on Sequential Data

### Generate Data

```python
X_train = np.array(
    [[[i+j] for i in range(5)]
     for j in range(1000)],
    dtype=float
)

y_train = np.array(
    [[i+5] for i in range(1000)],
    dtype=float
)
```

### Compile Model

```python
model.compile(
    optimizer=Adam(learning_rate=0.01),
    loss="mean_squared_error"
)
```

### Train Model

```python
model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32
)
```

---

## Task 3: Evaluate Model

### Evaluate

```python
loss = model.evaluate(X_test, y_test)
print(loss)
```

### Predict

```python
y_pred = model.predict(X_test)
print(y_pred)
```

---

## Summary

| Component      | Purpose               |
| -------------- | --------------------- |
| SimpleRNN      | Sequential learning   |
| Dense Layer    | Output prediction     |
| Adam Optimizer | Training optimization |
| MSE Loss       | Error calculation     |

---

## Conclusion

In this lab, I implemented a simple Recurrent Neural Network using Keras, trained it on sequential numerical data, evaluated its performance, and generated sequence predictions.
