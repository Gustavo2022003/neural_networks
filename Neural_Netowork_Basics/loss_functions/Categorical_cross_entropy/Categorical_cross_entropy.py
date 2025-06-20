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

# NN Basics.
class Layer_Dense:
	def __init__(self, n_inputs, n_neurons):
		self.weight = 0.10 * np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))

	# Calculate the layer output.
	def forward(self, inputs):
		self.output = np.dot(np.array(inputs), self.weight) + self.biases

# Function to activate the neuron. if value > 0 returns the value or else returns 0.
class Activation_ReLU:
	def forward(self, inputs):
		self.output = np.maximum(0, inputs) # returns the highest value between 0 and every iterable in inputs

# NN Activation function, commonly used on the NN output. Returns the classes probabilities.
class Activation_softmax:
	def forward(self, inputs):
		exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
		probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)# Normalize the exponential output
		self.output = probabilities

class Loss:
	def calculate(self, output, y):
		sample_losses = self.forward(output, y)
		data_loss = np.mean(sample_losses)
		return data_loss
	
class Loss_CategoricalCrossEntropy(Loss):
	def forward(self, y_pred, y_true):
		samples = len(y_pred)
		y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)

# Creating the data in spiral with 100 samples for the 3 classes (33 samples for each)
X, y = spiral_data(samples=100, classes=3)

"""Setting up the layers"""

# Creating the first dense layer with 2 inputs and 3 neurons
dense1 = Layer_Dense(2, 3)
# Initializing the ReLU activation function
activation1 = Activation_ReLU()

# Creating the second dense layer with 3 inputs and 3 neurons
dense2 = Layer_Dense(3, 3)
# Initializing the softmax activation function
activation2 = Activation_softmax()

"""Giving the inputs"""

# Giving the first dense layer data from the spiral_data
dense1.forward(X)
# Activating the ReLU with the first layer output
activation1.forward(dense1.output)

# Getting the ReLU output and using it as the input of dense layer 2
dense2.forward(activation1.output)
# Activating the softmax function with the dense layer 2 output
activation2.forward(dense2.output)

# Printing the first 5 samples from the output batch
print(activation2.output[:5])