"""
Hidden layer activation functions (ReLU)
"""

import numpy as np

# nnfs (Neural Network From Scratch)
import nnfs
from nnfs.datasets import spiral_data

"""
Initializing the nnfs lib
- Defines a fixed seed for the random numbers generator (numpy.random.seed)
- Configures the numpy default dtype to float32
- etc...
"""
nnfs.init()

# Input data X
X = [[1, 2, 3, 2.5],
	[2.0, 5.0, -1.0, 2.0],
	[-1.5, 2.7, 3.3, -0.8]]


# Generates data in spiral. 100 (number of samples), 3 (number of classes)
X, y = spiral_data(100, 3)

class Layer_Dense:
	def __init__(self, n_inputs, n_neurons):
		self.weight = 0.10 * np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))

	# Calculate the layer output
	def forward(self, inputs):
		self.output = np.dot(np.array(inputs), self.weight) + self.biases

class Activation_ReLU:
	def forward(self, inputs):
		self.output = np.maximum(0, inputs) # returns the highest value between 0 and every iterable in inputs

# Setting up the network structure
Layer1 = Layer_Dense(2, 5) # Initialize layer 1 with 2 inputs to 5 neurons
activation1 = Activation_ReLU()
Layer1.forward(X) # Using input data X to get output
activation1.forward(Layer1.output) # Using the activation function