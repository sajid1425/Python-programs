import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.array([[11,22,33],[44,55,66],[77,88,99]])

print("Array1")
print(arr1)
print("Array2")
print(arr2)
#1. Arithmetic Operation
result=arr1+arr2
print("Result arr1+arr2")
print(result)

result=arr2-arr1
print("Result arr2-arr1")
print(result)

result=arr2*arr1
print("Result arr2*arr1")
print(result)

result=arr2/arr1
print("Result arr2/arr1")
print(result)

#2. Dot Product
print("Dot Product")
result=np.dot(arr1,arr2)
print(result)

#3. Sum
print("Sum")
result=np.sum(arr1)
print(result)

#4. Mean
print("Mean")
result=np.mean(arr1)
print(result)

#5. Min
print("Min")
result=np.min(arr1)
print(result)

#6. Max
print("Max")
result=np.max(arr1)
print(result)

#7. Transpose
print("Transpose of Array 1")
result=np.transpose(arr1)
print(result)