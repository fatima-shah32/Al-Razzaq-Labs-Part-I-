import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Simple Attention Mechanism Lab")

# Sample text dataset
sentences = [
    "i love machine learning",
    "attention improves models",
    "deep learning is powerful",
    "tensorflow makes ai easier"
]

# Tokenization
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

max_len = max(len(seq) for seq in sequences)

padded = tf.keras.preprocessing.sequence.pad_sequences(
    sequences,
    maxlen=max_len,
    padding='post'
)

vocab_size = len(tokenizer.word_index) + 1

# Inputs and targets
X = padded
y = padded

# Attention Layer
class SimpleAttention(tf.keras.layers.Layer):

    def __init__(self, units):
        super(SimpleAttention, self).__init__()

        self.W_a = tf.keras.layers.Dense(units)
        self.U_a = tf.keras.layers.Dense(units)
        self.V_a = tf.keras.layers.Dense(1)

    def call(self, encoder_states, decoder_hidden):

        decoder_hidden = tf.expand_dims(decoder_hidden, 1)

        score = self.V_a(
            tf.nn.tanh(
                self.W_a(encoder_states) +
                self.U_a(decoder_hidden)
            )
        )

        attention_weights = tf.nn.softmax(score, axis=1)

        context_vector = attention_weights * encoder_states

        context_vector = tf.reduce_sum(
            context_vector,
            axis=1
        )

        return context_vector, attention_weights


# Build Model
inputs = tf.keras.layers.Input(shape=(max_len,))

embedding = tf.keras.layers.Embedding(
    vocab_size,
    16
)(inputs)

encoder_output = tf.keras.layers.LSTM(
    32,
    return_sequences=True,
    return_state=True
)

encoder_states, state_h, state_c = encoder_output(
    embedding
)

attention_layer = SimpleAttention(32)

context_vector, attention_weights = attention_layer(
    encoder_states,
    state_h
)

dense_output = tf.keras.layers.Dense(
    vocab_size,
    activation='softmax'
)(context_vector)

model = tf.keras.Model(
    inputs=inputs,
    outputs=dense_output
)

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# Dummy targets
targets = np.array([seq[0] for seq in sequences])

# Train
history = model.fit(
    X,
    targets,
    epochs=10,
    verbose=1
)

# Save model
model.save("attention_model.keras")

print("Model Saved")

# Plot Accuracy
plt.figure(figsize=(8,5))

plt.plot(history.history['accuracy'])

plt.title("Training Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.savefig("accuracy_plot.png")

plt.show()

# Extract attention weights
attention_model = tf.keras.Model(
    inputs=model.input,
    outputs=attention_weights
)

sample_attention = attention_model.predict(X[:1])

print("Attention Shape:", sample_attention.shape)

# Visualize attention
plt.figure(figsize=(8,4))

sns.heatmap(
    sample_attention.squeeze(),
    cmap='viridis',
    annot=True
)

plt.title("Attention Weights")

plt.savefig("attention_heatmap.png")

plt.show()

# Generate report
with open("project_report.txt", "w") as f:

    f.write("Lab 41 - Simple Attention Mechanism\n\n")
    f.write("Concepts:\n")
    f.write("- Query\n")
    f.write("- Key\n")
    f.write("- Value\n")
    f.write("- Attention Weights\n")
    f.write("- Context Vector\n\n")
    f.write("Model: LSTM + Attention\n")
    f.write("Dataset: Small Text Dataset\n")

print("Report Generated")
