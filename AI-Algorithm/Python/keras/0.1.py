from keras.layers import Input
from keras.layers import Dense 
from keras.layers import Lambda
from keras import Model

# Create an input layers 
inp1 = Input(10)
inp2 = Input(20)

# Next we create a Lambda layer 
lambda_layer = Lambda(lambda x:x+1)

# apply lambda layer 
a1 = lambda_layer(inp1)
b1 = lambda_layer(a1)
c1 = lambda_layer(b1)
d1 = lambda_layer(c1)
e1 = lambda_layer(d1)
f1 = lambda_layer(e1)
g1 = lambda_layer(f1)

# Create a model 
model = Model(inp1 , [g1 , a1])

# Show model summary
model.summary()