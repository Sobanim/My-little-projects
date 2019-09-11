import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


training_inputs = np.array([[3, 2, 1, 4],
                            [1, 2, 4, 3],
                            [4, 2, 1, 3],
                            [2, 4, 3, 1]])

training_outputs = np.array([[4, 3, 1, 2]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((4, 1)) - 1

print("Random initial weight")
print(synaptic_weights)

# Method backpropagation
for i in range(110000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    err = training_outputs - outputs
    adjustments = np.dot( input_layer.T, err * (outputs * (1 - outputs)) )

    synaptic_weights += adjustments

print("Weight after learinig:")
print(synaptic_weights)

print("Result after learning")
print(outputs)

new_inputs = np.array([0, 2, 0, 1])
output = sigmoid ( np.dot( new_inputs, synaptic_weights))

print("New situation")
print(output)
print("Weights new situation")
print(synaptic_weights)
