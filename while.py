#Import
import numpy as np
import random as rd

#Variabler
input_data = np.array([1,2])    #Input af data
number_of_training = 2 #Antal af træninger
target_value = 15    #Dette er hvad den skal ramme
target_value_area = 0.02 #Området af usikkerhed den må har
training_rate = 0.1
start_value = 0
final_numbers_of_training = 0   #Antal af træninger
output = 0

#Funktioner
def sigmoid(x):
    return 1/(1+np.exp(-x))
def slope(x):
    return 2*(x-target_value)
def relu(x):
    return max(0,x)

#Vægte
weight = dict()
weight['output'] = np.array([rd.uniform(-1,1),rd.uniform(-1,1)])
a = weight['output']
start_value = (weight['output']*input_data).sum()
print("før træning: ")
print(start_value)   
print("Vægtenes ændring under træning")
print(weight['output'])

while output != target_value:
    output = (weight['output']*input_data).sum()
    print(output)
    weight['output'] = weight['output'] - training_rate *slope(output)
    print("\n\nEfter træning:")
    print(weight['output'])
    output = round(output, 8)
    final_numbers_of_training += 1  #Antal af træninger tælles
    print(final_numbers_of_training)
