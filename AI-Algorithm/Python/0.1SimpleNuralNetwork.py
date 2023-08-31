import numpy , random , os 
lr = 1 # Learning rate 
bias = 1 # Value of bias 
weights = [random.random(),random.random(),random.random()]
# Generate in a list (3 weights in total for 2 neurons and the bias)

def preceptron(input1 , input2 , output):
  outputP = input1*weights[0]+input2*weights[1]+bias*weights[2]
  if outputP > 0: # activation funtion (here Heaviside)
   outputP = 1
  else:
   outputP = 0
 
  error = output - outputP
  weights[0] += error * input1 * lr
  weights[1] += error * input2 * lr
  weights[2] += error * bias * lr

 
for i in range(50):
  preceptron(1,1,1) # True or True
  preceptron(0,1,1) # False or True
  preceptron(1,0,1) # True or False 
  preceptron(0,0,0) # False or False
  print(weights)
