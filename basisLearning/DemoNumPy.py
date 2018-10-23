# -*- coding: utf-8 -*-
import numpy as np

print '''创建数组'''
arr1 = np.array([2, 3, 4])
print arr1
print '*' * 70 + '\n'

print '''函数向量化'''


def addSubtract(a, b):
    if (a > b):
        return a - b
    else:
        return a + b


vec_addSubtract = np.vectorize(addSubtract)
print vec_addSubtract([0, 3, 6, 9], [1, 3, 5, 7])
