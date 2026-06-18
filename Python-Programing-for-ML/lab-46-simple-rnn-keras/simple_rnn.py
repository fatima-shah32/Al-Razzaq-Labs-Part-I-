import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.optimizers import Adam

# Build Model
model = Sequential()

model.add(
    SimpleRNN(
        units=10,
        input_shape=(5, 1)
    )
)

model.add(Dense(units=1))

# Generate Training Data
X_train = np.array(
    [[[i + j] for i in range(5)]
     for j in range(1000)],
    dtype=float
)

y_train = np.array(
    [[i + 5] for i in range(1000)],
    dtype=float
)

# Compile Model
model.compile(
    optimizer=Adam(learning_rate=0.01),
    loss="mean_squared_error"
)

# Train Model
model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    verbose=1
)

# Test Data
X_test = np.array(
    [[[i + j] for i in range(5)]
     for j in range(100, 110)],
    dtype=float
)

y_test = np.array(
    [[i + 5] for i in range(100, 110)],
    dtype=float
)

# Evaluate
loss = model.evaluate(X_test, y_test)

print("\nTest Loss:", loss)

# Predict
y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred.flatten())
