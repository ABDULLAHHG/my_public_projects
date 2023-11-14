import numpy as np 
import matplotlib.pyplot as plt 
import random

def y_function(x):
    return np.sin(2*x)

def y_derivative(x):
    return 2*np.cos(2*x)

x = np.arange(-5,5,0.1)
y = y_function(x)
n = random.randint(-5,5)
current_pos = (n , y_function(n))

learning_rate = 0.1

for _ in range(1000):
    new_x = current_pos[0] - y_derivative(current_pos[0]) * learning_rate
    new_y = y_function(new_x)
    current_pos = (new_x , new_y)

    plt.plot(x , y)
    plt.scatter(current_pos[0],current_pos[1] , color = 'red')
    plt.pause(0.001)
    plt.clf()

