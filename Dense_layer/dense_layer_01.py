"""
Dense layer and direct propagation
"""

import numpy as np

np.random.seed(0)

# Input data X
X = [[1, 2, 3, 2.5],
	[2.0, 5.0, -1.0, 2.0],
	[-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
	def __init__(self, n_inputs, n_neurons):
		self.weight = 0.10 * np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))

	# Calculate the layer output
	def forward(self, inputs):
		self.output = np.dot(inputs, self.weight) + self.biases

# Setting up the network structure
Layer1 = Layer_Dense(4, 5) # 4 inputs to 5 neurons
Layer2 = Layer_Dense(5, 2) # 5 inputs to 2 neurons


Layer1.forward(X) # Initialize layer 1 with the input data X
Layer2.forward(Layer1.output) # Initialize layer 2 with the output data from layer 1

print(Layer2.output) # Print the output from layer 2