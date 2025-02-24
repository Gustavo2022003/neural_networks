"""
Primeira implementação de redes neurais: camadas densas e propagação direta.
"""

import numpy as np

np.random.seed(0)

# Dados de entrada X
X = [[1, 2, 3, 2.5],
	[2.0, 5.0, -1.0, 2.0],
	[-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
	def __init__(self, n_inputs, n_neurons):
		self.weight = 0.10 * np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))

	# Calcula a saída da camada
	def forward(self, inputs):
		self.output = np.dot(inputs, self.weight) + self.biases

# Definindo a estrutura da rede
Layer1 = Layer_Dense(4, 5) # 4 entradas para 5 neurônios
Layer2 = Layer_Dense(5, 2) # 5 entradas para 2 neurônios


Layer1.forward(X) # inicializa a camada 1 com os valores de X
Layer2.forward(Layer1.output) # inicializa a camada 2 com os valores de saída da camada 1

print(Layer2.output) # Imprime no terminal os valores de saída da camada 2