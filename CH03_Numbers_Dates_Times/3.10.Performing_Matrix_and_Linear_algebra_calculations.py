# @Time: 2022/4/13 21:18
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.10.Performing_Matrix_and_Linear_algebra_calculations.py


import numpy as np
from numpy import linalg as nlg

m = np.arange(9).reshape((3, 3))
print(m)
print(m.T)
# print(nlg.inv(m))

v = np.arange(2, 5).reshape(3, 1)
print(v)

print(m * v)
print(m @ v)

print(nlg.det(m))
print(nlg.eigvals(m))



# nlg.solve(m, v) #solve linear systems
