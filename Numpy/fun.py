# Shape & Reshape
import numpy as np
print("2D Array")
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array Shape ",arr.shape)
rearr=arr.reshape(1,9)
print("ReShaped Array ",rearr)
print("Array Shape ",rearr.shape)
