import numpy as np

def perceptron(entrees, poids, biais):
    z = np.dot(entrees, poids) + biais
    return 1 if z >= 0 else 0

# À compléter :
poids = np.array([ 0.5 , 0.5 ])
biais = -0.2

# Tests attendus : [0,0]->0  [1,0]->1  [0,1]->1  [1,1]->1
print(perceptron(np.array([0, 0]), poids, biais))
print(perceptron(np.array([1, 0]), poids, biais))
print(perceptron(np.array([0, 1]), poids, biais)) 
print(perceptron(np.array([1, 1]), poids, biais))