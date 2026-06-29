import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Flatten, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from sklearn.manifold import TSNE

print("=== Lab 19: Building a Simple Embedding Layer ===")

# Task 1: Prepare small text dataset
texts = [
    "this movie is good",
    "this film is excellent",
    "i love this movie",
    "this story is amazing",
    "this movie is bad",
    "this film is terrible",
    "i hate this movie",
    "this story is boring"
]

labels = np.array([1, 1, 1, 1, 0, 0, 0, 0])

vocab_size = 1000
embedding_dim = 50
max_length = 10

# Tokenize text
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(texts)

sequences = tokenizer.texts_to_sequences(texts)

X_data = pad_sequences(
    sequences,
    maxlen=max_length,
    padding="post"
)

y_data = labels

print("\nTokenized sequences:")
print(X_data)

print("\nWord Index:")
print(tokenizer.word_index)

# Task 2: Build model with Embedding layer
model = Sequential([
    Embedding(
        input_dim=vocab_size,
        output_dim=embedding_dim,
        input_length=max_length
    ),
    Flatten(),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print("\nModel Summary:")
model.summary()

# Train model
history = model.fit(
    X_data,
    y_data,
    epochs=20,
    batch_size=2,
    verbose=1
)

# Evaluate on same small dataset
loss, accuracy = model.evaluate(X_data, y_data, verbose=0)

print("\nTraining Accuracy:", round(accuracy, 4))

# Save model
model.save("embedding_model.keras")

# Save training history
history_df = pd.DataFrame(history.history)
history_df.to_csv("embedding_training_history.csv", index=False)

# Plot training accuracy and loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Accuracy")
plt.plot(history.history["loss"], label="Loss")
plt.title("Embedding Model Training History")
plt.xlabel("Epoch")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.savefig("embedding_training_history.png")
plt.close()

# Task 3: Extract embeddings
embeddings = model.layers[0].get_weights()[0]

# Use only actual words from tokenizer
word_index = tokenizer.word_index
words = list(word_index.keys())
word_ids = list(word_index.values())

embedding_vectors = np.array([
    embeddings[word_id]
    for word_id in word_ids
])

# t-SNE needs perplexity less than number of samples
perplexity_value = max(2, min(5, len(words) - 1))

tsne = TSNE(
    n_components=2,
    random_state=42,
    perplexity=perplexity_value
)

reduced_embeddings = tsne.fit_transform(embedding_vectors)

# Save reduced embeddings
embedding_df = pd.DataFrame({
    "word": words,
    "x": reduced_embeddings[:, 0],
    "y": reduced_embeddings[:, 1]
})

embedding_df.to_csv("reduced_embeddings.csv", index=False)

# Plot t-SNE embeddings
plt.figure(figsize=(8, 6))
plt.scatter(
    reduced_embeddings[:, 0],
    reduced_embeddings[:, 1]
)

for i, word in enumerate(words):
    plt.annotate(
        word,
        (reduced_embeddings[i, 0], reduced_embeddings[i, 1])
    )

plt.title("t-SNE Visualization of Learned Embeddings")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.tight_layout()
plt.savefig("embedding_tsne_plot.png")
plt.close()

# Save report
with open("embedding_report.txt", "w") as file:
    file.write("Lab 19: Building a Simple Embedding Layer\n\n")
    file.write("Dataset: Small sentiment text dataset\n")
    file.write(f"Vocabulary Size Setting: {vocab_size}\n")
    file.write(f"Embedding Dimension: {embedding_dim}\n")
    file.write(f"Maximum Sequence Length: {max_length}\n")
    file.write(f"Training Accuracy: {accuracy:.4f}\n\n")
    file.write("Word Index:\n")
    file.write(str(tokenizer.word_index))
    file.write("\n\nObservation:\n")
    file.write("The embedding layer converts words into dense vectors.\n")
    file.write("These vectors are learned during training and can capture simple relationships from text data.\n")
    file.write("t-SNE was used to reduce embeddings to 2D for visualization.\n")

print("\nFiles saved:")
print("embedding_model.keras")
print("embedding_training_history.csv")
print("embedding_training_history.png")
print("reduced_embeddings.csv")
print("embedding_tsne_plot.png")
print("embedding_report.txt")

print("\nLab completed successfully.")
