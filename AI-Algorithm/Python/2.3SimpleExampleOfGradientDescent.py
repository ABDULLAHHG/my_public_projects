import numpy as np 

x = np.array([1,2,3,4,5])
y = 20 * x + 5 

def SGD():
	m = b = 0
	n = len(x)
	lr = 0.05
	iter = 1000
	for i in range(iter):
		y_predict = m*x + b
		cost = 1/n * sum(val**2 for val in y-y_predict)
		md = -(2/n)*sum(x*(y-y_predict))
		bd = -(2/n)*sum(y-y_predict)
		
		m = m - md * lr 
		b = b - bd * lr
		
		print(f"M : {m:.2f} B : {b:.2f} Cost : {cost:.2f}")
		
SGD()

