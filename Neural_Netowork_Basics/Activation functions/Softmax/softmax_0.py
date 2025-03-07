"""
Hidden layer activation functions (Softmax)
"""
import numpy as np
import nnfs

nnfs.init()

layer_outputs = [[4.8, 1.21, 2.385], 
                [8.9, -1.81, 0.2],
                [1.41, 1.051, 0.026]]

exp_values = np.exp(layer_outputs) # Get the exponential values from the layer_outputs
norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True) # Normalize the exponential output

print(norm_values)