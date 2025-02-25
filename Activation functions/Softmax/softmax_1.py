"""
Hidden layer activation functions (softmax)
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
		
class Activation_softmax:
	def forward(self, inputs):
		exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
		nom_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)# Normalize the exponential output

# Setting up the network structure
Layer1 = Layer_Dense(2, 5) # Initialize layer 1 with 2 inputs to 5 neurons
activation1 = Activation_ReLU()
Layer1.forward(X) # Using input data X to get output
activation1.forward(Layer1.output) # Using the activation function