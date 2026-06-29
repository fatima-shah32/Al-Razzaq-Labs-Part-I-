import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

print("=== Lab 18: Text Generation with RNNs ===")

# Task 1: Prepare small text corpus
text = """
alice was beginning to get very tired of sitting by her sister on the bank.
she had nothing to do and once or twice she had peeped into the book.
the rabbit ran close by her and said oh dear oh dear i shall be late.
alice followed the rabbit and found herself in a curious world of wonder.
"""

text = text.lower()
text = text.replace("\n", " ")

with open("alice_in_wonderland.txt", "w") as file:
    file.write(text)

print("\nText corpus created successfully")
print("Text length:", len(text), "characters")

# Character mappings
chars = sorted(list(set(text)))

char_to_index = {
    char: index
    for index, char in enumerate(chars)
}

index_to_char = {
    index: char
    for index, char in enumerate(chars)
}

print("Unique characters:", len(chars))

# Task 2: Create sequences
seq_length = 40
step = 1

sequences = []
next_chars = []

for i in range(0, len(text) - seq_length, step):
    sequences.append(text[i:i + seq_length])
    next_chars.append(text[i + seq_length])

print("Number of sequences:", len(sequences))

X = np.zeros(
    (len(sequences), seq_length, len(chars)),
    dtype=bool
)

y = np.zeros(
    (len(sequences), len(chars)),
    dtype=bool
)

for i, sequence in enumerate(sequences):
    for t, char in enumerate(sequence):
        X[i, t, char_to_index[char]] = 1

    y[i, char_to_index[next_chars[i]]] = 1

print("\nInput shape:", X.shape)
print("Target shape:", y.shape)

# Build character-level RNN/LSTM model
model = Sequential([
    LSTM(
        128,
        input_shape=(seq_length, len(chars))
    ),
    Dense(
        len(chars),
        activation="softmax"
    )
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nModel Summary:")
model.summary()

# Train model
history = model.fit(
    X,
    y,
    batch_size=32,
    epochs=20,
    verbose=1
)

# Text generation function
def generate_text(seed_text, num_chars):
    input_text = seed_text.lower()
    generated_text = seed_text

    for _ in range(num_chars):
        x_pred = np.zeros(
            (1, seq_length, len(chars))
        )

        for t, char in enumerate(input_text):
            if char in char_to_index:
                x_pred[0, t, char_to_index[char]] = 1

        preds = model.predict(
            x_pred,
            verbose=0
        )[0]

        next_index = np.argmax(preds)
        next_char = index_to_char[next_index]

        generated_text += next_char
        input_text = input_text[1:] + next_char

    return generated_text

# Generate sample text
seed_text = text[:seq_length]
generated_text = generate_text(seed_text, 300)

print("\nGenerated Text:\n")
print(generated_text)

with open("generated_text.txt", "w") as file:
    file.write(generated_text)

# Save model
model.save("text_generation_rnn.keras")

# Save training history
history_df = pd.DataFrame(history.history)
history_df.to_csv("training_history.csv", index=False)

# Plot loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.title("Text Generation RNN Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("training_loss.png")
plt.close()

# Save report
with open("text_generation_report.txt", "w") as file:
    file.write("Lab 18: Text Generation with RNNs\n\n")
    file.write("Dataset: Small Alice-inspired text corpus\n")
    file.write(f"Text Length: {len(text)} characters\n")
    file.write(f"Unique Characters: {len(chars)}\n")
    file.write(f"Sequence Length: {seq_length}\n")
    file.write(f"Number of Sequences: {len(sequences)}\n\n")
    file.write("Model Architecture:\n")
    file.write("LSTM(128) -> Dense(vocabulary size, softmax)\n\n")
    file.write("Generated Text:\n")
    file.write(generated_text)
    file.write("\n\nObservation:\n")
    file.write("Character-level RNNs can learn local character patterns but may generate repetitive or imperfect text on small datasets.\n")

print("\nFiles saved:")
print("alice_in_wonderland.txt")
print("generated_text.txt")
print("text_generation_rnn.keras")
print("training_history.csv")
print("training_loss.png")
print("text_generation_report.txt")

print("\nLab completed successfully.")
