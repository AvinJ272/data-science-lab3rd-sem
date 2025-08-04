import numpy as np
ar1= np.array([[1,2],[5,6]])
ar2= np.array([[4,7],[8,9]])
print("add two matrix")
print(np.add(ar1,ar2))


print("subtract two matrix")
print(np.subtract(ar1,ar2))

print("multiply two matrix")
print(np.multiply(ar1,ar2))

print("divide two matrix")
print(np.divide(ar1,ar2))

print("perform matrix multiplication")
print(np.dot(ar1,ar2))

print("display the trasnsponse of the matricesa")
print(ar1.transpose)
print(ar2.transpose)

print("sum of diagonal element of the matrices")
print(np.trace(ar1))
print(np.trace(ar2))