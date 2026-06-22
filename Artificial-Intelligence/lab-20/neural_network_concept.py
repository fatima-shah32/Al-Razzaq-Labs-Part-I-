import numpy as np

print("=== Lab 20: Intro to Neural Networks Concept ===")

# Task 1: Neuron example

x1 = 2
x2 = 3
x3 = 4

w1 = 0.5
w2 = 0.3
w3 = 0.2

weighted_sum = (w1 * x1) + (w2 * x2) + (w3 * x3)

print("\nNeuron Calculation:")
print("Weighted Sum:", weighted_sum)

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ReLU activation function
def relu(x):
    return np.maximum(0, x)

print("\nActivation Function Outputs:")
print("Sigmoid Output:", sigmoid(weighted_sum))
print("ReLU Output:", relu(weighted_sum))

# Task 2: Simple neural network diagram in text

diagram = """
Simple Neural Network Diagram

Input Layer        Hidden Layer        Output Layer

  X1  --------\\
               \\ 
  X2  ---------->   H1  --------\\
               /                 \\ 
  X3  --------/                   >   Output
                                /
                  H2  --------/
"""

print(diagram)

# Task 3: Key terminology summary

summary = """
Key Terminology:

Neuron:
A neuron is the basic unit of a neural network. It takes inputs,
multiplies them by weights, adds them together, and passes the result
through an activation function.

Activation Function:
An activation function adds non-linearity to the network. This helps
the neural network learn complex patterns. Examples include Sigmoid
and ReLU.

Layers:
Layers are groups of neurons. A neural network usually has an input
layer, one or more hidden layers, and an output layer.
"""

print(summary)

# Save summary report
with open("neural_network_summary.txt", "w") as file:
    file.write("Lab 20: Intro to Neural Networks Concept\n\n")
    file.write("Weighted Sum: " + str(weighted_sum) + "\n")
    file.write("Sigmoid Output: " + str(sigmoid(weighted_sum)) + "\n")
    file.write("ReLU Output: " + str(relu(weighted_sum)) + "\n\n")
    file.write(diagram)
    file.write("\n")
    file.write(summary)

print("Summary saved as neural_network_summary.txt")
print("\nLab completed successfully.")
