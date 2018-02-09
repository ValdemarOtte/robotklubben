"""

A 12, inc. production

Jacob Bluhm, CEO

"""

import numpy as np
import random as rd

input_0 = 1
input_1 = 2
target_value = 10
learning_rate = 0.1
number_of_training = 15
input_data = np.array([input_0,input_1])

def sigmoid(x):
	return 1/(1+np.exp(-x))

def slope(x):
	return 2*(x-target_value)

def relu(x):
	return max(0,x)



weight = dict()
weight['output'] = np.array([rd.uniform(-1,1), rd.uniform(-1,1)])
output = (weight['output']*input_data).sum()
print(output)
print(weight['output'])
for i in range(number_of_training):
	output = (weight['output']*input_data).sum()
	weight['output'] = weight['output']-learning_rate * slope(output)
	
print(weight['output'])
print(output)
