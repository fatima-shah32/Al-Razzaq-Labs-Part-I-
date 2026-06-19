import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Create synthetic dataset
X = np.random.rand(100, 8)
Y = np.random.randint(2, size=(100, 1))

# Build Sequential model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# Train model
model.fit(X, Y, epochs=150, batch_size=10, verbose=0)

# Evaluate training performance
loss, accuracy = model.evaluate(X, Y, verbose=0)
print(f"Training Loss: {loss:.4f}")
print(f"Training Accuracy: {accuracy:.4f}")

# Create test dataset
X_test = np.random.rand(20, 8)
Y_test = np.random.randint(2, size=(20, 1))

# Evaluate test performance
test_loss, test_accuracy = model.evaluate(X_test, Y_test, verbose=0)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")
