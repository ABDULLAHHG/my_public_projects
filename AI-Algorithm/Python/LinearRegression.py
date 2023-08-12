import numpy as np 

class LinearRegression:
    def __init__(self, learning_rate = 0.01,num_iterations = 100):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations 
        self.weights = None
        self.bias = None
    
    def fit(self , X ,y):
        # Initialize the weights and bais to zero
        n_samples , n_features = X.shape
        self.weights = np.zeros(n_features).reshape(1,1)
        self.bias = 0
        # Gradient descebt 
        for _ in range(self.num_iterations):
            # Compute the predictions and the errors 
            y_pred = np.dot(X , self.weights) + self.bias
            errors = y - y_pred

            # Update the weight and bias 
            self.weights += (self.learning_rate * np.dot(X.T,errors)/n_samples)
            self.bias += (self.learning_rate * np.sum(errors)/n_samples)

    def predict(self,X):
        # Compute the predictions using the learned weight and bias
        return np.dot(X,self.weights)+self.bias 

# Generate some random data
X = np.random.rand(100,1)
y = 2 * X + 1 + np.random.randn(100,1) * 0.1

# Fit a linear regression model to the data 
lr = LinearRegression(learning_rate = 0.1 ,num_iterations = 1000)
lr.fit(X,y)

# Predict the target values for new data 
X_new = np.array([[0.5],[0.6],[0.7]])
y_pred = lr.predict(X_new)
print(y_pred)
        
