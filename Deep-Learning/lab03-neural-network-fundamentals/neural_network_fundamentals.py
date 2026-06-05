import numpy as np

# -------------------------
# Neural Network Structure
# -------------------------

print("Basic Neural Network Architecture")

print("""
Input Layer      Hidden Layer      Output Layer
  (3 Nodes)        (4 Nodes)         (2 Nodes)

   [I1] ----------> [H1]
   [I2] ----------> [H2]
   [I3] ----------> [H3]
                    [H4]

                      |
                      v

                   [O1]
                   [O2]
""")

# -------------------------
# Input Data
# -------------------------

input_features = np.array([[1, 2, 3]])

hidden_layer_size = 4
output_layer_size = 2

# -------------------------
# Activation Functions
# -------------------------

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

# -------------------------
# Initialize Weights
# -------------------------

np.random.seed(42)

weights_input_hidden = np.random.rand(
    3,
    hidden_layer_size
)

weights_hidden_output = np.random.rand(
    hidden_layer_size,
    output_layer_size
)

# -------------------------
# Hidden Layer Processing
# -------------------------

hidden_input = np.dot(
    input_features,
    weights_input_hidden
)

hidden_output = sigmoid(hidden_input)

relu_output = relu(hidden_input)

print("Hidden Layer Output (Sigmoid):")
print(hidden_output)

print("\nHidden Layer Output (ReLU):")
print(relu_output)

# -------------------------
# Feedforward Function
# -------------------------

def feedforward(
    input_data,
    weights_input_hidden,
    weights_hidden_output
):

    hidden_input = np.dot(
        input_data,
        weights_input_hidden
    )

    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(
        hidden_output,
        weights_hidden_output
    )

    final_output = sigmoid(final_input)

    return final_output

# -------------------------
# Run Feedforward
# -------------------------

output = feedforward(
    input_features,
    weights_input_hidden,
    weights_hidden_output
)

print("\nFeedforward Output:")
print(output)
